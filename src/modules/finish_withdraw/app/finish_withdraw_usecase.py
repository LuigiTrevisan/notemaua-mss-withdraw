from src.shared.domain.entities.withdraw import Withdraw
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class FinishWithdrawUsecase:
    def __init__(self, repo: IWithdrawRepository):
        self.repo = repo

    def __call__(self, num_serie : str) -> Withdraw:
        withdraw = self.repo.finish_withdraw(num_serie)
        if withdraw is None:
            raise NoItemsFound("num_serie")
        return withdraw