from tokenize import Single
from singleton_logger import Logger

logger_object = Logger()
logger_object.filename = "./singleton_logger/script.log"

logger_object.info("This is an info message")

print("Logger Object: ", logger_object)

logger_object.warn("THIS IS A WARN MESSAGE!!")