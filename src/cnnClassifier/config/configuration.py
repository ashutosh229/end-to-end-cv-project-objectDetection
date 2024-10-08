from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import read_yaml,create_directories
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
from src.cnnClassifier.entity.config_entity import PrepareBaseModelConfig
from src.cnnClassifier.entity.config_entity import TrainingConfig
import os

class ConfigurationManager:
  def __init__(
    self,
    config_filepath = CONFIG_FILE_PATH,
    params_filepath = PARAMS_FILE_PATH,
    
  ):
    self.config = read_yaml(config_filepath)
    self.params = read_yaml(params_filepath)
    
    create_directories([self.config.artifacts_root])
  
  def get_data_ingestion_config(self)->DataIngestionConfig:
    config = self.config.data_ingestion
    create_directories([config.root_dir])
    data_ingestion_config = DataIngestionConfig(
      root_dir=config.root_dir,
      source_url=config.source_url,
      local_data_file=config.local_data_file,
      unzip_dir=config.unzip_dir
    )
    return data_ingestion_config
  
  def get_prepare_base_model_config(self)->PrepareBaseModelConfig:
    config = self.config.prepare_base_model
    params = self.params
    create_directories([config.root_dir])
    prepare_base_model_config = PrepareBaseModelConfig(
      root_dir=Path(config.root_dir),
      base_model_path=Path(config.base_model_path),
      updated_model_path=Path(config.updated_base_model_path),
      params_image_size=params.IMAGE_SIZE,
      params_classes=params.CLASSES,
      params_weights=params.WEIGHTS,
      params_include_top=params.INCLUDE_TOP,
      params_learning_rate=params.LEARNING_RATE        
    )
    return prepare_base_model_config
  
  def get_training_config(self)->TrainingConfig:
    params = self.params
    training = self.config.training #extracting the training configurations
    prepare_base_model = self.config.prepare_base_model 
    training_data = os.path.join(self.config.data_ingestion.unzip_dir,"Chest-CT-Scan-data")
    create_directories([Path(training.root_dir)])
    
    training_config = TrainingConfig(
      root_dir=Path(training.root_dir),
      trained_model_path=Path(training.trained_model_path),
      updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
      training_data=Path(training_data),
      params_batch_size=params.BATCH_SIZE,
      params_epochs=params.EPOCHS,
      params_image_size=params.IMAGE_SIZE,
      params_is_augmentation=params.AUGMENTATION
    )
    return training_config