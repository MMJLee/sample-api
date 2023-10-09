import os
from pydantic import BaseSettings

env = os.environ.get('ENV')

def configure_db_connection(env='dev') -> str:
    if env == 'prod':
        engine = os.environ.get('DB_ENGINE')
        username = os.environ.get('DB_USERNAME')
        password = os.environ.get('DB_PASS')
        host = os.environ.get('DB_HOST')
        port = os.environ.get('DB_PORT')
        db_name = os.environ.get('DB_NAME')
        return f'{engine}://{username}:{password}@{host}:{port}/{db_name}'
    return "postgresql://postgres:postgres@localhost:5432/postgres"

class Settings(BaseSettings):
    # API config settings
    API_VERSION: str = '1.0.0' 
    API_MAJOR_VERSION: str = API_VERSION.split('.')[0]
    API_TITLE: str = 'Sample API'

    # DB connection pool config settings
    MIN_DB_POOL_SIZE: int = 1
    MAX_DB_POOL_SIZE: int = 1
    # CORS config settings
    ALLOW_ORIGIN_REGEX: str = r'.*'

class ProductionConfig(Settings):
    #set specific regex for produciton
    ALLOW_ORIGIN_REGEX = r''
    # DB connection pool settings
    MAX_DB_POOL_SIZE = 10
    # DB connection config settings
    DATABASE_URL = configure_db_connection(env)

class DevelopmentConfig(Settings):
    # DB connection pool settings
    MAX_DB_POOL_SIZE = 10
    # DB connection config settings
    DATABASE_URL = configure_db_connection(env)


def get_settings():
    if env == 'prod':
        return ProductionConfig()
    else:
        return DevelopmentConfig()