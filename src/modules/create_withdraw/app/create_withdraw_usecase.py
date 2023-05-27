from datetime import datetime
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound


class CreateWithdrawUsecase:
    def __init__(self, repo_withdraw: IWithdrawRepository, repo_user: IUserRepository):
        self.repo_withdraw = repo_withdraw
        self.repo_user = repo_user
    
    def __call__(self, num_serie : str, email : str) -> Withdraw:
        notebook = self.repo_withdraw.get_notebook(num_serie)
        if notebook is None:
            raise NoItemsFound('num_serie')
        
        if notebook.isActive:
            raise DuplicatedItem('num_serie')
        
        user = self.repo_user.get_user_by_email(email)
        if user is None:
            raise NoItemsFound('email')
        
        
        withdraws = self.repo_withdraw.get_withdraws_by_email(email)
        for withdraw in withdraws:
            if withdraw.finish_time is None:
                raise DuplicatedItem('email')
            
        withdraw = Withdraw(len(withdraws), num_serie, email, int(datetime.now().timestamp() * 1000))
        
        return self.repo_withdraw.create_withdraw(withdraw)