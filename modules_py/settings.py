import json
import logging
from pathlib import PurePath, PureWindowsPath, PurePosixPath, Path

logger = logging.getLogger(__name__)

class Setting():
    def __init__(self):
        self.jsonSettingPath =''
        self.cameraSettingGain = 23.98
        self.cameraSettingExposureTime = 40
        self.cameraSettingBalanceRed = 1460
        self.cameraSettingBalanceGreen = 1024
        self.cameraSettingBalanceBlue = 1957
        self.cameraSettingWidth = 4096
        self.cameraSettingHeight = 1000
        self.cameraSettingOffsetX = 100
        self.cameraSettingReverseX = False
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
            self.cnnPath = config['CnnSetting']['cnnPath']
            self.cameraSettingReverseX = config['cameraSetting']['ReverseX']

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

    def write_setting_Width(self, Width_link):
        self.confige['cameraSetting']['Width'] = Width_link
        with open(self.jsonSettingPath, "w") as file:
            json.dump(self.confige, file)

    def write_setting_Height(self, Height_link):
        self.confige['cameraSetting']['Height'] = Height_link
        with open(self.jsonSettingPath, "w") as file:
            json.dump(self.confige, file)

    def write_setting_OffsetX(self, OffsetX_link):
        self.confige['cameraSetting']['OffsetX'] = OffsetX_link
        with open(self.jsonSettingPath, "w") as file:
            json.dump(self.confige, file)




