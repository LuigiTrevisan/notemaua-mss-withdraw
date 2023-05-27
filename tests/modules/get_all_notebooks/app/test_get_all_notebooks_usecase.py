import pytest

from src.modules.get_all_notebooks.app.get_all_notebooks_usecase import GetAllNotebooksUsecase
from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.entities.user import User
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.domain.enums.role import ROLE
from src.shared.helpers.errors.usecase_errors import ForbiddenAction

from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

class Test_GetAllNotebooksUsecase:
    
    def test_get_all_notebooks_usecase(self):
        repo = WithdrawRepositoryMock()
        usecase = GetAllNotebooksUsecase(repo=repo)
        requester_user = User(
            ra=None,
            name="Rony Rustico",
            email="rony@maua.br",
            role=ROLE.EMPLOYEE
        )
        notebooks = usecase(user=requester_user)
        assert len(notebooks) == 4
        assert type(notebooks) == list
        assert type(notebooks[0]) == tuple
        assert type(notebooks[0][0]) == Notebook
        assert type(notebooks[1][1]) == list
        assert type(notebooks[1][1][0]) == Withdraw
        
    def test_get_all_notebooks_usecase_forbidden(self):
        repo = WithdrawRepositoryMock()
        usecase = GetAllNotebooksUsecase(repo=repo)
        requester_user = User(
            ra="22011020",
            name="Luigi Aluno",
            email="22.01102-0@maua.br",
            role=ROLE.STUDENT
        )
        with pytest.raises(ForbiddenAction):
            usecase(user=requester_user)