import os
from aws_cdk import (
    # Duration,
    Stack, aws_cognito,
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk.aws_apigateway import RestApi, Cors, CognitoUserPoolsAuthorizer
from dotenv import load_dotenv
from .lambda_stack import LambdaStack

load_dotenv()
class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.user_pool_name = os.environ.get("USER_POOL_NAME")
        self.user_pool_id = os.environ.get("USER_POOL_ID")

        self.rest_api = RestApi(self, f"Notemaua_RestApi",
                                rest_api_name=f"Notemaua_RestApi",
                                description="This is the Notemaua RestApi",
                                default_cors_preflight_options=
                                {
                                    "allow_origins": Cors.ALL_ORIGINS,
                                    "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                                    "allow_headers": ["*"]
                                },
                                )

        api_gateway_resource = self.rest_api.root.add_resource("mss-withdraw", default_cors_preflight_options=
            {
                "allow_origins": Cors.ALL_ORIGINS,
                "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": Cors.DEFAULT_HEADERS
            }
        )
        
        ENVIRONMENT_VARIABLES = {
            "STAGE": "TEST",
            # "DYNAMO_TABLE_NAME": self.dynamo_stack.dynamo_table.table_name,
            # "DYNAMO_PARTITION_KEY": self.dynamo_stack.partition_key_name,
            # "DYNAMO_SORT_KEY": self.dynamo_stack.sort_key_name,
        }
        
        authorizer = CognitoUserPoolsAuthorizer(self, f"notemaua_cognito_stack",
                                                     cognito_user_pools=[aws_cognito.UserPool.from_user_pool_id(self, id=self.user_pool_name, user_pool_id=self.user_pool_id)]
                                                     )

        self.lambda_stack = LambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES, authorizer=authorizer)
