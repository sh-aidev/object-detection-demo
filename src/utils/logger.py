import os

from src.pylogger.logger import Logger
from src.utils.config import Config

class Logger_py:

    def __init__(self) -> None:
        self.config_root_dir = "configs"
        self.config = Config(self.config_root_dir)
        self.logger = Logger.create_sess(os.getenv("ENVIRONMENT", self.config.obj_detector.logger.environment))
        self.logger.info(
            f"Logger for environemnt: {str(os.getenv('ENVIRONMENT', self.config.obj_detector.logger.environment))}"
        )
    
    def run(self) -> Logger:
        return self.logger
        
logger = Logger_py().run()