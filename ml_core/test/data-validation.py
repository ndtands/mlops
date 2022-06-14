from ml_core import data_validation
from configs.config import logger

if __name__ == '__main__':
    data_validation.validate_data(project='mlops-final')
    logger.info('Validation Done')