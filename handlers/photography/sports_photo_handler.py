import random
from ...base_handler import BaseThemeHandler

class SportsPhotoHandler(BaseThemeHandler):
    """Handler for Sports Photography style"""
    
    def get_theme_name(self) -> str:
        return "sports_photo"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["athlete action"]))
        style = random.choice(config.get("styles", ["sports photography"]))
        lighting = random.choice(config.get("lighting", ["stadium lights"]))
        effect = random.choice(config.get("effects", ["frozen motion"]))
        shot_type = random.choice(config.get("shot_types", ["peak action moment"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{shot_type}",
            f"{lighting}",
            f"{effect}",
            "sports photography, action shot, dynamic",
            "high speed, peak moment, athletic"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "static, posed, motion blur, out of focus, slow shutter"





