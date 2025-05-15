from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    project_name: str
    database_url: str
    test_database_url: str = "sqlite:///./test.db"
    secret_key: str

    class Config:
        env_file = ".env"
        extra = "allow"  # This allows extra fields in the .env file without causing validation errors

settings = Settings()