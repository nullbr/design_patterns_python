from asyncore import write

class Logger(object):
    """ A file based message logger with the following attributes
    filename: a string representing the full path of the log file to witch this logger will write its messages """

    def __init__(self, filename):
        self.filename = filename

    # logger method to log messages from anywhere
    def _write_log(level, msg):
        with open(self.filename, "a") as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))

    def critical(self, msg):
        self._write_log("CRITICAL", msg)

    def error(self, msg):
        self._write_log("ERROR", msg)

    def warn(self, msg):
        self._write_log("WARN", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)
