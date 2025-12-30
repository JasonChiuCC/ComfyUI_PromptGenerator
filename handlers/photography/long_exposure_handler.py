import random
from ...base_handler import BaseThemeHandler

class LongExposureHandler(BaseThemeHandler):
    """Handler for Long Exposure photography style"""
    
    def get_theme_name(self) -> str:
        return "long_exposure"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["light trails"]))
        style = random.choice(config.get("styles", ["long exposure photography"]))
        lighting = random.choice(config.get("lighting", ["city lights"]))
        environment = random.choice(config.get("environments", ["night scene"]))
        composition = random.choice(config.get("composition_types", ["leading lines"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "long exposure, light trails, motion blur",
            "tripod shot, smooth motion, night photography"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "frozen motion, fast shutter, handheld blur, noisy, daylight snapshot"





