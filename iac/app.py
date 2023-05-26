#!/usr/bin/env python3
import os

import aws_cdk as cdk
from dotenv import load_dotenv

from adjust_layer_directory import adjust_layer_directory
from iac.iac_stack import IacStack

print("Starting the CDK")

print("Adjusting the layer directory")
adjust_layer_directory(shared_dir_name="shared", destination="lambda_layer_out_temp")
print("Finished adjusting the layer directory")

app = cdk.App()

load_dotenv()
aws_region = os.environ.get("AWS_REGION")
aws_account_id = os.environ.get("AWS_ACCOUNT_ID")

IacStack(app, "NotemauaStack", env=cdk.Environment(account=aws_account_id, region=aws_region))

app.synth()
