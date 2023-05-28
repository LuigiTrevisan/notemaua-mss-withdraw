import pytest
from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock
from src.shared.infra.repositories.withdraw_repository_dynamo import WithdrawRepositoryDynamo


class Test_WithdrawRepositoryDynamo:
    
    @pytest.mark.skip(reason="can't test locally")
    def test_withdraw_repository_dynamo_create_withdraw(self):
        withdraw_repository_dynamo = WithdrawRepositoryDynamo()
        withdraw_repository_mock = WithdrawRepositoryMock()
        withdraw_id = len(withdraw_repository_mock.withdraws) + 1
        withdraw = Withdraw(
            num_serie='34095',
            email="22.01589-2@maua.br",
            withdraw_id=withdraw_id,
            withdraw_time=1682604600000,
            )
        withdraw = withdraw_repository_dynamo.create_withdraw(withdraw)
        
    @pytest.mark.skip(reason="can't test locally")
    def test_withdraw_repository_dynamo_create_notebook(self):
        withdraw_repository_dynamo = WithdrawRepositoryDynamo()
        withdraw_repository_mock = WithdrawRepositoryMock()
        notebook = Notebook(
            num_serie='34095',
            isActive=False
        )
        notebook = withdraw_repository_dynamo.create_notebook(notebook)
        
    @pytest.mark.skip(reason="can't test locally")
    def test_withdraw_repository_dynamo_get_withdraws_by_email(self):
        withdraw_repository_dynamo = WithdrawRepositoryDynamo()
        withdraws = withdraw_repository_dynamo.get_withdraws_by_email("22.01102-0@maua.br")
        assert len(withdraws) > 0
        assert isinstance(withdraws[0], Withdraw)
        
    @pytest.mark.skip(reason="can't test locally")
    def test_withdraw_repository_dynamo_get_withdraws_by_num_serie(self):
        withdraw_repository_dynamo = WithdrawRepositoryDynamo()
        withdraws = withdraw_repository_dynamo.get_withdraws_by_num_serie("34036")
        assert len(withdraws) > 0
        
    @pytest.mark.skip(reason="can't test locally")
    def test_withdraw_repository_dynamo_get_notebook(self):
        withdraw_repository_dynamo = WithdrawRepositoryDynamo()
        notebook = withdraw_repository_dynamo.get_notebook("34035")
        
    @pytest.mark.skip(reason="can't test locally")
    def test_withdraw_repository_dynamo_get_active_withdraw(self):
        withdraw_repository_dynamo = WithdrawRepositoryDynamo()
        withdraw = withdraw_repository_dynamo.get_active_withdraw("34038")
        
    @pytest.mark.skip(reason="can't test locally")
    def test_withdraw_repository_dynamo_finish_withdraw(self):
        withdraw_repository_dynamo = WithdrawRepositoryDynamo()
        withdraw = Withdraw(
            withdraw_id=2,
            num_serie='34038',
            email="22.01049-0@maua.br",
            withdraw_time=1682611052153
        )
        new_withdraw = withdraw_repository_dynamo.finish_withdraw(withdraw)
        
    # @pytest.mark.skip(reason="can't test locally")
    def test_withdraw_repository_dynamo_get_all_notebooks(self):
        withdraw_repository_dynamo = WithdrawRepositoryDynamo()
        notebooks = withdraw_repository_dynamo.get_all_notebooks()
        assert True