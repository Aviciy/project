from datetime import datetime

from Abstract.logger import Logger


class ConsoleLogger(Logger):

    def __init__(self):
        super().__init__()

    def trace(self, message: str) -> None:
        print(f'{datetime.now()} | TRACE | {message}')

    def debug(self, message: str) -> None:
        print(f'{datetime.now()} | DEBUG | {message}')

    def info(self, message: str) -> None:
        print(f'{datetime.now()} | INFO | {message}')

    def warning(self, message: str) -> None:
        print(f'{datetime.now()} | WARNING | {message}')

    def error(self, message: str) -> None:
        print(f'{datetime.now()} | ERROR | {message}')
        
    def critical(self, message: str) -> None:
        print(f'{datetime.now()} | CRITICAL | {message}')
