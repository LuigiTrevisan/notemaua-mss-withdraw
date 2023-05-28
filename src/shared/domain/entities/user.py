import abc
import re
from src.shared.domain.enums.role import ROLE
from src.shared.helpers.errors.domain_errors import EntityError

class User(abc.ABC):
    ra: str
    name: str
    email: str
    role: ROLE
    MIN_NAME_LENGTH = 3
    MIN_PASSWORD_LENGTH = 8
    RA_LENGTH = 8
    
    def __init__(self, ra: str, name: str, email: str, role: ROLE):
        
        if not User.validate_ra(ra, role):
            raise EntityError("ra")
        self.ra = ra
                
        if not User.validate_name(name):
            raise EntityError("name")
        self.name = name
        
        if not User.validate_email(email):
            raise EntityError("email")
        self.email = email
        
        if not User.validate_role(role):
            raise EntityError("role")
        self.role = role
        
    @staticmethod
    def validate_ra(ra, role) -> bool:
        if role is ROLE.STUDENT:
            if ra is None:
                return False
            if type(ra) != str:
                return False
            if not ra.isdecimal():
                return False
            if len(ra) != User.RA_LENGTH:
                return False
        else:
            if ra is not None:
                return False
        
        return True    
    
    @staticmethod
    def validate_name(name) -> bool:
        if name == None:
            return False
        if type(name) != str:
            return False
        if len(name) < User.MIN_NAME_LENGTH:
            return False
        
        return True
    
    @staticmethod
    def validate_email(email) -> bool:
        if email == None:
            return False
        if type(email) != str:
            return False
        if email[-8:] != "@maua.br":
            return False
        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return bool(re.fullmatch(regex, email))
    
    @staticmethod
    def validate_role(role) -> bool:
        if role == None:
            return False
        if type(role) != ROLE:
            return False
        if role.value not in [r.value for r in ROLE]:
            return False
        
        return True
    
    def __eq__(self, other):
        return self.ra == other.ra and self.name == other.name and self.email == other.email and self.role == other.role