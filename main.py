from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
  logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<")
  obj = DataIngestionTrainingPipeline()
  obj.main()
  logger.info(f">>>>> Stage {STAGE_NAME} Ended <<<<<")
except Exception as error:
  logger.exception(error)
  raise error