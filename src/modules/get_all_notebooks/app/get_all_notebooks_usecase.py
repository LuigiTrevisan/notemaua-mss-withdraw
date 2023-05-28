from typing import List, Tuple

from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.entities.user import User
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.domain.enums.role import ROLE
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction

class GetAllNotebooksUsecase:
    
    def __init__(self, repo: IWithdrawRepository):
        self.repo = repo
        
    def __call__(self, user: User) -> List[Tuple[Notebook, List[Withdraw]]]:
        
        if user.role not in [ROLE.ADMIN, ROLE.EMPLOYEE]:
            raise ForbiddenAction("user")
        
        notebooks = self.repo.get_all_notebooks()
        active_withdraws = []
        for notebook, withdraws in notebooks:
            if notebook.isActive == True:
                for withdraw in withdraws:
                    if withdraw.finish_time == None:
                        active_withdraws.append((notebook, [withdraw]))
            else:
                active_withdraws.append((notebook, None))
        return active_withdraws