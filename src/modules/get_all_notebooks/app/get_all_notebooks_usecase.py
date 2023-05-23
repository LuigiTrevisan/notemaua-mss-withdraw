from typing import List

from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository

class GetAllNotebooksUsecase:
    
    def __init__(self, repo: IWithdrawRepository):
        self.repo = repo
        
    def __call__(self) -> List[tuple[Notebook, List[Withdraw]]]:
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