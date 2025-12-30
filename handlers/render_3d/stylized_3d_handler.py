import random
from ...base_handler import BaseThemeHandler

class Stylized3DHandler(BaseThemeHandler):
    """Handler for Stylized cartoon 3D art style"""
    
    def get_theme_name(self) -> str:
        return "stylized_3d"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["cartoon character"]))
        style = random.choice(config.get("styles", ["stylized 3D"]))
        environment = random.choice(config.get("environments", ["colorful fantasy world"]))
        lighting = random.choice(config.get("lighting", ["bright cheerful lighting"]))
        composition = random.choice(config.get("composition_types", ["character showcase"]))
        detail = random.choice(config.get("details", ["exaggerated features"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{detail}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "stylized 3D, cartoon 3D render, Fortnite style",
            "vibrant colors, playful, high quality 3D"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "realistic, photorealistic, dark, gritty, horror, low poly, ugly, deformed"

