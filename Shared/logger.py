from datetime import datetime


class SimpleLogger:
    def __init__(self, log_file: str):
        self.__log_file = log_file

    def log(self, message: str, level: str):
        output = SimpleLogger.format_message(message, level)
        print(output)
        with open(self.__log_file, 'a') as file:
            file.write(output + '\n')

    @staticmethod
    def format_message(message: str, level: str) -> str:
        return f'{datetime.now()} | {level} | {message}'

    def debug(self, message: str):
        self.log(message, "DEBUG")
