import logging

class Logger:
    def __init__(self, log_file):
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

    def log(self, message: str):
        self.logger.debug(message)

if __name__ == "__main__":
    logger = Logger("my_log_file.log")
    logger.log("Це повідомлення для лог-файлу (debug)")

