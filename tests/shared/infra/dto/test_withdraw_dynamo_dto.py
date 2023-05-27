from src.shared.domain.entities.withdraw import Withdraw
from src.shared.infra.dto.withdraw_dynamo_dto import WithdrawDynamoDTO


class Test_WithdrawDynamoDTO:
    
    def test_withdraw_dynamo_dto_from_entity(self):
        withdraw = Withdraw(withdraw_id=6, num_serie="34036", email="22.01102-0@maua.br", withdraw_time=1685194260000)
        withdraw_dto = WithdrawDynamoDTO.from_entity(withdraw)
        assert withdraw_dto == WithdrawDynamoDTO(withdraw_id=6, num_serie="34036", email="22.01102-0@maua.br", withdraw_time=1685194260000, finish_time=None)
        
    def test_withdraw_dynamo_dto_to_dynamo(self):
        withdraw_dto = WithdrawDynamoDTO(withdraw_id=6, num_serie="34036", email="22.01102-0@maua.br", withdraw_time=1685194260000, finish_time=None)
        assert withdraw_dto.to_dynamo() == {
            "entity" : "withdraw",
            "withdraw_id": 6,
            "num_serie": "34036",
            "email": "22.01102-0@maua.br",
            "withdraw_time": 1685194260000,
        }
        
    def test_withdraw_dynamo_dto_from_dynamo(self):
        withdraw_dto = WithdrawDynamoDTO.from_dynamo({
            "entity" : "withdraw",
            "withdraw_id": 6,
            "num_serie": "34036",
            "email": "22.01102-0@maua.br",
            "withdraw_time": 1685194260000,
            "finish_time": 1685194268000
        })
        
        assert withdraw_dto == WithdrawDynamoDTO(withdraw_id=6, num_serie="34036", email="22.01102-0@maua.br", withdraw_time=1685194260000, finish_time=1685194268000)
        
    def test_withdraw_dynamo_dto_to_entity(self):
        withdraw_dto = WithdrawDynamoDTO(withdraw_id=6, num_serie="34036", email="22.01102-0@maua.br", withdraw_time=1685194260000, finish_time=None)
        assert withdraw_dto.to_entity() == Withdraw(withdraw_id=6, num_serie="34036", email="22.01102-0@maua.br", withdraw_time=1685194260000, finish_time=None)
        
    def test_withdraw_dynamo_dto_from_entity_to_dynamo(self):
        withdraw = Withdraw(withdraw_id=6, num_serie="34036", email="22.01102-0@maua.br", withdraw_time=1685194260000)
        withdraw_dto = WithdrawDynamoDTO.from_entity(withdraw).to_dynamo()
        assert withdraw_dto == {
            "entity" : "withdraw",
            "withdraw_id": 6,
            "num_serie": "34036",
            "email": "22.01102-0@maua.br",
            "withdraw_time": 1685194260000,
        }
        
    def test_withdraw_dynamo_dto_from_dynamo_to_entity(self):
        withdraw = WithdrawDynamoDTO.from_dynamo({
            "entity" : "withdraw",
            "withdraw_id": 6,
            "num_serie": "34036",
            "email": "22.01102-0@maua.br",
            "withdraw_time": 1685194260000,
            "finish_time": 1685194268000
        }).to_entity()
        
        assert withdraw == Withdraw(withdraw_id=6, num_serie="34036", email="22.01102-0@maua.br", withdraw_time=1685194260000, finish_time=1685194268000)