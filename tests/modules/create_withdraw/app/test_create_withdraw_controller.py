from src.modules.create_withdraw.app.create_withdraw_controller import CreateWithdrawController
from src.modules.create_withdraw.app.create_withdraw_usecase import CreateWithdrawUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock


class Test_CreateWithdrawController:
    def test_create_withdraw_controller(self):
        repo_withdraw = WithdrawRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateWithdrawUsecase(repo_withdraw, repo_user)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={
            'num_serie':'34035',
            'requester_user' : {
                "sub" : "123456789",
                "email" : repo_user.users[6].email,
                "name" : repo_user.users[6].name,
                "custom:ra" : repo_user.users[6].ra,
                "custom:role" : repo_user.users[6].role.value
            }
        })
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body['message'] == 'the withdraw was created'
        assert response.body['withdraw']['num_serie'] == '34035'
        assert response.body['withdraw']['email'] == repo_user.users[6].email
        assert response.body['withdraw']['withdraw_time'] is not None
        assert response.body['withdraw']['finish_time'] is None
        
    def test_create_withdraw_controller_missing_num_serie(self):
        repo_withdraw = WithdrawRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateWithdrawUsecase(repo_withdraw, repo_user)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'requester_user' : {
                "sub" : "123456789",
                "email" : repo_user.users[6].email,
                "name" : repo_user.users[6].name,
                "custom:ra" : repo_user.users[6].ra,
                "custom:role" : repo_user.users[6].role.value
            }})
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field num_serie is missing'
        
    def test_create_withdraw_controller_wrong_type_num_serie(self):
        repo_withdraw = WithdrawRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateWithdrawUsecase(repo_withdraw, repo_user)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':34035, 'requester_user' : {
                "sub" : "123456789",
                "email" : repo_user.users[6].email,
                "name" : repo_user.users[6].name,
                "custom:ra" : repo_user.users[6].ra,
                "custom:role" : repo_user.users[6].role.value
            }})
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field num_serie isn't in the right type.\n Received: <class 'int'>.\n Expected: str"
        
    def test_create_withdraw_controller_email_already_with_withdraw(self):
        repo_withdraw = WithdrawRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateWithdrawUsecase(repo_withdraw, repo_user)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':'34035', 'requester_user' : {
                "sub" : "123456789",
                "email" : repo_user.users[0].email,
                "name" : repo_user.users[0].name,
                "custom:ra" : repo_user.users[0].ra,
                "custom:role" : repo_user.users[0].role.value
            }})
                              
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'This user already has an active notebook.'
        
    def test_create_withdraw_controller_notebook_already_active(self):
        repo_withdraw = WithdrawRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateWithdrawUsecase(repo_withdraw, repo_user)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':'34036', 'requester_user' : {
                "sub" : "123456789",
                "email" : repo_user.users[6].email,
                "name" : repo_user.users[6].name,
                "custom:ra" : repo_user.users[6].ra,
                "custom:role" : repo_user.users[6].role.value
            }})
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'This notebook is already active.'
        
    def test_create_withdraw_controller_notebook_not_found(self):
        repo_withdraw = WithdrawRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateWithdrawUsecase(repo_withdraw, repo_user)
        controller = CreateWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':'34034', 'requester_user' : {
                "sub" : "123456789",
                "email" : repo_user.users[6].email,
                "name" : repo_user.users[6].name,
                "custom:ra" : repo_user.users[6].ra,
                "custom:role" : repo_user.users[6].role.value
            }})
        
        response = controller(request)
        assert response.status_code == 404
        assert response.body == 'No items found for num_serie'