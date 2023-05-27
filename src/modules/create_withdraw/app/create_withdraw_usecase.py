from datetime import datetime
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound


class CreateWithdrawUsecase:
    def __init__(self, repo: IWithdrawRepository):
        self.repo = repo
    
    def __call__(self, num_serie : str, email : str) -> Withdraw:
        notebook = self.repo.get_notebook(num_serie)
        if notebook is None:
            raise NoItemsFound('num_serie')
        
        if notebook.isActive:
            raise DuplicatedItem('num_serie')
        
        user = self.repo.get_user_by_email(email)
        if user is None:
            raise NoItemsFound('email')
        
        
        withdraws = self.repo.get_withdraws_by_email(email)
        for withdraw in withdraws:
            if withdraw.finish_time is None:
                raise DuplicatedItem('email')
            
        withdraw = Withdraw(len(withdraws), num_serie, email, int(datetime.now().timestamp() * 1000))
        
        return self.repo.create_withdraw(withdraw)