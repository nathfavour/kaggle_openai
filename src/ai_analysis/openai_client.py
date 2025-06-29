import openai
from typing import List, Dict, Any
import base64
import json
from ..config import Config

class OpenAIAnalyzer:
    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY
        self.client = openai.OpenAI()
    
    def analyze_satellite_image(self, image_path: str, context: str = "") -> Dict[str, Any]:
        """Analyze satellite imagery for archaeological features"""
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        
        prompt = f"""
        You are an expert archaeologist analyzing satellite imagery of the Amazon rainforest. 
        Look for potential archaeological features such as:
        - Geometric patterns in vegetation
        - Unusual linear or circular formations
        - Evidence of ancient settlements or earthworks
        - Patterns that differ from natural forest formations
        
        Context: {context}
        
        Provide a detailed analysis including:
        1. Identified features and their coordinates
        2. Confidence level (1-10)
        3. Reasoning for identification
        4. Recommended follow-up analysis
        """
        
        response = self.client.chat.completions.create(
            model=Config.OPENAI_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=Config.MAX_TOKENS,
            temperature=Config.TEMPERATURE
        )
        
        return {
            "analysis": response.choices[0].message.content,
            "model": Config.OPENAI_MODEL,
            "image_path": image_path
        }
    
    def analyze_historical_document(self, document_text: str) -> Dict[str, Any]:
        """Analyze historical documents for archaeological clues"""
        prompt = f"""
        As an expert archaeologist and historian, analyze this historical document for:
        1. Geographic references to unknown settlements
        2. Descriptions of ancient structures or earthworks
        3. Indigenous place names and their potential locations
        4. References to "lost cities" or archaeological sites
        
        Document text: {document_text}
        
        Extract and summarize any archaeological significance.
        """
        
        response = self.client.chat.completions.create(
            model=Config.OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=Config.MAX_TOKENS,
            temperature=Config.TEMPERATURE
        )
        
        return {
            "analysis": response.choices[0].message.content,
            "model": Config.OPENAI_MODEL
        }
