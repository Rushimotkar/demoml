import logging 
import os 
from  datetime  import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path=os.path.join(os.getcwd(),LOG_FILE)
os.makedirs(logs_path,exist_ok=True)


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)



if __name__ == "__main__":
    
    logging.info("logging has started")