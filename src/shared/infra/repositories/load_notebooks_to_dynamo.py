from src.shared.domain.entities.notebook import Notebook
from src.shared.infra.repositories.withdraw_repository_dynamo import WithdrawRepositoryDynamo


notebooks = []
gabinete1 = range(34871, 34895 + 1)
gabinete2 = range(34896, 34920 + 1)
gabinete3 = range(34541, 34570 + 1)
gabinete4 = range(34701, 34725 + 1)
gabinete5 = range(34726, 34750 + 1)
gabinete6 = range(34751, 34775 + 1)
gabinete7 = range(34776, 34800 + 1)
gabinete8 = range(34801, 34820 + 1)
for gabinete in [gabinete1, gabinete2, gabinete3, gabinete4, gabinete5, gabinete6, gabinete7, gabinete8]:
    for num_serie in gabinete:
        notebooks.append(Notebook(num_serie=str(num_serie), isActive=False))

repo_dynamo = WithdrawRepositoryDynamo()
print(f"Loading {len(notebooks)} notebooks to DynamoDB...")
count = 1
for notebook in notebooks:
    print(f"Loading notebook {count}...")
    repo_dynamo.create_notebook(notebook)
    count += 1
print("Done!")
