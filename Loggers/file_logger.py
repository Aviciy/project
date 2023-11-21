from datetime import datetime

from Abstract.logger import Logger


class FileLogger(Logger):

    def __init__(self, filename: str) -> object:
        super().__init__()
        self.__filename = filename

    def __log(self, message: str) -> None:
        with open(self.__filename, 'a') as file:
            file.write(f'{datetime.now()} | {message}\n')

    def trace(self, message: str) -> None:
        self.__log(f'{datetime.now()} | TRACE | {message}')

    def debug(self, message: str) -> None:
        self.__log(f'{datetime.now()} | DEBUG | {message}')

    def info(self, message: str) -> None:
        self.__log(f'{datetime.now()} | INFO | {message}')

    def warning(self, message: str) -> None:
        self.__log(f'{datetime.now()} | WARNING | {message}')

    def error(self, message: str) -> None:
        self.__log(f'{datetime.now()} | ERROR | {message}')

    def critical(self, message: str) -> None:
        self.__log(f'{datetime.now()} | CRITICAL | {message}')
