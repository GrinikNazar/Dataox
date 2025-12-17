from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    app_name: str
    app_host: str
    app_port: int

    scrape_start_url: str
    scrape_time: str
    dump_time: str

    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    class Config:
        env_file = ".env"


settings = Settings()
