from src.shared.domain.entities.user import User
from src.shared.domain.enums.role import ROLE
from src.shared.infra.dto.user_cognito_dto import UserCognitoDTO


class Test_UserCognitoDTO:
    def test_user_cognito_dto_from_cognito(self):
        cognito_user = {'Attributes' : [
                {'Name' : 'name',
                'Value' : 'Luigi Trevisan'},
                {'Name' : 'email',
                'Value' : '22.01102-0@maua.br'},
                {'Name' : 'custom:ra',
                'Value' : '22011020'},
                {'Name' : 'custom:role',
                'Value' : 'STUDENT'}],
            'Enabled' : True,
            'UserStatus' : 'CONFIRMED',
            'Username' : 'e2d865b1-e0c3-427e-866a-efa4e72e20f9'}
        
        user_dto = UserCognitoDTO.from_cognito(cognito_user)
        
        assert user_dto == UserCognitoDTO(
            name='Luigi Trevisan',
            ra='22011020',
            email='22.01102-0@maua.br',
            role=ROLE.STUDENT
        )
        
    def test_user_cognito_dto_to_entity(self):
        user_dto = UserCognitoDTO(
            name='Luigi Trevisan',
            ra='22011020',
            email='22.01102-0@maua.br',
            role=ROLE.STUDENT
        )
        
        user = user_dto.to_entity()
        assert user == User(
            name='Luigi Trevisan',
            ra='22011020',
            email="22.01102-0@maua.br",
            role=ROLE.STUDENT
        )
        
    def test_user_cognito_dto_from_cognito_to_entity(self):
        cognito_user = {'Attributes' : [
                {'Name' : 'name',
                'Value' : 'Luigi Trevisan'},
                {'Name' : 'email',
                'Value' : '22.01102-0@maua.br'},
                {'Name' : 'custom:ra',
                'Value' : '22011020'},
                {'Name' : 'custom:role',
                'Value' : 'STUDENT'}],
            'Enabled' : True,
            'UserStatus' : 'CONFIRMED',
            'Username' : 'e2d865b1-e0c3-427e-866a-efa4e72e20f9'}

        user = UserCognitoDTO.from_cognito(cognito_user).to_entity()

        assert user == User(
            name='Luigi Trevisan',
            ra='22011020',
            email="22.01102-0@maua.br",
            role=ROLE.STUDENT
        )
        