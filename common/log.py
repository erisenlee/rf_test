import logging, time
from common.readConfig import ReadConfig
import os.path
from settings import BASE_DIR
class Log:
    def __init__(self, name,section='Log'):
        self.name = name
        parser = ReadConfig()
        filename=parser.get_option(section,'filename')
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        logfile_name='log/'+filename+now+'_.log'
        filepath = os.path.join(BASE_DIR, logfile_name)
        self.logger = logging.getLogger(self.name)
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=filepath
        )
    
    def info(self,msg):
        self.logger.info(msg)
    def warning(self,msg):
        self.logger.warning(msg)
    def error(self,msg):
        self.logger.error(msg)
    def debug(self,msg):
        self.logger.debug(msg)
    def critical(self,msg):
        self.logger.critical(msg)
    def exception(self, msg):
        self.logger.exception(msg)

def get_log():
    logger = Log(os.path.basename(__file__))
    return logger

if __name__ == '__main__':
    main()
    print(BASE_DIR)