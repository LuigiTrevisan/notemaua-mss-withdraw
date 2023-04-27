import pytest
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

class Test_WithdrawRepositoryMock:
    def test_repo(self):
        repo = WithdrawRepositoryMock()
        assert True    