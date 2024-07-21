from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    gcp_project_id: str
    gcp_bucket_name: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()