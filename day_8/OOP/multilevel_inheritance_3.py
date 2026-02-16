class Logger:
    def log(self, message):
        print(f"Log: {message}")

class FileLogger(Logger):
    def log(self, message):
        super().log(message)
        with open("log.txt", "a") as file:
            file.write(f"{message}\n")  

class CloudLogger(Logger):
    def log(self, message):
        super().log(message)
        print(f"Logging to cloud: {message}")

file_logger = FileLogger()
cloud_logger = CloudLogger()
file_logger.log("This is a file log message.")
cloud_logger.log("This is a cloud log message.")                                                                                                                                                                                                                                                                                                                                                                                                                                                        