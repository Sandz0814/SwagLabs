import logging
import os


class LogGen:
    @staticmethod
    def logger():
        # Define the log directory and file
        log_directory = os.path.join(os.getcwd(), "Logs")  # Get the root directory
        log_file = "automation.log"

        # Create the Logs directory if it doesn't exist
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Set up logging configuration
        logging.basicConfig(
            filename=os.path.join(log_directory, log_file),
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )

        # Create or get the root logger
        log = logging.getLogger()
        log.setLevel(logging.INFO)

        return log
