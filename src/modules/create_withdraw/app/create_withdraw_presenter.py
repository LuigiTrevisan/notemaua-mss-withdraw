from .create_withdraw_controller import CreateWithdrawController
from .create_withdraw_usecase import CreateWithdrawUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo_withdraw = Environments.get_withdraw_repo()()
repo_user=Environments.get_user_repo()()
usecase = CreateWithdrawUsecase(repo_withdraw=repo_withdraw, repo_user=repo_user)
controller = CreateWithdrawController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return httpResponse.toDict()