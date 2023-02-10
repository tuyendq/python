# Import module
import logging

# Create and configure logger
logging.basicConfig(filename="logs/python.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Create object
logger = logging.getLogger()

# Set log level to DEBUG/INFO/WARNING/ERROR/CRITICAL
logger.setLevel(logging.INFO)

# Test messages
logger.info("This is an info message")