from ml_core import training
from configs.config import logger

if __name__ == '__main__':
    training.train(project='mlops-final')
    logger.info('Training + Tuning Done')