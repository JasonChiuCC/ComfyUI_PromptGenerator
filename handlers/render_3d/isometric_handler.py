import random
from ...base_handler import BaseThemeHandler

class IsometricHandler(BaseThemeHandler):
    """Handler for Isometric 3D art style"""
    
    def get_theme_name(self) -> str:
        return "isometric"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["isometric scene"]))
        style = random.choice(config.get("styles", ["isometric view"]))
        environment = random.choice(config.get("environments", ["white background"]))
        lighting = random.choice(config.get("lighting", ["soft ambient lighting"]))
        composition = random.choice(config.get("composition_types", ["centered isometric"]))
        detail = random.choice(config.get("details", ["tiny details"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{detail}",
            f"{lighting}",
            f"{environment}",
            "isometric art, diorama, miniature world",
            "high quality, sharp details, clean render"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "blurry, distorted perspective, messy, low quality, 2D flat, realistic photo"

