import logging
import inspect
import logging.config

class CustomLogger:

    def custom_logger(self, loglevel=logging.DEBUG):
        loggername = inspect.stack()[1][3]
        log = logging.getLogger(loggername)
        log.setLevel(logging.INFO)

        file_handler = logging.FileHandler("automation1.log", mode='a')
        #file_handler = logging.StreamHandler()
        file_handler.setLevel(loglevel)
        formatter = logging.Formatter("%(asctime)s- %(name)s- %(levelname)s- %(message)s",
                                      datefmt="%d-%m-%y %HH:%MM:%SS")
        file_handler.setFormatter(formatter)

        log.addHandler(file_handler)

        return log

