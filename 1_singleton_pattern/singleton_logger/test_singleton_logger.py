from tokenize import Single
from singleton_logger import Logger

logger_object = Logger()
logger_object.filename = "./1_singleton_pattern/singleton_logger/script.log"

logger_object.info("This is an info message")

print("Logger Object: ", logger_object)


logger_object2 = Logger()

logger_object2.warn("THIS IS A WARN MESSAGE!!")

print("Logger Object 2: ", logger_object2)