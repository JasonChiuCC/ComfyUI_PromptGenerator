import random
from ...base_handler import BaseThemeHandler

class GoldenHourHandler(BaseThemeHandler):
    """Handler for Golden Hour photography style"""
    
    def get_theme_name(self) -> str:
        return "golden_hour"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["sunset scene"]))
        style = random.choice(config.get("styles", ["golden hour photography"]))
        lighting = random.choice(config.get("lighting", ["warm orange backlight"]))
        color = random.choice(config.get("colors", ["warm orange tones"]))
        shot_type = random.choice(config.get("shot_types", ["backlit portrait"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{shot_type}",
            f"{lighting}",
            f"{color}",
            "golden hour, magic hour, sunset",
            "warm light, dreamy, romantic, lens flare"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "midday harsh light, overcast, cold tones, blue light, night"






