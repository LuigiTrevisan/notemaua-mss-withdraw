from datetime import datetime
import random
from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.environments import Environments
from src.shared.infra.dto.notebook_dynamo_dto import NotebookDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from src.shared.infra.dto.withdraw_dynamo_dto import WithdrawDynamoDTO
from boto3.dynamodb.conditions import Key

class WithdrawRepositoryDynamo(IWithdrawRepository):
    
    @staticmethod
    def notebook_partition_key_format(num_serie: str) -> str:
        return f'{num_serie}'
    
    @staticmethod
    def notebook_sort_key_format(num_serie: str) -> str:
        return f'notebook#{num_serie}'
    
    @staticmethod
    def withdraw_partition_key_format(num_serie: str) -> str:
        return f'{num_serie}'
    
    @staticmethod
    def withdraw_sort_key_format(email: str, withdraw_id: str) -> str:
        return f'withdraw#{email}#{withdraw_id}'
    
    @staticmethod
    def gsi1_withdraw_partition_key_format(email: str) -> str:
        return f'{email}'
    
    def __init__(self):
        self.dynamo = DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_table_name,
            region=Environments.get_envs().region,
            partition_key=Environments.get_envs().dynamo_partition_key,
            sort_key=Environments.get_envs().dynamo_sort_key,
            gsi_partition_key=Environments.get_envs().dynamo_gsi_partition_key,
            )
        print(f"Variáveis:\n{Environments.get_envs().__dict__}")
        
    def create_withdraw(self, withdraw: Withdraw) -> Withdraw:
        item = WithdrawDynamoDTO.from_entity(withdraw).to_dynamo()
        item[self.dynamo.gsi_partition_key] = self.gsi1_withdraw_partition_key_format(withdraw.email)
        resp = self.dynamo.put_item(item=item, partition_key=self.withdraw_partition_key_format(withdraw.num_serie), sort_key=self.withdraw_sort_key_format(email=withdraw.email, withdraw_id=withdraw.withdraw_id))
        
        return withdraw        
    
    def create_notebook(self, notebook: Notebook) -> Notebook:
        item = NotebookDynamoDTO.from_entity(notebook).to_dynamo()
        resp = self.dynamo.put_item(item=item, partition_key=self.notebook_partition_key_format(notebook.num_serie), sort_key=self.notebook_sort_key_format(notebook.num_serie))
        return notebook
    
    def get_withdraws_by_email(self, email):
        query_string = Key(self.dynamo.gsi_partition_key).eq(email)
        response = self.dynamo.query(IndexName="GSI1", key_condition_expression=query_string)
        
        withdraws = [WithdrawDynamoDTO.from_dynamo(item).to_entity() for item in response['Items']]
            
        return withdraws
    
    def get_withdraws_by_num_serie(self, num_serie):
        query_string = Key(self.dynamo.partition_key).eq(num_serie) & Key(self.dynamo.sort_key).begins_with('withdraw#')
        response = self.dynamo.query(key_condition_expression=query_string)
        
        withdraws = [WithdrawDynamoDTO.from_dynamo(item).to_entity() for item in response['Items']]
        
        return withdraws
    
    def get_notebook(self, num_serie):
        query_string = Key(self.dynamo.partition_key).eq(num_serie)
        response = self.dynamo.query(key_condition_expression=query_string)
        if response["Count"] == 0:
            return None
        notebook_data = response['Items'][0]
        notebook_data['isActive'] = False
        if len(response['Items']) > 1:
            for item in response['Items'][1:]:
                if item.get("finish_time") is None:
                    notebook_data['isActive'] = True
        notebook = NotebookDynamoDTO.from_dynamo(notebook_data).to_entity()
        
        return notebook
    
    def get_active_withdraw(self, num_serie):
        query_string = Key(self.dynamo.partition_key).eq(num_serie) & Key(self.dynamo.sort_key).begins_with('withdraw#')
        response = self.dynamo.query(key_condition_expression=query_string)
        withdraw_data = None
        for item in response['Items']:
            if item.get("finish_time") is None:
                withdraw_data = item
        withdraw = WithdrawDynamoDTO.from_dynamo(withdraw_data).to_entity() if withdraw_data is not None else None
        
        return withdraw
        
    def finish_withdraw(self, withdraw: Withdraw):
        finish_time = int(datetime.now().timestamp() * 1000)
        response = self.dynamo.update_item(
            partition_key=self.withdraw_partition_key_format(withdraw.num_serie),
            sort_key=self.withdraw_sort_key_format(email=withdraw.email, withdraw_id=withdraw.withdraw_id),
            update_dict={
                "finish_time": finish_time
            }
        )
        updated_withdraw = WithdrawDynamoDTO.from_dynamo(response['Attributes']).to_entity()
        return updated_withdraw
        
    def get_all_notebooks(self):
        response = self.dynamo.get_all_items()
        notebooks = []
        for i in range(len(response['Items'])):
            if response['Items'][i]['entity'] == 'notebook':
                notebook_data = response['Items'][i]
                notebook_data['isActive'] = False
                j = i + 1
                withdraws = []
                while j < len(response['Items']) and response['Items'][j]['entity'] == 'withdraw':
                    withdraws.append(WithdrawDynamoDTO.from_dynamo(response['Items'][j]).to_entity())
                    if response['Items'][j].get("finish_time") is None:
                        notebook_data['isActive'] = True
                    j += 1
                notebook = NotebookDynamoDTO.from_dynamo(notebook_data).to_entity()
                notebooks.append((notebook, withdraws))
                
        return notebooks