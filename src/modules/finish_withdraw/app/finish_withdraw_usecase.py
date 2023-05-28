from src.shared.domain.entities.user import User
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.domain.enums.role import ROLE
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound

class FinishWithdrawUsecase:
    def __init__(self, repo: IWithdrawRepository):
        self.repo = repo

    def __call__(self, num_serie : str, user: User) -> Withdraw:
        
        if user.role not in [ROLE.EMPLOYEE, ROLE.ADMIN]:
            raise ForbiddenAction("user")
        
        withdraw = self.repo.get_active_withdraw(num_serie)
        if withdraw is None:
            raise NoItemsFound("num_serie")
        
        return self.repo.finish_withdraw(withdraw)