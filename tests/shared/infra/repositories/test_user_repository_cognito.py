import pytest
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role import ROLE

from src.shared.infra.repositories.user_repository_cognito import UserRepositoryCognito


class Test_UserRepositoryCognito:
    def test_get_user_by_email(self):
        repo = UserRepositoryCognito()
        user = repo.get_user_by_email("21.00596-6@maua.br")
        assert user == User(
            ra="21005966",
            name="Eduardo Garcia Moretti",
            email="21.00596-6@maua.br",
            role=ROLE.STUDENT
        )