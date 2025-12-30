import random
from ...base_handler import BaseThemeHandler

class ProductRenderHandler(BaseThemeHandler):
    """Handler for commercial product visualization render style"""
    
    def get_theme_name(self) -> str:
        return "product_render"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["product"]))
        style = random.choice(config.get("styles", ["product visualization"]))
        environment = random.choice(config.get("environments", ["white infinity curve"]))
        lighting = random.choice(config.get("lighting", ["soft studio lighting"]))
        composition = random.choice(config.get("composition_types", ["hero product shot"]))
        material = random.choice(config.get("materials", ["glossy plastic"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{material}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "product render, commercial 3D, advertising quality",
            "photorealistic, e-commerce, catalog shot, 8K"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "low quality, blurry, noisy, dark, amateur, messy background, dirty"

