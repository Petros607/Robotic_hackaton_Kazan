import os
import string

class DBSettings:
    CONNECT_STRING = string.Template(
        "postgresql+asyncpg://${user}:${password}@${hostname}/${dbname}"
    )

    @classmethod
    def get_url(cls) -> str:
        URL = cls.CONNECT_STRING.substitute(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            hostname=os.getenv('DB_SERVER')+":"+os.getenv('DB_HOST'),
            dbname=os.getenv("DB_NAME"),
        )
        return URL