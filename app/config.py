from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    # bot_token: SecretStr
    bot_token: str
    bot_container_name: str = 'default_bot_container_name'
    bot_image_name: str = 'default_bot_image_name'
    bot_name: str = 'default_bot_name'
    admin_id: int

    class Config:
        env_file = '.env'


config = Settings()
