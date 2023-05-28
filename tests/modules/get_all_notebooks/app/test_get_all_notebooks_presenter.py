import json
import pytest

from src.modules.get_all_notebooks.app.get_all_notebooks_presenter import lambda_handler

class Test_GetAllNotebooksPresenter:
    def test_get_all_notebooks_presenter(self):
        event = {
            "httpMethod": "GET",
            "path": "/notebooks",
            "queryStringParameters": {},
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
            "headers": {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "CloudFront-Forwarded-Proto": "https",
                "CloudFront-Is-Desktop-Viewer": "true",
                "CloudFront-Is-Mobile-Viewer": "false",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Is-Tablet-Viewer": "false",
                "CloudFront-Viewer-Country": "US",
                "content-type": "application/json",
                "Host": "localhost:3000",
                "origin": "http://localhost:3000",
                "Referer": "http://localhost:3000/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "User-Agent": "PostmanRuntime/7.26.8",
                "Via": "2.0 4a6c4b9e2e1f2e3f7f8a6f1e9c0b3f0c.cloudfront.net (CloudFront)",
                "X-Amz-Cf-Id": "D5P5j5X8U4Q6M8W4J1x2Q8p2a0a8n3d4I5u7I4o4e7n3e9d7J0e0Q==",
                "X-Amzn-Trace-Id": "Root=1-60c0b3f4-2c4b9e2e1f2e3f7f8a6f1e9c",
                "X-Forwarded-For": "",
                "X-Forwarded-Port": "443",
                "X-Forwarded-Proto": "https"
            },
            "body": {},
            "isBase64Encoded": False
        }
        
        response = lambda_handler(event, None)
        expected = {
            'notebooks':[
                {
                    'notebook':{
                        'num_serie':'34035',
                        'isActive':False
                    },
                    'withdraws':[]
                },
                {
                    'notebook':{
                        'num_serie':'34036',
                        'isActive':True
                    },
                    'withdraws':[
                        {
                        'withdraw_id':1,
                        'num_serie':'34036',
                        'email':'22.01102-0@maua.br',
                        'withdraw_time':1682610909494,
                        'finish_time':None
                        }
                    ]
                },
                {
                    'notebook':{
                        'num_serie':'34037',
                        'isActive':False
                    },
                    'withdraws':[]
                },
                {
                    'notebook':{
                        'num_serie':'34038',
                        'isActive':True
                    },
                    'withdraws':[
                        {
                        'withdraw_id':2,
                        'num_serie':'34038',
                        'email':'22.01049-0@maua.br',
                        'withdraw_time':1682611052153,
                        'finish_time':None
                        }
                    ]
                }
            ],
            'message':'Notebooks found successfully!'
        }
        assert response["statusCode"] == 200
        assert json.loads(response["body"]) == expected