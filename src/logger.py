from logging import DEBUG, StreamHandler, basicConfig, getLogger

# rotating_file_handler = RotatingFileHandler(filename=".log", maxBytes=512)
# rotating_file_handler.setLevel(INFO)

basicConfig(
    level=DEBUG,
    force=True,
    encoding="UTF-8",
    format="%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s",
    handlers=[StreamHandler()],
)

logger = getLogger()
