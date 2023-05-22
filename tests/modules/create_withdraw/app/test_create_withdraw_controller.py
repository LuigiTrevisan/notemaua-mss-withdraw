from src.modules.create_withdraw.app.create_withdraw_controller import CreateWithdrawController
from src.modules.create_withdraw.app.create_withdraw_usecase import CreateWithdrawUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock


class Test_CreateWithdrawController:
    def test_create_withdraw_controller(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={
            'num_serie':'34035',
            'email':'arthur@maua.br'
        })
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body['message'] == 'the withdraw was created'
        assert response.body['withdraw']['num_serie'] == '34035'
        assert response.body['withdraw']['email'] == 'arthur@maua.br'
        assert response.body['withdraw']['withdraw_time'] is not None
        assert response.body['withdraw']['finish_time'] is None
        
    def test_create_withdraw_controller_missing_num_serie(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'email':'arthur@maua.br'})
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field num_serie is missing'
        
    def test_create_withdraw_controller_missing_email(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':'34035'})
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field email is missing'
        
    def test_create_withdraw_controller_wrong_type_num_serie(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':34035, 'email':'arthur@maua.br'})
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field num_serie isn't in the right type.\n Received: <class 'int'>.\n Expected: str"
        
    def test_create_withdraw_controller_wrong_type_email(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':'34035', 'email':123})
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field email isn't in the right type.\n Received: <class 'int'>.\n Expected: str"
        
    def test_create_withdraw_controller_email_already_with_withdraw(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':'34035', 'email':'22.01102-0@maua.br'})
                              
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'The item alredy exists for this email'
        
    def test_create_withdraw_controller_email_not_found(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':'34035', 'email':'10.01483-0@maua.br'})	
        
        response = controller(request)
        assert response.status_code == 404
        assert response.body == 'No items found for email'
        
    def test_create_withdraw_controller_notebook_already_active(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':'34036', 'email':'arthur@maua.br'})
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'The item alredy exists for this num_serie'
        
    def test_create_withdraw_controller_notebook_not_found(self):
        repo = WithdrawRepositoryMock()
        usecase = CreateWithdrawUsecase(repo)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':'34034', 'email':'arthur@maua.br'})
        
        response = controller(request)
        assert response.status_code == 404
        assert response.body == 'No items found for num_serie'