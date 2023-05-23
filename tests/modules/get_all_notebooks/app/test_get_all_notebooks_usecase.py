import pytest

from src.modules.get_all_notebooks.app.get_all_notebooks_usecase import GetAllNotebooksUsecase
from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.entities.withdraw import Withdraw

from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

class Test_GetAllNotebooksUsecase:
    
    def test_get_all_notebooks_usecase(self):
        repo = WithdrawRepositoryMock()
        usecase = GetAllNotebooksUsecase(repo=repo)
        notebooks = usecase()
        assert len(notebooks) == 4
        assert type(notebooks) == list
        assert type(notebooks[0]) == tuple
        assert type(notebooks[0][0]) == Notebook
        assert type(notebooks[1][1]) == list
        assert type(notebooks[1][1][0]) == Withdraw