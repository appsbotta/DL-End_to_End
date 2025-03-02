import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py"
    "src/pipeline/__init__.py",
    "src/entity/__init__.py"
    "src/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"

]

for file in list_of_files:
    file = Path(file)
    filedir,filename = os.path.split(file)\
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file,"w") as f:
            pass
        logging.info(f"creating empty file:{file}")
    else:
        logging.info(f"{file} already exist")