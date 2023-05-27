import abc
from src.shared.helpers.errors.domain_errors import EntityError

class Notebook(abc.ABC):
    num_serie: str
    isActive: bool
    NUM_SERIE_LENGTH = 5
    
    def __init__(self, num_serie: str, isActive: bool == False):
        if not Notebook.validate_num_serie(num_serie):
            raise EntityError("num_serie")
        self.num_serie = num_serie
        
        if isActive == None:
            isActive = False
        if type(isActive) is not bool:
            raise EntityError("isActive")
        self.isActive = isActive
        
    @staticmethod
    def validate_num_serie(num_serie) -> bool:
        if num_serie is None:
            return False
        if type(num_serie) is not str:
            return False
        if not num_serie.isdecimal():
            return False
        if len(num_serie) != Notebook.NUM_SERIE_LENGTH:
            return False
        
        return True
    
    def __repr__(self):
        return f"Notebook(num_serie={self.num_serie}, isActive={self.isActive})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__