import os  # Importing the os module to interact with the operating system
from pathlib import Path  # Importing the Path class from pathlib module for path manipulations

# Define the project name
project_name = "us_visa"

# List of files and directories to create for the project
list_of_files = [
    f"{project_name}/__init__.py",  # Package initializer for the main project directory
    f"{project_name}/components/__init__.py",  # Package initializer for the components directory
    f"{project_name}/components/data_ingestion.py",  # Data ingestion component
    f"{project_name}/components/data_validation.py",  # Data validation component
    f"{project_name}/components/data_transformation.py",  # Data transformation component
    f"{project_name}/components/model_trainer.py",  # Model trainer component
    f"{project_name}/components/model_evaluation.py",  # Model evaluation component
    f"{project_name}/components/model_pusher.py",  # Model pusher component
    f"{project_name}/configuration/__init__.py",  # Package initializer for the configuration directory
    f"{project_name}/constants/__init__.py",  # Package initializer for the constants directory
    f"{project_name}/entity/__init__.py",  # Package initializer for the entity directory
    f"{project_name}/entity/config_entity.py",  # Config entity definitions
    f"{project_name}/entity/artifact_entity.py",  # Artifact entity definitions
    f"{project_name}/exception/__init__.py",  # Package initializer for the exception directory
    f"{project_name}/logger/__init__.py",  # Package initializer for the logger directory
    f"{project_name}/pipline/__init__.py",  # Package initializer for the pipeline directory
    f"{project_name}/pipline/training_pipeline.py",  # Training pipeline script
    f"{project_name}/pipline/prediction_pipeline.py",  # Prediction pipeline script
    f"{project_name}/utils/__init__.py",  # Package initializer for the utils directory
    f"{project_name}/utils/main_utils.py",  # Main utility functions
    "app.py",  # Main application script
    "requirements.txt",  # List of project dependencies
    "Dockerfile",  # Docker configuration file
    ".dockerignore",  # Docker ignore file
    "demo.py",  # Demo script
    "setup.py",  # Setup script for the project
    "config/model.yaml",  # Model configuration file
    "config/schema.yaml",  # Schema configuration file
]

# Loop through the list of files to create them
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the string path to a Path object
    filedir, filename = os.path.split(filepath)  # Split the path into directory and filename
    if filedir != "":  # If the directory part is not empty
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it doesn't exist
    # Check if the file does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Create an empty file
            pass  # No need to write anything, just create the file
    else:
        print(f"file is already present at: {filepath}")  # Print message if file already exists

