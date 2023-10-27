import logging

class SimpleLogger:
    def __init__(self, log_file, log_to_console=True):
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

        if log_to_console:
            self.logger.addHandler(logging.StreamHandler())

    def log(self, message, level=logging.INFO):
        getattr(self.logger, logging.getLevelName(level).lower())(message)

# Приклад використання
if __name__ == "__main__":
    logger = SimpleLogger("my_log_file.log", log_to_console=True)
    logger.log("info")
    logger.log("debug", level=logging.DEBUG)
    logger.log("warning", level=logging.WARNING)
    logger.log("error", level=logging.ERROR)