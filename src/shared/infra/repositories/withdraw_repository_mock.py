from datetime import datetime
from typing import List
from src.shared.domain.enums.role import ROLE
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.domain.entities.user import User
from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.entities.withdraw import Withdraw

class WithdrawRepositoryMock(IWithdrawRepository):
    notebooks: List[Notebook]
    withdraws: List[Withdraw]
    
    def __init__(self):
        self.notebooks = [
            Notebook(num_serie="34035", isActive=False),
            Notebook(num_serie="34036", isActive=True),
            Notebook(num_serie="34037", isActive=False),
            Notebook(num_serie="34038", isActive=True),
        ]
        
        self.withdraws = [
            Withdraw(withdraw_id=1, num_serie="34036", email="22.01102-0@maua.br", withdraw_time=1682610909494),
            Withdraw(withdraw_id=2, num_serie="34038", email="22.01049-0@maua.br", withdraw_time=1682611052153),
            Withdraw(withdraw_id=3, num_serie="34037", email="22.01589-2@maua.br", withdraw_time=1682604600000, finish_time=1682611200000),
            Withdraw(withdraw_id=4, num_serie="34038", email="22.01102-0@maua.br", withdraw_time=1682611052153, finish_time=1682629052000),
    ]
        
    def get_withdraws_by_email(self, email):
        withdraws = []
        for withdraw in self.withdraws:
            if withdraw.email == email:
                withdraws.append(withdraw)
        return withdraws
    
    def get_withdraws_by_num_serie(self, num_serie):
        withdraws = []
        for withdraw in self.withdraws:
            if withdraw.num_serie == num_serie:
                withdraws.append(withdraw)
        return withdraws
    
    def get_notebook(self, num_serie):
        for notebook in self.notebooks:
            if notebook.num_serie == num_serie:
                return notebook
        return None
    
    def create_withdraw(self, withdraw):
        self.withdraws.append(withdraw)
        for notebook in self.notebooks:
            if notebook.num_serie == withdraw.num_serie:
                notebook.isActive = True
        return withdraw
                
    def finish_withdraw(self, withdraw):
        for w in self.withdraws:
            if w.num_serie == withdraw.num_serie and w.finish_time == None:
                finish_time = int(datetime.now().timestamp() * 1000)
                w.finish_time = finish_time
                for notebook in self.notebooks:
                    if notebook.num_serie == withdraw.num_serie:
                        notebook.isActive = False
                return w
        return None
    
    def get_all_notebooks(self):
        notebooks = []
        for notebook in self.notebooks:
            withdraws = self.get_withdraws_by_num_serie(notebook.num_serie)
            notebooks.append((notebook, withdraws))
        return notebooks
    
    def create_notebook(self, notebook):
        for notebook_ in self.notebooks:
            if notebook_.num_serie == notebook.num_serie:
                return None
        self.notebooks.append(notebook)
        return notebook
    
    def get_active_withdraw(self, num_serie):
        for withdraw in self.withdraws:
            if withdraw.num_serie == num_serie and withdraw.finish_time == None:
                return withdraw
        return None