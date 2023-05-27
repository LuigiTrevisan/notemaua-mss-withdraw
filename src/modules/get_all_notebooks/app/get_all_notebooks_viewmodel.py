from typing import List

from src.shared.domain.entities.user import User
from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.entities.withdraw import Withdraw
from src.shared.domain.enums.role import ROLE

class UserViewmodel:
    ra: str
    name: str
    email: str
    role: ROLE
    
    def __init__(self, user: User):
        self.ra = user.ra
        self.name = user.name
        self.email = user.email
        self.role = user.role
        
    def to_dict(self) -> dict:
        return {
            "ra": self.ra,
            "name": self.name,
            "email": self.email,
            "role": self.role
        }
        
class NotebookViewmodel:
    num_serie: str
    isActive: bool
    
    def __init__(self, notebook: Notebook):
        self.num_serie = notebook.num_serie
        self.isActive = notebook.isActive
        
    def to_dict(self) -> dict:
        return {
            "num_serie": self.num_serie,
            "isActive": self.isActive
        }
        
class WithdrawViewmodel:
    withdraw_id: int
    num_serie: str
    email: str
    withdraw_time: int
    finish_time: int = None
    
    def __init__(self, withdraw: Withdraw):
        if withdraw is not None:
            self.withdraw_id = withdraw.withdraw_id
            self.num_serie = withdraw.num_serie
            self.email = withdraw.email
            self.withdraw_time = withdraw.withdraw_time
            self.finish_time = withdraw.finish_time
        else:
            self.withdraw_id = None
            self.num_serie = None
            self.email = None
            self.withdraw_time = None
            self.finish_time = None
    
    def to_dict(self) -> dict:
        return {
            "withdraw_id": self.withdraw_id,
            "num_serie": self.num_serie,
            "email": self.email,
            "withdraw_time": self.withdraw_time,
            "finish_time": self.finish_time
        }
        
        
class GetAllNotebooksViewmodel:
    notebooks: List[tuple[Notebook, List[Withdraw]]]
    
    def __init__(self, notebooks: List[tuple[Notebook, List[Withdraw]]]):
        self.notebooks = notebooks
            
    def to_dict(self) -> dict:
        return {
            "notebooks" : [
                {
                    "notebook": NotebookViewmodel(notebook).to_dict(),
                    "withdraws": [WithdrawViewmodel(withdraw).to_dict() for withdraw in withdraws] if withdraws != None else None} for notebook, withdraws in self.notebooks
            ],
            "message": "Notebooks found successfully!"
        }
        
        
