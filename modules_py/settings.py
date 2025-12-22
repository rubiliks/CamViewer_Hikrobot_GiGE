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
        self.valvesNumber = 80
        self.valvesLengthToBlock = 1.2
        self.conveyerSpeed = 2.53
        self.valvesTimeOpen = 0.25
        self.valveTimeDelta = 0.0
        self.modbusInOutIp = "192.168.88.150"

    def set_setting_path(self,SettingPath):
        p = Path(SettingPath)
        if(p.exists() and p.is_file( )):
            self.jsonSettingPath = p
            logger.info("Path setting ok")
        else:
            logger.error("path not exist")

    def read_settings(self):
        with open(self.jsonSettingPath, 'r', encoding='utf-8') as file:
            self.confige = json.load(file)
            self.cameraSettingGain = self.confige['cameraSetting']['gain']
            self.cameraSettingExposureTime = self.confige['cameraSetting']['exposureTime']
            self.cameraSettingBalanceRed = self.confige['cameraSetting']['BalanceRed']
            self.cameraSettingBalanceGreen = self.confige['cameraSetting']['BalanceGreen']
            self.cameraSettingBalanceBlue = self.confige['cameraSetting']['BalanceBlue']
            self.cameraSettingWidth = self.confige['cameraSetting']['Width']
            self.cameraSettingHeight = self.confige['cameraSetting']['Height']
            self.cameraSettingOffsetX = self.confige['cameraSetting']['OffsetX']
            self.cnnPath = self.confige['CnnSetting']['cnnPath']
            self.cameraSettingReverseX = self.confige['cameraSetting']['ReverseX']
            self.valveTimeDelta = self.confige['Valve']['valveTimeDelta']
            self.valvesTimeOpen = self.confige['Valve']['valveTimeToOpen']
            self.valvesNumber = self.confige['Valve']['valvesNumber']
            self.valvesLengthToBlock = self.confige['Valve']['valvesLengthToBlock']
            self.conveyerSpeed = self.confige['Valve']['conveyerSpeed']
            self.modbusInOutIp = self.confige['modbusInOut']['ip']


    def write_setting_gain(self, gain_link):
        self.confige['cameraSetting']['gain'] = gain_link
        with open(self.jsonSettingPath, "w",encoding='utf-8') as file:
            json.dump(self.confige, file,ensure_ascii=False, indent=4)

    def write_setting_exposure(self, exposure_link):
        self.confige['cameraSetting']['exposureTime'] = exposure_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_BalanceRed(self, BalanceRed_link):
        self.confige['cameraSetting']['BalanceRed'] = BalanceRed_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_BalanceGreen(self, BalanceGreen_link):
        self.confige['cameraSetting']['BalanceGreen'] = BalanceGreen_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_BalanceBlue(self, BalanceBlue_link):
        self.confige['cameraSetting']['BalanceBlue'] = BalanceBlue_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_Width(self, Width_link):
        self.confige['cameraSetting']['Width'] = Width_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_Height(self, Height_link):
        self.confige['cameraSetting']['Height'] = Height_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_OffsetX(self, OffsetX_link):
        self.confige['cameraSetting']['OffsetX'] = OffsetX_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_valveTimeDelta(self, valveTimeDelta_link):
        self.confige['Valve']['valveTimeDelta'] = valveTimeDelta_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_valvesTimeOpen(self, valvesTimeOpen_link):
        self.confige['Valve']['valveTimeToOpen'] = valvesTimeOpen_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_valvesLengthToBlock(self, valvesLengthToBlock_link):
        self.confige['Valve']['valvesLengthToBlock'] = valvesLengthToBlock_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_valvesNumber(self, valvesNumber_link):
        self.confige['Valve']['valvesNumber'] = valvesNumber_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_conveyerSpeed(self, valvesSpeed_link):
        self.confige['Valve']['conveyerSpeed'] = valvesSpeed_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)

    def write_setting_modbusInOutIp(self, ip_link):
        self.confige['modbusInOut']['ip'] = ip_link
        with open(self.jsonSettingPath, "w", encoding='utf-8') as file:
            json.dump(self.confige, file, ensure_ascii=False, indent=4)



