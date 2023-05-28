import pytest
from datetime import datetime
from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

class Test_WithdrawRepositoryMock:
    
    def test_get_withdraws_by_email(self):
        repo = WithdrawRepositoryMock()
        withdraws = repo.get_withdraws_by_email("22.01102-0@maua.br")
        assert len(withdraws) == 2
        assert withdraws[0] == repo.withdraws[0]
        assert withdraws[1] == repo.withdraws[3]
        assert withdraws[0].email == "22.01102-0@maua.br"
        assert withdraws[1].email == "22.01102-0@maua.br"
        
    def test_get_withdraws_by_num_serie(self):
        repo = WithdrawRepositoryMock()
        withdraws = repo.get_withdraws_by_num_serie("34038")
        assert len(withdraws) == 2
        assert withdraws[0] == repo.withdraws[1]
        assert withdraws[1] == repo.withdraws[3]
        assert withdraws[0].num_serie == "34038"
        assert withdraws[1].num_serie == "34038"
        
    def test_get_notebook(self):
        repo = WithdrawRepositoryMock()
        notebook = repo.get_notebook("34038")
        assert notebook.num_serie == "34038"
        assert notebook.isActive == True
            
    def test_create_withdraw(self):
        repo = WithdrawRepositoryMock()
        num_serie = "34139"
        email = "22.01102-0@maua.br"
        len_before = len(repo.withdraws)
        withdraw = Withdraw(withdraw_id=len_before, num_serie=num_serie, email=email, withdraw_time=int(datetime.now().timestamp() * 1000))
        repo.create_withdraw(withdraw)
        assert withdraw.withdraw_id == len_before
        assert withdraw.num_serie == num_serie
        assert withdraw.email == email
        assert withdraw.withdraw_time == int(datetime.now().timestamp() * 1000)
        assert withdraw.finish_time == None
        assert len(repo.withdraws) == len_before + 1
        
    def test_finish_withdraw(self):
        repo = WithdrawRepositoryMock()
        num_serie = repo.withdraws[1].num_serie
        len_before = len(repo.withdraws)
        withdraw = repo.finish_withdraw(num_serie)
        assert withdraw.withdraw_id == repo.withdraws[1].withdraw_id
        assert withdraw.num_serie == repo.withdraws[1].num_serie
        assert withdraw.email == repo.withdraws[1].email
        assert withdraw.withdraw_time == repo.withdraws[1].withdraw_time
        assert withdraw.finish_time == int(datetime.now().timestamp() * 1000)
        assert len(repo.withdraws) == len_before
        assert repo.get_notebook(num_serie).isActive == False
        
    def test_get_all_notebooks(self):
        repo = WithdrawRepositoryMock()
        notebooks = repo.get_all_notebooks()
        assert len(notebooks) == 4
        assert type(notebooks) == list
        assert type(notebooks[1]) == tuple
        assert type(notebooks[1][0]) == Notebook
        assert type(notebooks[1][1]) == list
        
    def test_create_notebook(self):
        repo = WithdrawRepositoryMock()
        notebook = Notebook(num_serie="34139", isActive=False)
        len_before = len(repo.notebooks)
        notebook = repo.create_notebook(notebook)
        assert notebook.num_serie == "34139"
        assert notebook.isActive == False
        assert len(repo.notebooks) == len_before + 1
        assert repo.notebooks[-1] == notebook