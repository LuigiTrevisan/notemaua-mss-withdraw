from src.modules.create_withdraw.app.create_withdraw_controller import CreateWithdrawController
from src.modules.create_withdraw.app.create_withdraw_usecase import CreateWithdrawUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo = Environments.get_withdraw_repo()()
usecase = CreateWithdrawUsecase(repo=repo)
controller = CreateWithdrawController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return httpResponse.toDict()