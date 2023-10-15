import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_API = str(os.getenv('TOKEN_API'))
ADMIN = str(os.getenv('ADMIN'))

__all__ = ['TOKEN_API', 'ADMIN']