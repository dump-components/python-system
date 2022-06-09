import os, glob, sys, pathlib, shutil

from .enviroments import Enviroments
from .directory import Directory

class OperationSystem:
    
    def __init__(self) -> None:
        self._enviroments = Enviroments
        self._directory = Directory
        
    @property
    def computer_name(self):
        return os.environ['COMPUTERNAME']
    
    @property
    def env(self):
        return self._enviroments
    
    @property
    def directory(self):
        return self._directory
    
    def close_chrome_instances(self):
        os.system('taskkill /IM "chrome.exe" /F')
        os.system('taskkill /IM "chromedriver.exe" /F')
        os.system('taskkill /IM "chromeserver.exe" /F')
        
    
    def dell_all_files_in_tmp(self):
        try:
            files = glob.glob(self._directory.temporary.value + '*')
            for f in files:
                os.remove(f)
            with open(self._directory.temporary.value + ".gitkeep"):
                pass
        except Exception as Ex:
            sys.exit(Ex)
    
    def extensions_exists_in_path(self, extension, path):
        file_dir = path
        file_ext = f"*.{extension}"
        try:
            dir_file = list(pathlib.Path(file_dir).glob(file_ext))
            if os.path.exists(dir_file):
                return dir_file
        except:
            return None
    
    def move_file(self, dir_src, dir_dst):
        try:
            shutil.move(dir_src, dir_dst)
        except Exception as err:
            sys.exit(err)