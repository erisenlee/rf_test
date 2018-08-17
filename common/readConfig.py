import configparser
import os.path
from settings import BASE_DIR

config_file = os.path.join(BASE_DIR, 'config.ini')


class ReadConfig:
    def __init__(self, file_path=None):
        self.file_path = file_path if file_path else config_file
        
        self.parser = configparser.ConfigParser()
        self.parser.read(self.file_path,encoding='utf-8')

    def get_section(self, section_name):
        if not self.parser.has_section(section_name):
            raise ValueError('section_name uncorrect')
        config_list = self.parser.items(section_name)
        return config_list
        
        

    def get_option(self, section, option):
        if self.parser.has_option(section, option):
            return self.parser.get(section, option)
        else:
            return None
    def update_attr(self, instance, section):
        config_list = self.get_section(section)
        if not config_list:
            raise ValueError('empty config of {}'.format(section))
        # print(config_list)
        config_dict={k.lower():v for k, v  in config_list}
        for key, value in config_dict.items():
                setattr(instance, key, value)
                
        
    

if __name__ == '__main__':
    c = ReadConfig()
    # value=c.get_option('Db','host')
    value=c.get_section('Db')
    print(value)
        
        
    

        