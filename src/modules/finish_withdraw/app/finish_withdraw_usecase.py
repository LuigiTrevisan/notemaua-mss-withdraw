from src.shared.domain.entities.withdraw import Withdraw
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class FinishWithdrawUsecase:
    def __init__(self, repo: IWithdrawRepository):
        self.repo = repo

    def __call__(self, num_serie : str) -> Withdraw:
        withdraws = self.repo.get_withdraws_by_num_serie(num_serie)
        contador = 0
        for withdraw in withdraws:
            if withdraw.finish_time == None:
                contador +=1
        if contador == 0:
            raise NoItemsFound('num_serie')
        return self.repo.finish_withdraw(num_serie)