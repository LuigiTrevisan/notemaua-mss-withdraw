import boto3

from src.shared.infra.repositories.withdraw_repository_dynamo import WithdrawRepositoryDynamo
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

def setup_dynamo_table():
    print('Setting up dynamo table...')
    dynamo_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000', region_name='sa-east-1')
    tables = dynamo_client.list_tables()['TableNames']

    if not tables:
        print('Creating table...')
        dynamo_client.create_table(
            TableName="notemaua_mss_withdraw-table",
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'SK',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'SK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI1-PK',
                    'AttributeType': 'S'
                }
            ],
            BillingMode='PAY_PER_REQUEST',
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'GSI1',
                    'KeySchema': [
                        {
                            'AttributeName': 'GSI1-PK',
                            'KeyType': 'HASH'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    }
                }
            ]
        )
        print('Table "notemaua_withdraw-table" created!\n')
    else:
        print('Table already exists!\n')

def load_mock_to_local_dynamo():
    repo_dynamo = WithdrawRepositoryDynamo()
    repo_mock = WithdrawRepositoryMock()

    print('Loading mock data to dynamo...')

    print('Loading withdraws...')
    count = 0
    for withdraw in repo_mock.withdraws:
        print(f'Loading withdraw {withdraw.withdraw_id}...')
        repo_dynamo.create_withdraw(num_serie=withdraw.num_serie, email=withdraw.email)
        count += 1
        print(withdraw)
    print(f'{count} withdraws loaded!\n')
    count = 0
    for notebook in repo_mock.notebooks:
        print(f'Loading notebook {notebook.num_serie}...')
        repo_dynamo.create_notebook(notebook=notebook)
        count += 1
        print(notebook)
    print(f'{count} notebooks loaded!\n')

    print('Done!')

if __name__ == '__main__':
    setup_dynamo_table()
    load_mock_to_local_dynamo()