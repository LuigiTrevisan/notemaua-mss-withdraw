from datetime import datetime
from src.modules.create_withdraw.app.create_withdraw_usecase import CreateWithdrawUsecase
from src.modules.create_withdraw.app.create_withdraw_viewmodel import CreateWithdrawViewmodel
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock


class Test_CreateWithdrawViewmodel:
    def test_create_withdraw_viewmodel(self):
        repo_withdraw = WithdrawRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateWithdrawUsecase(repo_withdraw=repo_withdraw, repo_user = repo_user)
        withdraw = usecase(num_serie='34035', email="arthur@maua.br")
        viewmodel = CreateWithdrawViewmodel(withdraw=withdraw).to_dict()
        expected = {
                    'withdraw':{
                        'num_serie':'34035',
                        'email':'arthur@maua.br',
                        'withdraw_time':int(datetime.now().timestamp() * 1000),
                        'finish_time':None
                    },
                    'message':'the withdraw was created'
                    }
        
        assert viewmodel == expected