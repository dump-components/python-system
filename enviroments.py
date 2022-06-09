from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()
 

class Enviroments(Enum):
    
    user = os.getlogin()
    selenoid_host = os.getenv('SELENOID_HOST')
    extensions = os.getenv('EXTENSIONS')
    remote_browser = os.getenv('DRIVER_REMOTE')
    path_root_bot = os.getenv('DIRECTORY')
    host_api_nivy = os.getenv('HOST_NYVI')
    mock_task = os.getenv('MOCK_TASK')
    host_nivy_api = os.getenv('HOST_NYVI')
    username_api = os.getenv('USERNAME_API')
    password_api = os.getenv('PASSWORD_API')
    path_ocr = os.getenv('PATH_OCR')
