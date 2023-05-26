from datetime import datetime
from src.modules.finish_withdraw.app.finish_withdraw_usecase import FinishWithdrawUsecase
from src.modules.finish_withdraw.app.finish_withdraw_viewmodel import FinishWithdrawViewmodel
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

class Test_FinishWithdrawViewmodel:
    def test_finish_withdraw_viewmodel(self):
        repo = WithdrawRepositoryMock()
        usecase = FinishWithdrawUsecase(repo=repo)
        withdraw = usecase(num_serie='34036')
        viewmodel = FinishWithdrawViewmodel(withdraw).to_dict()
        expected = {
                    'withdraw':{
                        'num_serie':'34036',
                        'email':'22.01102-0@maua.br',
                        'withdraw_time':repo.withdraws[0].withdraw_time,
                        'finish_time':repo.withdraws[0].finish_time
                    },
                    'message':'the withdraw has been finished'
                    }

        assert viewmodel == expected