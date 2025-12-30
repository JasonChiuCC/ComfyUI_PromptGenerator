import random
from ...base_handler import BaseThemeHandler

class UnrealEngineHandler(BaseThemeHandler):
    """Handler for Unreal Engine photorealistic game render style"""
    
    def get_theme_name(self) -> str:
        return "unreal_engine"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["game scene"]))
        style = random.choice(config.get("styles", ["Unreal Engine 5 render"]))
        environment = random.choice(config.get("environments", ["detailed open world"]))
        lighting = random.choice(config.get("lighting", ["ray traced global illumination"]))
        composition = random.choice(config.get("composition_types", ["cinematic wide shot"]))
        effect = random.choice(config.get("effects", ["depth of field"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{environment}",
            f"{composition}",
            f"{lighting}",
            f"{effect}",
            "Unreal Engine 5, UE5, photorealistic game graphics",
            "ray tracing, lumen, nanite, AAA game quality, 8K"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "low poly, cartoon, stylized, 2D, pixel art, low resolution, mobile game graphics"

