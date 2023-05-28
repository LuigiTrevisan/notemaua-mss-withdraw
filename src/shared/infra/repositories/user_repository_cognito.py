from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.environments import Environments
from src.shared.infra.dto.user_cognito_dto import UserCognitoDTO
import boto3

class UserRepositoryCognito(IUserRepository):
    client: boto3.client
    user_pool_id: str
    
    def __init__(self):
        self.client = boto3.client('cognito-idp')
        self.user_pool_id = Environments.get_envs().user_pool_id
    
    def get_user_by_email(self, email: str) -> User:
        response = self.client.list_users(
            UserPoolId=self.user_pool_id,
            Filter=f'email = "{email}"'
        )
        if len(response['Users']) == 0:
            return None
        
        user = UserCognitoDTO.from_cognito(response['Users'][0]).to_entity()
        return user