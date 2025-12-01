import json
import pathlib

with open('../resources/settings.json', 'r', encoding='utf-8') as file:
    users = json.load(file)

for user in users:
    print(f"ID: {user['id']}, Имя: {user['name']}, Email: {user['email']}")


class Setting():
    def __init__(self):
        self.jsonSettingPath = ''

    def set_model_path(self,SettingPath):


        self.jsonSettingPath = SettingPath



