from Abstract.logger import Logger


class CompositeLogger(Logger):
    def __init__(self, *loggers):
        super().__init__()
        self.__loggers = loggers

    def trace(self, message: str) -> None:
        for logger in self.__loggers:
            logger.trace(message)

    def debug(self, message: str) -> None:
        for logger in self.__loggers:
            logger.debug(message)

    def info(self, message: str) -> None:
        for logger in self.__loggers:
            logger.info(message)

    def warning(self, message: str) -> None:
        for logger in self.__loggers:
            logger.warning(message)

    def error(self, message: str) -> None:
        for logger in self.__loggers:
            logger.error(message)

    def critical(self, message: str) -> None:
        for logger in self.__loggers:
            logger.critical(message)
