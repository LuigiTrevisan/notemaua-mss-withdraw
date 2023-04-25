import abc

from src.shared.helpers.errors.domain_errors import EntityError

class Notebook(abc.ABC):
    serial: str
    isActive: bool
    SERIAL_LENGTH = 5
    
    def __init__(self, serial: str, isActive: bool == False):
        if not Notebook.validate_serial(serial):
            raise EntityError("serial")
        self.serial = serial
        
        if isActive == None:
            isActive = False
        if type(isActive) is not bool:
            raise EntityError("isActive")
        self.isActive = isActive
        
    @staticmethod
    def validate_serial(serial) -> bool:
        if serial is None:
            return False
        if type(serial) is not str:
            return False
        if not serial.isdecimal():
            return False
        if len(serial) != Notebook.SERIAL_LENGTH:
            return False
        
        return True
    