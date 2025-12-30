import random
from ...base_handler import BaseThemeHandler

class StudioPhotoHandler(BaseThemeHandler):
    """Handler for Studio photography style"""
    
    def get_theme_name(self) -> str:
        return "studio_photo"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["studio portrait"]))
        style = random.choice(config.get("styles", ["studio photography"]))
        lighting = random.choice(config.get("lighting", ["three-point lighting"]))
        background = random.choice(config.get("backgrounds", ["seamless white"]))
        shot_type = random.choice(config.get("shot_types", ["portrait shot"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{shot_type}",
            f"{lighting}",
            f"{background} background",
            "professional studio, commercial quality",
            "sharp focus, high resolution, 8K"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "outdoor, natural light only, messy background, amateur, blurry"






