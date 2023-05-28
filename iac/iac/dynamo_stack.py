import os
from aws_cdk import (
    CfnOutput,
    aws_dynamodb,
    RemovalPolicy
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration

class DynamoStack(Construct):
    
    def __init__(self, scope: Construct) -> None:
        super().__init__(scope, "NotemauaDynamoStack")
        
        self.dynamo_table = aws_dynamodb.Table(
            self, "Notemaua_Dynamo_Table",
            partition_key=aws_dynamodb.Attribute(
                name="PK",
                type=aws_dynamodb.AttributeType.STRING
            ),
            sort_key=aws_dynamodb.Attribute(
                name="SK",
                type=aws_dynamodb.AttributeType.STRING
            ),
            billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY
        )
        
        self.dynamo_table.add_global_secondary_index(
            partition_key=aws_dynamodb.Attribute(
                name="GSI1-PK",
                type=aws_dynamodb.AttributeType.STRING
            ),
            index_name="GSI1"
        )