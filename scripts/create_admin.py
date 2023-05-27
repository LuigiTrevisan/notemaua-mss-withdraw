import boto3
client = boto3.client('cognito-idp')
user_pool_id = "sa-east-1_cELM9XDrE"

if __name__ == "__main__":
    
    name = 'Lounis T'
    email = f'22.01102-0@maua.br'
    default_pass = "Maua1234!"
    ra = email[:11]

    response = client.admin_create_user( 
    UserPoolId=user_pool_id,
    Username=email, 
    TemporaryPassword=default_pass,
    UserAttributes=[{'Name': 'email', 'Value': email}, {'Name': 'name', 'Value': name.title()},{'Name': 'custom:role', 'Value': 'EMPLOYEE'}, {'Name': 'custom:ra', 'Value': ra}],
    ForceAliasCreation=True,
    MessageAction='SUPPRESS',
    )
    
    # Verify email
    response = client.admin_update_user_attributes(
            UserPoolId=user_pool_id,
            Username=email,
            UserAttributes=[
                {
                    'Name': 'email_verified',
                    'Value': 'true'
                }
            ]
        )