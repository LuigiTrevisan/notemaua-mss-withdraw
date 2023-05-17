from datetime import datetime
import pytest
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

class Test_WithdrawRepositoryMock:
    
    def test_get_withdraw_by_email(self):
        repo = WithdrawRepositoryMock()
        withdraw = repo.get_withdraw_by_email("22.01102-0@maua.br")
        assert withdraw.withdraw_id == repo.withdraws[0].withdraw_id
        assert withdraw.num_serie == repo.withdraws[0].num_serie
        assert withdraw.email == repo.withdraws[0].email
        assert withdraw.withdraw_time == repo.withdraws[0].withdraw_time
        assert withdraw.finish_time == repo.withdraws[0].finish_time

    def test_get_withdraw_by_num_serie(self):
        repo = WithdrawRepositoryMock()
        withdraw = repo.get_withdraw_by_num_serie("34038")
        assert withdraw.withdraw_id == repo.withdraws[1].withdraw_id
        assert withdraw.num_serie == repo.withdraws[1].num_serie
        assert withdraw.email == repo.withdraws[1].email
        assert withdraw.withdraw_time == repo.withdraws[1].withdraw_time
        assert withdraw.finish_time == repo.withdraws[1].finish_time
        
    def test_get_notebook(self):
        repo = WithdrawRepositoryMock()
        notebook = repo.get_notebook("34038")
        assert notebook.num_serie == "34038"
        assert notebook.isActive == True
        
    def test_get_user_by_email(self):
        repo = WithdrawRepositoryMock()
        user = repo.get_user_by_email("22.01102-0@maua.br")
        assert user.ra == repo.users[0].ra
        assert user.name == repo.users[0].name
        assert user.email == repo.users[0].email
        assert user.role == repo.users[0].role
            
    def test_create_withdraw(self):
        repo = WithdrawRepositoryMock()
        num_serie = "34139"
        email = "22.01102-0@maua.br"
        len_before = len(repo.withdraws)
        withdraw = repo.create_withdraw(num_serie, email)
        assert withdraw.withdraw_id == 4
        assert withdraw.num_serie == num_serie
        assert withdraw.email == email
        assert withdraw.withdraw_time == int(datetime.now().timestamp() * 1000)
        assert withdraw.finish_time == None
        assert len(repo.withdraws) == len_before + 1
        