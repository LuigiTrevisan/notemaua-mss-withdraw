from src.shared.domain.entities.user import User
from src.shared.domain.enums.role import ROLE
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class Test_UserApiGatewayDynamoDTO:
    def test_user_api_gateway_dynamo_dto_to_entity(self):
        user_dto = UserApiGatewayDTO(
            name="Luigi Trevisan",
            ra="22011020",
            email="22.01102-0@maua.br",
            role=ROLE.STUDENT
        )
        user = user_dto.to_entity()
        assert user == User(name="Luigi Trevisan", ra="22011020", email="22.01102-0@maua.br", role=ROLE.STUDENT)
        
    def test_user_api_gateway_dynamo_dto_from_api_gateway(self):
        user_data = {
            "name": "Luigi Trevisan",
            "custom:ra": "22011020",
            "email": "22.01102-0@maua.br",
            "custom:role": "STUDENT"
        }
        user_dto = UserApiGatewayDTO.from_api_gateway(user_data)
        assert user_dto == UserApiGatewayDTO(name="Luigi Trevisan", ra="22011020", email="22.01102-0@maua.br", role=ROLE.STUDENT)