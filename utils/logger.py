import logging.handlers
import os


def __setup_logger(filename):


    LOG_LOCATION = './logs'

    if not os.path.exists(LOG_LOCATION):
        os.makedirs(LOG_LOCATION)

    # logfile settings
    LOG_FORMAT = "%(asctime)s [%(levelname)-5.5s] %(message)s"
    LOG_PATH = LOG_LOCATION

    progressLogger = logging.getLogger(filename)
    progressLogger.setLevel(logging.DEBUG)
    rotatingfileHandler = logging.handlers.RotatingFileHandler(LOG_PATH +"/"+ filename,
                                                               maxBytes=(1048576 * 5), backupCount=7)
    # log file handler
    logFormatter = logging.Formatter(LOG_FORMAT)
    rotatingfileHandler.setFormatter(logFormatter)
    progressLogger.addHandler(rotatingfileHandler)
    rotatingfileHandler.setLevel(logging.INFO)

    # console handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    progressLogger.addHandler(consoleHandler)
    consoleHandler.setLevel(logging.INFO)
    return progressLogger

log_file = "pharmeasy_service.log"
serviceLogger = __setup_logger(log_file)
