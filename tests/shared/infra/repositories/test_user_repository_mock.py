from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryMock:
    def test_get_user_by_email(self):
        repo = UserRepositoryMock()
        user = repo.get_user_by_email(repo.users[0].email)
        assert user.ra == repo.users[0].ra
        assert user.name == repo.users[0].name
        assert user.email == repo.users[0].email
        assert user.role == repo.users[0].role