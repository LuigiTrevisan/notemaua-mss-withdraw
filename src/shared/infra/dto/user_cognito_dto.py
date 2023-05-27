from src.shared.domain.entities.user import User
from src.shared.domain.enums.role import ROLE


class UserCognitoDTO:
    name: str
    email: str
    ra: str
    role: ROLE
    
    def __init__(self, name: str, email: str, ra: str, role: ROLE):
        self.name = name
        self.email = email
        self.ra = ra
        self.role = role
        
    @staticmethod
    def from_cognito(cognito_user: dict):
        
        custom_prefix = "custom:"
        user_data = {user_attribute["Name"].removeprefix(custom_prefix): user_attribute["Value"] for user_attribute in cognito_user["Attributes"]}
        ra = user_data["ra"].replace("-", "")
        ra = ra.replace(".", "")
        return UserCognitoDTO(
            name=user_data["name"],
            email=user_data["email"],
            ra=ra,
            role=ROLE(user_data["role"])
        )
        
    def to_entity(self):
        return User(
            ra=self.ra,
            name=self.name,
            email=self.email,
            role=self.role
        )
        
    def __eq__(self, other):
        return self.name == other.name and self.email == other.email and self.ra == other.ra and self.role == other.role