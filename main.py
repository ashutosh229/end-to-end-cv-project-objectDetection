from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
  logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<")
  obj = DataIngestionTrainingPipeline()
  obj.main()
  logger.info(f">>>>> Stage {STAGE_NAME} Ended <<<<<")
except Exception as error:
  logger.exception(error)
  raise error

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} ended <<<<<")
    
except Exception as error:
    logger.exception(error)
    raise error