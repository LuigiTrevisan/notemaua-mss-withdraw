import pytest
from src.shared.domain.enums.role import ROLE

from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

from src.shared.helpers.external_interfaces.http_models import HttpRequest

from src.modules.get_all_notebooks.app.get_all_notebooks_controller import GetAllNotebooksController
from src.modules.get_all_notebooks.app.get_all_notebooks_usecase import GetAllNotebooksUsecase

class Test_GetAllNotebooksController:
    def test_get_all_notebooks_controller(self):
        repo = WithdrawRepositoryMock()
        usecase = GetAllNotebooksUsecase(repo=repo)
        controller = GetAllNotebooksController(usecase=usecase)
        
        request = HttpRequest(body={'requester_user' : {
                "sub" : "123456789",
                "email" : "rony@maua.br",
                "name" : "Rony Rustico",
                "custom:ra" : None,
                "custom:role" : "EMPLOYEE"
            }})
        
        response = controller(request=request)
        
        assert response.status_code == 200
        assert type(response.body['notebooks']) == list
        assert response.body['message'] == 'Notebooks found successfully!'
        
    def test_get_all_notebooks_controller_missing_user(self):
        repo = WithdrawRepositoryMock()
        usecase = GetAllNotebooksUsecase(repo=repo)
        controller = GetAllNotebooksController(usecase=usecase)
        
        request = HttpRequest(body={})
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'
        
    def test_get_all_notebooks_controller_forbidden(self):
        repo = WithdrawRepositoryMock()
        usecase = GetAllNotebooksUsecase(repo=repo)
        controller = GetAllNotebooksController(usecase=usecase)
        
        request = HttpRequest(body={'requester_user' : {
                "sub" : "123456789",
                "email" : "22.01102-0@maua.br",
                "name" : "Luigi Aluno",
                "custom:ra" : "22011020",
                "custom:role" : "STUDENT"
            }})
        
        response = controller(request=request)
        
        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this user'