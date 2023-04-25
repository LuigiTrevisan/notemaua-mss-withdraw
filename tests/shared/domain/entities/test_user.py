from src.shared.domain.entities.user import User
from src.shared.domain.enums.role import ROLE
import pytest
from src.shared.helpers.errors.domain_errors import EntityError


class Test_User:
    def test_user(self):
        user = User(
            ra="22011020",
            name="Luigi Trevisan",
            email="22.01102-0@maua.br",
            role=ROLE.STUDENT
        )
        
        assert type(user) == User
        assert user.ra == "22011020"
        assert user.name == "Luigi Trevisan"
        assert user.email == "22.01102-0@maua.br"
        assert user.role == ROLE.STUDENT
            
    def test_user_ra_is_none(self):
        with pytest.raises(EntityError):
            User(
                ra=None,
                name="Luigi Trevisan",
                email="22.01102-0@maua.br",
                role=ROLE.STUDENT
            )
            
        
    def test_user_ra_not_str(self):
        with pytest.raises(EntityError):
            User(
                ra=22011020,
                name="Luigi Trevisan",
                email="22.01102-0@maua.br",
                role=ROLE.STUDENT
            )
            
    def test_user_ra_not_decimal(self):
        with pytest.raises(EntityError):
            User(
                ra="2201102a",
                name="Luigi Trevisan",
                email="22.01102-0@maua.br",
                role=ROLE.STUDENT
            )
            
    def test_user_ra_wrong_length(self):
        with pytest.raises(EntityError):
            User(
                ra="2201102",
                name="Luigi Trevisan",
                email="22.01102-0@maua.br",
                role=ROLE.STUDENT
            )
            
    def test_user_name_is_none(self):
        with pytest.raises(EntityError):
            User(
                ra="22011020",
                name=None,
                email="22.01102-0@maua.br",
                role=ROLE.STUDENT
            )
            
    def test_user_name_not_str(self):
        with pytest.raises(EntityError):
            User(
                ra="22011020",
                name=True,
                email="22.01102-0@maua.br",
                role=ROLE.STUDENT
            )
            
    def test_user_name_wrong_length(self):
        with pytest.raises(EntityError):
            User(
                ra="22011020",
                name="L",
                email="22.01102-0@maua.br",
                role=ROLE.STUDENT
            )
            
    def test_user_email_is_none(self):
        with pytest.raises(EntityError):
            User(
                ra="22011020",
                name="Luigi Trevisan",
                email=None,
                role=ROLE.STUDENT
            )
            
    def test_user_email_not_str(self):
        with pytest.raises(EntityError):
            User(
                ra="22011020",
                name="Luigi Trevisan",
                email=22011020,
                role=ROLE.STUDENT
            )
            
    def test_user_email_not_maua(self):
        with pytest.raises(EntityError):
            User(
                ra="22011020",
                name="Luigi Trevisan",
                email="22.01102-0@gmail.com",
                role=ROLE.STUDENT
            )
            
    def test_user_email_not_email(self):
        with pytest.raises(EntityError):
            User(
                ra="22011020",
                name="Luigi Trevisan",
                email="02938@@@*!$@maua.br",
                role=ROLE.STUDENT
            )
            
    def test_user_role_is_none(self):
        with pytest.raises(EntityError):
            User(
                ra="22011020",
                name="Luigi Trevisan",
                email="22.01102-0@maua.br",
                role=None
            )
            
    def test_user_role_not_enum(self):
        with pytest.raises(EntityError):
            User(
                ra="22011020",
                name="Luigi Trevisan",
                email="22.01102-0@maua.br",
                role="student"
            )
            
    def test_user_role_not_role(self):
        with pytest.raises(EntityError):
            User(
                ra="22011020",
                name="Luigi Trevisan",
                email="22.01102-0@maua.br",
                role=ROLE
            ) 