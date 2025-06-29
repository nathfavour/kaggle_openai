import os
from dotenv import load_dotenv

# Load environment variables from .env file (local development only)
load_dotenv()

class Config:
    """Configuration for local development environment"""
    
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    PLANET_API_KEY = os.getenv('PLANET_API_KEY')
    NASA_API_KEY = os.getenv('NASA_API_KEY')
    
    # Project settings
    PROJECT_NAME = os.getenv('PROJECT_NAME', 'openai_to_z_challenge')
    DATA_DIR = 'data'
    OUTPUT_DIR = 'outputs'
    
    # Study area (Australia - updated from Amazon)
    STUDY_BOUNDS = {
        'west': 110.0,   # Western Australia
        'south': -45.0,  # Southern Australia
        'east': 155.0,   # Eastern Australia
        'north': -10.0   # Northern Australia
    }
    
    # OpenAI model settings
    OPENAI_MODEL = 'gpt-4'  # Use gpt-4 for local development
    MAX_TOKENS = 4000
    TEMPERATURE = 0.3
    
    # Local development flags
    IS_LOCAL = True
    IS_KAGGLE = False
    
    @classmethod
    def validate_setup(cls):
        """Validate local development setup"""
        missing = []
        if not cls.OPENAI_API_KEY:
            missing.append('OPENAI_API_KEY')
        
        if missing:
            print(f"⚠️  Missing environment variables: {', '.join(missing)}")
            print("💡 Create a .env file with required API keys")
            return False
        return True
