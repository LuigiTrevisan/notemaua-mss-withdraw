import enum
from enum import Enum
import os
from src.shared.domain.repositories.user_repository_interface import IUserRepository

from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE
    s3_bucket_name: str
    region: str
    endpoint_url: str = None
    dynamo_table_name: str
    dynamo_partition_key: str
    dynamo_sort_key: str
    cloud_front_distribution_domain: str
    user_pool_id: str

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.DOTENV.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

        if self.stage == STAGE.TEST:
            self.s3_bucket_name = "withdraw-s3"
            self.region = "sa-east-1"
            self.endpoint_url = "http://localhost:8000"
            self.dynamo_table_name = "notemaua_mss_withdraw-table"
            self.dynamo_partition_key = "PK"
            self.dynamo_sort_key = "SK"
            self.dynamo_gsi_partition_key = "GSI1-PK"
            self.cloud_front_distribution_domain = "https://d3q9q9q9q9q9q9.cloudfront.net"
            self.user_pool_id = "sa-east-1_cELM9XDrE"

        else:
            self.s3_bucket_name = os.environ.get("S3_BUCKET_NAME")
            self.region = os.environ.get("REGION")
            self.endpoint_url = os.environ.get("ENDPOINT_URL")
            self.dynamo_table_name = os.environ.get("DYNAMO_TABLE_NAME")
            self.dynamo_partition_key = os.environ.get("DYNAMO_PARTITION_KEY")
            self.dynamo_sort_key = os.environ.get("DYNAMO_SORT_KEY")
            self.dynamo_gsi_partition_key = os.environ.get("DYNAMO_GSI_PARTITION_KEY")
            self.cloud_front_distribution_domain = os.environ.get("CLOUD_FRONT_DISTRIBUTION_DOMAIN")
            self.user_pool_id = os.environ.get("USER_POOL_ID")

    @staticmethod
    def get_withdraw_repo() -> IWithdrawRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock
            return WithdrawRepositoryMock
        elif Environments.get_envs().stage == STAGE.PROD:
            from src.shared.infra.repositories.withdraw_repository_dynamo import WithdrawRepositoryDynamo
            return WithdrawRepositoryDynamo
        else:
            raise Exception("No repository found for this stage")

    @staticmethod
    def get_user_repo() -> IUserRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
            return UserRepositoryMock
        elif Environments.get_envs().stage == STAGE.PROD:
            from src.shared.infra.repositories.user_repository_cognito import UserRepositoryCognito
            return UserRepositoryCognito
        else:
            raise Exception("No repository found for this stage")
        
    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage}, s3_bucket_name={self.s3_bucket_name}, region={self.region}, endpoint_url={self.endpoint_url})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return self.__dict__

