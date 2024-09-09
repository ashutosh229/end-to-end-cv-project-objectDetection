import os 
import zipfile
import gdown
from src.cnnClassifier import logger
from src.cnnClassifier.utils.common import get_size
from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
  def __init__(self,config:DataIngestionConfig):
    self.config = config
  
  def download_file(self)->str:
    try:
      dataset_url = self.config.source_url
      zip_download_dir = self.config.local_data_file
      os.makedirs(f"{self.config.root_dir}",exist_ok=True)
      logger.info(f"Downloading data from {dataset_url} into file: {zip_download_dir}")
      
      file_id = dataset_url.split("/")[-2]
      prefix = 'https://drive.google.com/uc?/export=download&id='
      drive_link = prefix + file_id
      gdown.download(drive_link,zip_download_dir)
      
      logger.info(f"Downloaded data from {dataset_url} into file: {zip_download_dir}")
    except Exception as error:
      raise error
    
  def extract_zip_file(self):
    unzip_path = self.config.unzip_dir
    os.makedirs(unzip_path,exist_ok=True)
    with zipfile.ZipFile(self.config.local_data_file,"r") as reader:
      reader.extractall(unzip_path)
      