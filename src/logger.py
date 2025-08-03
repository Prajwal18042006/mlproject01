import logging
import os
from datetime import datetime

# Step 1: Create logs directory
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Step 2: Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Step 3: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("logging has started ")
