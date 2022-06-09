from enum import Enum
from .enviroments import Enviroments

class Directory(Enum):
    
    root = Enviroments.path_root_bot.value
    init = root + "__init__\\"
    storage = root + "persistence\\storage\\"
    webdriver = root + "services\\browser\\chromedriver.exe"
    extensions = root + "extension\\"
    mock =  root + "mock\\payload.json"
    database = root + "repository\\database\\"
    temporary = root + "tmp\\"
    logs = root + "logs\\"
    image_reference = root + "image_reference\\"
    certificates = f"C:\\Users\\{Enviroments.user.value}\\AppData\\Roaming\\Microsoft\\SystemCertificates\\My\\Certificates\\"

