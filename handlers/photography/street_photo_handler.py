import random
from ...base_handler import BaseThemeHandler

class StreetPhotoHandler(BaseThemeHandler):
    """Handler for Street photography style"""
    
    def get_theme_name(self) -> str:
        return "street_photo"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["street scene"]))
        style = random.choice(config.get("styles", ["street photography"]))
        lighting = random.choice(config.get("lighting", ["natural available light"]))
        environment = random.choice(config.get("environments", ["urban street"]))
        shot_type = random.choice(config.get("shot_types", ["candid moment"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{shot_type}",
            f"{environment}",
            f"{lighting}",
            "street photography, candid, documentary",
            "authentic moment, urban life, 35mm"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "posed, studio, artificial, staged, over-edited, HDR"






