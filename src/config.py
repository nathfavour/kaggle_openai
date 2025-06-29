import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    PLANET_API_KEY = os.getenv('PLANET_API_KEY')
    NASA_API_KEY = os.getenv('NASA_API_KEY')
    
    # Project settings
    PROJECT_NAME = os.getenv('PROJECT_NAME', 'openai_to_z_challenge')
    DATA_DIR = 'data'
    OUTPUT_DIR = 'outputs'
    
    # Study area (Amazon region)
    STUDY_BOUNDS = {
        'west': -74.0,
        'south': -10.0, 
        'east': -50.0,
        'north': 5.0
    }
    
    # OpenAI model settings
    OPENAI_MODEL = 'gpt-4'  # Update to o3/o4 mini when available
    MAX_TOKENS = 4000
    TEMPERATURE = 0.3
