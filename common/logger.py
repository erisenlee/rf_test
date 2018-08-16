import logging, time
from .readConfig import ReadConfig,BASE_DIR
import os

class Log:
    def __init__(self):
        parser = ReadConfig()
        log_name = parser.get_option('Log', 'name')
        now = time.strftime('%Y_%m_%d_%H_%M_%S')

        filepath=os.path.join(BASE_DIR,'log/'+now+log_name)
        
        self.logger = logging.getLogger(__name__)
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

