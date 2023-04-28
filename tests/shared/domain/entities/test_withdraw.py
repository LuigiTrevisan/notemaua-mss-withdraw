import pytest
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.helpers.errors.domain_errors import EntityError

class Test_Withdraw:
    
    def test_withdraw(self):
        withdraw = Withdraw(
            num_serie="34756",
            email="22.01102-0@maua.br",
            withdraw_time=1682508271948,
            finish_time=None
        )
        
        assert type(withdraw) == Withdraw
        assert withdraw.num_serie == "34756"
        assert withdraw.email == "22.01102-0@maua.br"
        assert withdraw.withdraw_time == 1682508271948
        assert withdraw.finish_time == None
        
    def test_withdraw_withdraw_time_is_none(self):
        with pytest.raises(EntityError):
            withdraw = Withdraw(
            num_serie="34756",
            email="22.01102-0@maua.br",
            withdraw_time=None,
            finish_time=None
        )
            
    def test_withdraw_withdraw_time_not_int(self):
        with pytest.raises(EntityError):
            withdraw = Withdraw(
            num_serie="34756",
            email="22.01102-0@maua.br",
            withdraw_time="1682508271948",
            finish_time=None
        )
            
    def test_withdraw_withdraw_time_past(self):
        with pytest.raises(EntityError):
            withdraw = Withdraw(
            num_serie="34756",
            email="22.01102-0@maua.br",
            withdraw_time=1071972000000,
            finish_time=None
        )
            
    def test_withdraw_return_time_not_int(self):
        with pytest.raises(EntityError):
            withdraw = Withdraw(
            num_serie="34756",
            email="22.01102-0@maua.br",
            withdraw_time=1682508271948,
            finish_time="1682509207926"
        )
            
    def test_withdraw_return_time_past(self):
        with pytest.raises(EntityError):
            withdraw = Withdraw(
            num_serie="34756",
            email="22.01102-0@maua.br",
            withdraw_time=1682508271948,
            finish_time=1071972000000
        )
            
    def test_withdraw_return_time_smaller_than_withdraw(self):
        with pytest.raises(EntityError):
            withdraw = Withdraw(
            num_serie="34756",
            email="22.01102-0@maua.br",
            withdraw_time=1682509207926,
            finish_time=1682508271948
        )