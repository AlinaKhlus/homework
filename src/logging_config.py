import logging


def setup_logger(name: str, log_file_path: str | None = None):
    # Создаём логгер для конкретного модуля или функции
    logger = logging.getLogger(name)

    # Уровень логирования — INFO или выше
    logger.setLevel(logging.INFO)

    # Если путь к файлу передан, пишем туда; иначе выводим в консоль
    if log_file_path is not None:
        handler = logging.FileHandler(log_file_path, encoding="utf-8")
    else:
        handler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
