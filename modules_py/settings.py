import json
import logging
from pathlib import PurePath, PureWindowsPath, PurePosixPath, Path

logger = logging.getLogger(__name__)

class Setting():
    def __init__(self):
        self.jsonSettingPath =''
        self.cameraSettingGain = 0.0
        self.cameraSettingExposureTime = 0
        self.cameraSettingBalanceRed = 0
        self.cameraSettingBalanceGreen = 0
        self.cameraSettingBalanceBlue = 0
        self.cameraSettingWidth = 0
        self.cameraSettingHeight = 0
        self.cameraSettingOffsetX = 0
        self.cameraSettingOffsetY = 0
        self.confige = ''
        self.cnnPath = ''

    def set_setting_path(self,SettingPath):
        p = Path(SettingPath)
        if(p.exists() and p.is_file( )):
            self.jsonSettingPath = p
            logger.info("Path setting ok")
        else:
            logger.error("path not exist")

    def read_settings(self):
        with open(self.jsonSettingPath, 'r', encoding='utf-8') as file:
            self.confige = config = json.load(file)
            self.cameraSettingGain = config['cameraSetting']['gain']
            self.cameraSettingExposureTime = config['cameraSetting']['exposureTime']
            self.cameraSettingBalanceRed = config['cameraSetting']['BalanceRed']
            self.cameraSettingBalanceGreen = config['cameraSetting']['BalanceGreen']
            self.cameraSettingBalanceBlue = config['cameraSetting']['BalanceBlue']
            self.cameraSettingWidth = config['cameraSetting']['Width']
            self.cameraSettingHeight = config['cameraSetting']['Height']
            self.cameraSettingOffsetX = config['cameraSetting']['OffsetX']
            self.cameraSettingOffsetY = config['cameraSetting']['OffsetY']
            self.cnnPath = config['CnnSetting']['cnnPath']

    def write_setting_gain(self, gain_link):
        self.confige['cameraSetting']['gain'] = gain_link
        with open(self.jsonSettingPath, "w") as file:
            json.dump(self.confige, file)

    def write_setting_exposure(self, exposure_link):
        self.confige['cameraSetting']['exposureTime'] = exposure_link
        with open(self.jsonSettingPath, "w") as file:
            json.dump(self.confige, file)

    def write_setting_BalanceRed(self, BalanceRed_link):
        self.confige['cameraSetting']['BalanceRed'] = BalanceRed_link
        with open(self.jsonSettingPath, "w") as file:
            json.dump(self.confige, file)

    def write_setting_BalanceGreen(self, BalanceGreen_link):
        self.confige['cameraSetting']['BalanceGreen'] = BalanceGreen_link
        with open(self.jsonSettingPath, "w") as file:
            json.dump(self.confige, file)

    def write_setting_BalanceBlue(self, BalanceBlue_link):
        self.confige['cameraSetting']['BalanceBlue'] = BalanceBlue_link
        with open(self.jsonSettingPath, "w") as file:
            json.dump(self.confige, file)



