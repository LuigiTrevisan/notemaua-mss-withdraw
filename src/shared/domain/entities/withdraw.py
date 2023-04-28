import abc
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.notebook import Notebook

class Withdraw(abc.ABC):
    num_serie: str
    email: str
    withdraw_time: int
    finish_time: int
    
    def __init__(self, num_serie: str, email: str, withdraw_time: int, finish_time: int == None):
        if not Notebook.validate_num_serie(num_serie):
            raise EntityError("num_serie")
        self.num_serie = num_serie
        
        if not User.validate_email(email):
            raise EntityError("email")
        self.email = email
        
        if not Withdraw.validate_time(withdraw_time):
            raise EntityError("withdraw_time")
        self.withdraw_time = withdraw_time
        
        if finish_time is not None:
            if not Withdraw.validate_time(finish_time):
                raise EntityError("finish_time")
            if finish_time < withdraw_time:
                raise EntityError("finish_time")
            self.finish_time = finish_time
        else:
            self.finish_time = None
        
        
        
    @staticmethod
    def validate_time(time) -> bool:
        if time == None:
            return False
        if type(time) != int:
            return False
        if time < 1641006000000:
            return False
        return True