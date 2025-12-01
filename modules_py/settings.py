import json
import logging
from pathlib import PurePath, PureWindowsPath, PurePosixPath, Path

logger = logging.getLogger(__name__)

class Setting():
    def __init__(self):
        self.jsonSettingPath =''
        self.cameraSettingGain = 0.0
        self.cameraSettingExposureTime = 0
        self.confige = ''

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
            self.confige = config = json.load(file)
            self.cameraSettingGain = config['cameraSetting']['gain']
            self.cameraSettingExposureTime = config['cameraSetting']['exposureTime']

    def write_setting(self):
        self.confige['cameraSetting']['gain'] =20.0
        self.confige['cameraSetting']['exposureTime'] = 20000
        with open(self.jsonSettingPath, "w") as file:
            json.dump(self.confige, file)





