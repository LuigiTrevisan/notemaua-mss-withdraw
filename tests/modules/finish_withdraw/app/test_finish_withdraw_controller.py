from src.modules.finish_withdraw.app.finish_withdraw_controller import FinishWithdrawController
from src.modules.finish_withdraw.app.finish_withdraw_usecase import FinishWithdrawUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

class Test_FinishWithdrawController:
    def test_finish_withdraw_controller(self):
        repo = WithdrawRepositoryMock()
        usecase = FinishWithdrawUsecase(repo)
        controller = FinishWithdrawController(usecase)
        request = HttpRequest(body={'num_serie':'34036', 'requester_user' : {
                "sub" : "123456789",
                "email" : "rony@maua.br",
                "name" : "Rony Rustico",
                "custom:ra" : None,
                "custom:role" : "EMPLOYEE"
            }})

        response = controller(request)
        assert response.status_code == 200
        assert response.body['message'] == 'the withdraw has been finished'
        assert response.body['withdraw']['num_serie'] == '34036'
        assert response.body['withdraw']['withdraw_time'] is not None
        assert response.body['withdraw']['finish_time'] is not None