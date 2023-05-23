import pytest

from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

from src.shared.helpers.external_interfaces.http_models import HttpRequest

from src.modules.get_all_notebooks.app.get_all_notebooks_controller import GetAllNotebooksController
from src.modules.get_all_notebooks.app.get_all_notebooks_usecase import GetAllNotebooksUsecase

class Test_GetAllNotebooksController:
    def test_get_all_notebooks_controller(self):
        repo = WithdrawRepositoryMock()
        usecase = GetAllNotebooksUsecase(repo=repo)
        controller = GetAllNotebooksController(usecase=usecase)
        
        request = HttpRequest()
        
        response = controller(request=request)
        
        assert response.status_code == 200
        assert type(response.body['notebooks']) == list
        assert response.body['message'] == 'Notebooks found successfully!'