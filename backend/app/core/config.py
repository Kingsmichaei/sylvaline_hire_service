from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Sylvaline Hire"
    VERSION: str = "1.0.0"
    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 
    # Nomba API Credentials 
    NOMBA_CLIENT_ID: str
    NOMBA_CLIENT_SECRET: str
    NOMBA_ACCOUNT_ID: str 
    NOMBA_WEBHOOK_SECRET: str
    SUB_ACCOUNT_ID: str
    NOMBA_BASE_URL: str 

    #SMTP Configuration
    SMTP_HOST: str | None = None
    SMTP_PORT: int = 587
    SMTP_USERNAME: str | None = None
    SMTP_PASSWORD: str | None = None
    SMTP_FROM_EMAIL: str | None = None
    SMTP_FROM_NAME: str = "Sylvaline Hire"
    SMTP_USE_TLS: bool = True

    PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = 30
    
    DATABASE_URL: str 
    FRONTEND_URL: str

    model_config = SettingsConfigDict(
        env_file= ".env",
        extra= "ignore"
    )

settings = Settings()