import random
from ...base_handler import BaseThemeHandler

class BlackWhiteHandler(BaseThemeHandler):
    """Handler for Black and White photography style"""
    
    def get_theme_name(self) -> str:
        return "black_white"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["B&W portrait"]))
        style = random.choice(config.get("styles", ["black and white photography"]))
        lighting = random.choice(config.get("lighting", ["dramatic side light"]))
        tone = random.choice(config.get("tones", ["deep blacks"]))
        composition = random.choice(config.get("composition_types", ["high contrast portrait"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{lighting}",
            f"{tone}",
            "black and white, monochrome, B&W",
            "fine art photography, timeless, classic"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "color, colorful, saturated, warm tones, cool tones"





