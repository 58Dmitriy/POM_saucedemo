import logging
import datetime
import os


class Logger:
    _logger = None

    @staticmethod
    def get_logger():
        if Logger._logger is None:
            # создаём папку для логов, если её нет
            log_dir = "logs"
            os.makedirs(log_dir, exist_ok=True)

            # уникальное имя файлф лога с временной меткой
            log_filename = datetime.datetime.now().strftime("test_run_%Y-%m-%d_%H-%M-%S.log")
            log_filepath = os.path.join(log_dir, log_filename)

            # Создаём экземпляр логгера
            Logger._logger = logging.getLogger("autotest_logger")
            # Устанавливаем уровень логирования
            Logger._logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter(""
                                          "%(asctime)s - %(levelname)s - %(name)s"
                                          " - [%(filename)s] - %(message)s"
                                          )
            file_handler = logging.FileHandler(log_filepath)
            # В файл логов пишем всё с уровнем DEBUG
            file_handler.setLevel(logging.DEBUG)

            # Связываем форматировщик с обработчиком
            file_handler.setFormatter(formatter)

            # Связываем обработчик с логгером
            Logger._logger.addHandler(file_handler)

            Logger._logger.info("Логгирование инициализированно")

        return Logger._logger

log = Logger.get_logger()
