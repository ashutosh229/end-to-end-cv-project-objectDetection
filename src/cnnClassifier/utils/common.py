import os 
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
  """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
  try:
      with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file);
        logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
  except BoxValueError:
      raise ValueError("yaml file is empty")
  except Exception as error:
    raise error
  
@ensure_annotations
def create_directories(path_to_dirs: list,verbose=True):
  """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
  """
  for path in path_to_dirs:
    os.makedirs(path,exist_ok=True)
    if verbose:
      logger.info(f"Created directory at: {path}")
      
@ensure_annotations
def save_json(path:Path,data:dict):
  """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
  """
  with open(path,"w") as writer:
    json.dump(data,writer,indent=4)
  logger.info(f"Json file is dumped at: {path}")

@ensure_annotations
def load_json(path:Path)->ConfigBox:
  """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
  """
  with open(path) as reader:
    content = json.load(reader)
  logger.info(f"Json file is loaded successfully from: {path}")
  content = ConfigBox(content)
  return content

@ensure_annotations
def save_bin(data:Any,path:Path):
  """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
  """
  joblib.dump(value=data,filename=path)
  logger.info(f"Binary file is saved at: {path}")
  
@ensure_annotations
def load_bin(path:Path)->Any:
 """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
 """ 
 content = joblib.load(path)
 logger.info(f"Binary file is loaded from: {path}")
 return content

@ensure_annotations
def get_size(path:Path)->str:
  """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
  """
  size = round(os.path.getsize(path)/1024)
  return f"~{size} KB"

def decodeImage(imgstring,fileName):
  imgdata = base64.b64decode(imgstring)
  with open(fileName,"wb") as writer:
    writer.write(imgdata)
    writer.close()
  
def encodeImage(croppedImagePath):
  with open(croppedImagePath,"rb") as reader:
    content = reader.read()
    encodedContent = base64.b64encode(content)
    return encodedContent
  
    
      
    
    
  