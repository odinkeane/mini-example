from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    
    __FRONTEND_URL = f"{os.getenv("FRONTEND_HOST")}:{os.getenv("FRONTEND_PORT")}"
    __TITLE = os.getenv("APP_NAME")
    __DB_TYPE = os.getenv("DB_TYPE")
    __DB_HOST = os.getenv("DB_HOST")
    __DB_PORT = os.getenv("DB_PORT")
    __DB_USER = os.getenv("DB_USER")
    __DB_PASSWORD =os.getenv("DB_PASSWORD")
    __DB_NAME = os.getenv("DB_NAME")
    __DB_URL = f"{__DB_TYPE}://{__DB_USER}:{__DB_PASSWORD}@{__DB_HOST}:{__DB_PORT}/{__DB_NAME}"

    @staticmethod
    def get_frontend_url():
        return Settings.__FRONTEND_URL
    @staticmethod
    def get_api_title():
        return Settings.__TITLE
    @staticmethod
    def get_database_url():
        return Settings.__DB_URL
    

if __name__ == "__main__":
    print(Settings.__DB_HOST)
    
