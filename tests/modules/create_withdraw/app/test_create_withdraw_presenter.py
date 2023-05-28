from datetime import datetime
import json
from src.modules.create_withdraw.app.create_withdraw_presenter import lambda_handler

class Test_CreateWithdrawPresenter:
    def test_create_withdraw_presenter(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "1"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "claims" : {
                        "sub" : "e2d865b1-e0c3-427e-866a-efa4e72e20f9",
                        "name" : "Arthur Trevisan",
                        "email" : "arthur@maua.br",
                        "custom:role" : "EMPLOYEE",
                        "custom:ra" : None
                    }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": '{"num_serie":"34035"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None,
        }
        
        response = lambda_handler(event, None)
        withdraw_time = int(datetime.now().timestamp() * 1000)
        expected = {'withdraw': {'num_serie': '34035', 'email': 'arthur@maua.br', 'withdraw_time': withdraw_time, 'finish_time': None}, 'message': 'the withdraw was created'}
        
        assert response["statusCode"] == 201
        assert json.loads(response["body"]) == expected