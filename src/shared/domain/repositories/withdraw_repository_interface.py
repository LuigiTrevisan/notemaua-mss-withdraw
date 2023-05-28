from abc import ABC, abstractmethod

class IWithdrawRepository(ABC):
    
    def get_notebook(self, num_serie):
        '''
        If notebook with num_serie exists, return Notebook
        else return None
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
    
    def create_withdraw(self, withdraw):
        '''
        If notebook exists and isActive == False and user exists, create withdraw and return it
        set withdraw_time to current time
        set Notebook.isActive to True
        '''
        pass
    
    def create_notebook(self, notebook):
        '''
        If notebook with num_serie exists, return None
        else create notebook and return it
        '''
        pass
    
    def finish_withdraw(self, withdraw):
        '''
        If withdraw with num_serie exists, finish withdraw and return it
        set Notebook.isActive to False
        set Withdraw.finish_time to current time
        get user and notebook and send them to withdraw history
        '''
        pass
    
    def get_active_withdraw(self, num_serie):
        '''
        If withdraw with num_serie exists and has no finish time, return withdraw
        else return None
        '''
        pass