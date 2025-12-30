import random
from ...base_handler import BaseThemeHandler

class LowPolyHandler(BaseThemeHandler):
    """Handler for Low Poly 3D art style"""
    
    def get_theme_name(self) -> str:
        return "low_poly"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["low poly scene"]))
        style = random.choice(config.get("styles", ["low poly art"]))
        environment = random.choice(config.get("environments", ["gradient background"]))
        lighting = random.choice(config.get("lighting", ["flat color lighting"]))
        composition = random.choice(config.get("composition_types", ["front view"]))
        color_palette = random.choice(config.get("color_palettes", ["vibrant colors"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{color_palette}",
            f"{lighting}",
            f"{environment}",
            "low polygon, geometric facets, stylized 3D",
            "clean render, sharp edges"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "high poly, smooth surfaces, realistic, organic curves, photorealistic, blurry"

