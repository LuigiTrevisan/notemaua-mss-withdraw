from abc import ABC, abstractmethod

class IWithdrawRepository(ABC):
    
    def get_user_by_email(self, email):
        '''
        If user with email exists, return User
        else return None
        '''
        pass
    
    def get_notebook(self, num_serie):
        '''
        If notebook with num_serie exists, return Notebook
        else return None
        '''
        pass
    
    def set_notebook_is_active(self, num_serie, is_active):
        '''
        If notebook with num_serie exists, set Notebook.isActive to is_active
        '''
        pass
    
    def get_all_notebooks(self):
        '''
        Return all withdraws
        '''
        pass
    
    def get_withdraws_by_num_serie(self, num_serie):
        '''
        If withdraw with num_serie exists, return Withdraw
        else return None
        '''
        pass
    
    def get_withdraws_by_email(self, email):
        '''
        If withdraw with email exists, return Withdraw
        else return None
        '''
        pass
    
    def create_withdraw(self, num_serie, email):
        '''
        If notebook exists and isActive == False and user exists, create withdraw and return it
        set Notebook.isActive to True
        set withdraw_time to current time
        '''
        pass
    
    def finish_withdraw(self, num_serie):
        '''
        If withdraw with num_serie exists, finish withdraw and return it
        set Notebook.isActive to False
        set Withdraw.finish_time to current time
        get user and notebook and send them to withdraw history
        '''
        pass