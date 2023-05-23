import pytest

from src.modules.get_all_notebooks.app.get_all_notebooks_usecase import GetAllNotebooksUsecase

from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

class Test_GetAllNotebooksUsecase:
    
    def test_get_all_notebooks_usecase(self):
        repo = WithdrawRepositoryMock()
        usecase = GetAllNotebooksUsecase(repo=repo)
        notebooks = usecase()
        assert True