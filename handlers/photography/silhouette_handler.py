import random
from ...base_handler import BaseThemeHandler

class SilhouetteHandler(BaseThemeHandler):
    """Handler for Silhouette photography style"""
    
    def get_theme_name(self) -> str:
        return "silhouette"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["silhouette figure"]))
        style = random.choice(config.get("styles", ["silhouette photography"]))
        lighting = random.choice(config.get("lighting", ["strong backlight"]))
        background = random.choice(config.get("backgrounds", ["vibrant sunset sky"]))
        composition = random.choice(config.get("composition_types", ["centered figure"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{lighting}",
            f"{background}",
            "silhouette, backlit, dramatic contrast",
            "shadow art, high contrast, stunning sky"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "front lit, fully visible, detailed face, no backlight, flat"






