import logging
import logging.handlers

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)

# Create a stream handler for the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Set the formatter for the console handler
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

# Create a rotating file handler for the log file
file_handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
file_handler.setLevel(logging.DEBUG)  # Log all levels to the file

# Set the formatter for the file handler
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)
