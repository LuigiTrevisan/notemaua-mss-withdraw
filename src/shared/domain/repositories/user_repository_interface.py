from abc import ABC, abstractmethod

class IUserRepository(ABC):

    def get_user_by_email(self, email):
        '''
        If user with email exists, return User
        else return None
        '''
        pass