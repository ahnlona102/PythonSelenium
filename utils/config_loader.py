import configparser
import os

class ConfigLoader:
    config = configparser.ConfigParser()

    def load_properties(self):
        try:
            config_file = os.path.join(os.path.dirname(__file__), 'config.properties')
            print(f"Attempting to load config file from: {config_file}")
            if not os.path.exists(config_file):
                raise FileNotFoundError(f"Config file {config_file} not found.")
            self.config.read(config_file)
        except Exception as e:
            raise RuntimeError(f"Failed to load config file: {e}")

    def get_property(self, section, key):
        if not self.config.sections():
            self.load_properties()
        return self.config.get(section, key)