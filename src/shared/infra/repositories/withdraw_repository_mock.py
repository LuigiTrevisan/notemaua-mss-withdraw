from datetime import datetime
from typing import List
from src.shared.domain.enums.role import ROLE
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.domain.entities.user import User
from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.entities.withdraw import Withdraw

class WithdrawRepositoryMock(IWithdrawRepository):
    users: List[User]
    notebooks: List[Notebook]
    withdraws: List[Withdraw]
    
    def __init__(self):
        self.users = [
            User(ra="22011020", name="Luigi Television", email="22.01102-0@maua.br", role=ROLE.STUDENT),
            User(ra="22010490", name="Vitor Negro", email="22.01049-0@maua.br", role=ROLE.STUDENT),
            User(ra="22015892", name="Gabriel Milanesa", email="22.01589-2@maua.br", role=ROLE.STUDENT),
            User(ra=None, name="Rony Rustico", email="rony@maua.br", role=ROLE.EMPLOYEE),
            User(ra=None, name="Arthur Television", email="arthur@maua.br", role=ROLE.EMPLOYEE),
            User(ra=None, name="Pana Aula", email="pana@maua.br", role=ROLE.ADMIN),
        ]
        
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
    
    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def create_withdraw(self, num_serie, email):
        withdraw_time = int(datetime.now().timestamp() * 1000)
        withdraw_id = len(self.withdraws) + 1
        withdraw = Withdraw(withdraw_id=withdraw_id, email=email, num_serie=num_serie, withdraw_time=withdraw_time, finish_time=None)
        self.withdraws.append(withdraw)
        for notebook in self.notebooks:
            if notebook.num_serie == num_serie:
                notebook.isActive = True
        return withdraw
                
    def finish_withdraw(self, num_serie):
        for withdraw in self.withdraws:
            if withdraw.num_serie == num_serie and withdraw.finish_time == None:
                finish_time = int(datetime.now().timestamp() * 1000)
                withdraw.finish_time = finish_time
                for notebook in self.notebooks:
                    if notebook.num_serie == num_serie:
                        notebook.isActive = False
                return withdraw
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