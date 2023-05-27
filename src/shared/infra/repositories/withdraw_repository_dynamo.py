from datetime import datetime
import random
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.environments import Environments
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from src.shared.infra.dto.withdraw_dynamo_dto import WithdrawDynamoDTO

class WithdrawRepositoryDynamo(IWithdrawRepository):
    @staticmethod
    def partition_key_format(withdraw: Withdraw) -> str:
        return f'{withdraw.num_serie}'
    
    @staticmethod
    def sort_key_format(withdraw: Withdraw) -> str:
        return f'withdraw#{withdraw.email}#{withdraw.withdraw_id}'
    
    @staticmethod
    def gsi1_partition_key_format(withdraw: Withdraw) -> str:
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
        
    def create_withdraw(self, num_serie: str, email: str) -> Withdraw:
        withdraw_time = int(datetime.now().timestamp() * 1000)
        withdraw_id = random.randint(0, 999999999)
        withdraw = Withdraw(withdraw_id=withdraw_id, email=email, num_serie=num_serie, withdraw_time=withdraw_time, finish_time=None)
        item = WithdrawDynamoDTO.from_entity(withdraw).to_dynamo()
        item[self.dynamo.gsi_partition_key] = self.gsi1_partition_key_format(withdraw)
        
        resp = self.dynamo.put_item(item=item, partition_key=self.partition_key_format(withdraw), sort_key=self.sort_key_format(withdraw))
        
        return withdraw        
        