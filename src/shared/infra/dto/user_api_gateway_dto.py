from src.shared.domain.entities.user import User
from src.shared.domain.enums.role import ROLE


class UserApiGatewayDTO:
    name: str
    ra: str
    email: str
    role: ROLE
    
    def __init__(self, name: str, ra: str, email: str, role: ROLE):
        self.name = name
        self.ra = ra
        self.email = email
        self.role = role
        
    @staticmethod
    def from_api_gateway(user_data: dict) -> "UserApiGatewayDTO":
        return UserApiGatewayDTO(
            name=user_data["name"],
            ra=user_data.get("custom:ra"),
            email=user_data["email"],
            role=ROLE(user_data["custom:role"])
        )
        
    def to_entity(self) -> User:
        if self.ra is not None:
            ra = self.ra.replace("-", "")
            ra = ra.replace(".", "")
        else:
            ra = None
        return User(
            name=self.name,
            ra=ra,
            email=self.email,
            role=self.role
        )
        
    def __eq__(self, other):
        return self.name == other.name and self.ra == other.ra and self.email == other.email and self.role == other.role