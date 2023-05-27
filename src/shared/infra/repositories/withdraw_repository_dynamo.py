from datetime import datetime
import random
from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.environments import Environments
from src.shared.infra.dto.notebook_dynamo_dto import NotebookDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from src.shared.infra.dto.withdraw_dynamo_dto import WithdrawDynamoDTO

class WithdrawRepositoryDynamo(IWithdrawRepository):
    
    @staticmethod
    def notebook_partition_key_format(notebook: Notebook) -> str:
        return f'{notebook.num_serie}'
    
    @staticmethod
    def notebook_sort_key_format(notebook: Notebook) -> str:
        return f'notebook#{notebook.num_serie}'
    
    @staticmethod
    def withdraw_partition_key_format(withdraw: Withdraw) -> str:
        return f'{withdraw.num_serie}'
    
    @staticmethod
    def withdraw_sort_key_format(withdraw: Withdraw) -> str:
        return f'withdraw#{withdraw.email}#{withdraw.withdraw_id}'
    
    @staticmethod
    def gsi1_withdraw_partition_key_format(withdraw: Withdraw) -> str:
        return f'withdraw#{withdraw.email}'
    
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
        item[self.dynamo.gsi_partition_key] = self.gsi1_withdraw_partition_key_format(withdraw)
        resp = self.dynamo.put_item(item=item, partition_key=self.withdraw_partition_key_format(withdraw), sort_key=self.withdraw_sort_key_format(withdraw))
        
        return withdraw        
    
    def create_notebook(self, notebook: Notebook) -> Notebook:
        item = NotebookDynamoDTO.from_entity(notebook).to_dynamo()
        resp = self.dynamo.put_item(item=item, partition_key=self.notebook_partition_key_format(notebook), sort_key=self.notebook_sort_key_format(notebook))
        return notebook