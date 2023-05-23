import pytest
from src.modules.create_withdraw.app.create_withdraw_usecase import CreateWithdrawUsecase
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock


class Test_CreateWithdrawUsecase:
    
    def test_create_withdraw_usecase(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo=repo)
        lenBefore = len(repo.withdraws)
        
        withdraw = usecase(num_serie='34037', email="arthur@maua.br")

        assert len(repo.withdraws) == lenBefore + 1
        assert repo.withdraws[-1] == withdraw
        
    def test_create_withdraw_usecase_with_notebook_not_found(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            usecase(num_serie='30398', email="arthur@maua.br")
            
    def test_create_withdraw_usecase_with_notebook_already_withdrawn(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo=repo)
        with pytest.raises(DuplicatedItem):
            usecase(num_serie='34038', email="arthur@maua.br")
            
    def test_create_withdraw_usecase_with_user_not_found(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            usecase(num_serie='34037', email="juninho@maua.br")
            
    def test_create_withdraw_usecase_with_user_already_with_notebook(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo=repo)
        with pytest.raises(DuplicatedItem):
            usecase(num_serie='34037', email="22.01102-0@maua.br") 