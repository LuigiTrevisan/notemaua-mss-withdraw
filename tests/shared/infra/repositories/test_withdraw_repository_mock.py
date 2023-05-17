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
        repo = WithdrawRepositoryMock()
        assert True    