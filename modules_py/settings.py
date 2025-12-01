import json
import logging
from pathlib import PurePath, PureWindowsPath, PurePosixPath, Path


#with open('../resources/settings.json', 'r', encoding='utf-8') as file:
#    users = json.load(file)

#for user in users:
#    print(f"ID: {user['id']}, Имя: {user['name']}, Email: {user['email']}")

logger = logging.getLogger(__name__)


class Setting():
    def __init__(self):
        self.jsonSettingPath =''

    def set_setting_path(self,SettingPath):
        p = Path(SettingPath)
        if(p.exists() and p.is_file( )):
            self.jsonSettingPath = p
            logger.info("Path setting ok")
        else:
            logger.error("path not exist")

    def read_settings(self):
        print(self.jsonSettingPath)
        with open(self.jsonSettingPath, 'r', encoding='utf-8') as file:
            users = json.load(file)
            for user in users:
                print(f"ID: {user['id']}, Имя: {user['name']}, Email: {user['email']}")



