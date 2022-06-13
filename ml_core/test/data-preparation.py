from ml_core import data_preparation
from configs.config import logger

if __name__ == '__main__':
    data_preparation.preparation_data(project='mlops')
    logger.info('Data Preparation Done')