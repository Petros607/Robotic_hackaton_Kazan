import json
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_CONFIGS = "src/user/token/token_configs.json"

with open(TOKEN_CONFIGS, 'r') as f:
    token_configs = json.load(f)
    
ALGORITHM = token_configs["ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = token_configs["ACCESS_TOKEN_EXPIRE_MINUTES"]
REFRESH_TOKEN_EXPIRE_DAYS = token_configs["REFRESH_TOKEN_EXPIRE_DAYS"]

SECRET_KEY = os.environ.get("JWT_KEY")
