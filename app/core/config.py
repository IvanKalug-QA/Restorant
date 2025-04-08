from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret: str
    main_host: str

    class Config:
        env_file = '.env'


settings = Settings()
