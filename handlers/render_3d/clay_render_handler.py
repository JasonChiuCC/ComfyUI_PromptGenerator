import random
from ...base_handler import BaseThemeHandler

class ClayRenderHandler(BaseThemeHandler):
    """Handler for Clay Render 3D style"""
    
    def get_theme_name(self) -> str:
        return "clay_render"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["clay model"]))
        style = random.choice(config.get("styles", ["clay render"]))
        environment = random.choice(config.get("environments", ["studio backdrop"]))
        lighting = random.choice(config.get("lighting", ["soft studio lighting"]))
        composition = random.choice(config.get("composition_types", ["product shot angle"]))
        material = random.choice(config.get("materials", ["white clay"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{material}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "clay render, matte material, sculpted 3D",
            "ambient occlusion, soft shadows, studio quality"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "shiny, glossy, textured, colorful, realistic skin, metallic, reflective"

