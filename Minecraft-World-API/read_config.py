import configparser


class ReadConfig:
    def __init__(self):
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read('options.ini')

    def read_single_value(self, value, section):
        return self.config_parser.get(section, value)
