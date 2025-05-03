import requests
import configparser
from typing import Optional, Dict, List
import time

class MCXController:
    def __init__(self, config_path: str = 'config.ini'):
        self.config = configparser.ConfigParser()
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config.read_file(f)
        self.base_url = f"http://{self.config['MCX_CONTROLLER']['ip_address']}:{self.config['MCX_CONTROLLER']['port']}"
        self.security_key = self.config['MCX_CONTROLLER']['security_key']
        self.timeout = int(self.config['MCX_CONTROLLER']['timeout'])
        self.current_preset: Optional[str] = None
        self.error_message: Optional[str] = None

    def load_preset(self, preset_name: str) -> bool:
        """プリセットを読み込む"""
        try:
            url = f"{self.base_url}/api/command/preset load {preset_name}/{self.security_key}"
            response = requests.get(url, timeout=self.timeout)
            
            if response.status_code == 200:
                if "success" in response.text:
                    self.current_preset = preset_name
                    self.error_message = None
                    return True
                else:
                    self.error_message = self.config['ERROR_MESSAGES']['preset_error'].format(preset_name=preset_name)
                    return False
            else:
                self.error_message = self.config['ERROR_MESSAGES']['connection_error']
                return False
                
        except requests.exceptions.Timeout:
            self.error_message = self.config['ERROR_MESSAGES']['timeout']
            return False
        except Exception as e:
            self.error_message = str(e)
            return False

    def get_preset_list(self) -> Dict[str, List[str]]:
        """利用可能なプリセットの一覧を取得"""
        presets = {
            'one_to_one': [p.strip() for p in self.config['PRESETS']['one_to_one'].split(',')],
            'n_to_one': [p.strip() for p in self.config['PRESETS']['n_to_one'].split(',')]
        }
        return presets

    def get_preset_display_name(self, preset_name: str) -> str:
        """プリセットの表示名を取得"""
        return self.config['PRESET_NAMES'].get(preset_name, preset_name)

    def get_current_preset(self) -> Optional[str]:
        """現在のプリセットを取得"""
        return self.current_preset

    def get_error_message(self) -> Optional[str]:
        """エラーメッセージを取得"""
        return self.error_message 