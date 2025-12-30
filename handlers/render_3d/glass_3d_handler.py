import random
from ...base_handler import BaseThemeHandler

class Glass3DHandler(BaseThemeHandler):
    """Handler for Glass Material 3D render style"""
    
    def get_theme_name(self) -> str:
        return "glass_3d"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["glass object"]))
        style = random.choice(config.get("styles", ["glass material render"]))
        environment = random.choice(config.get("environments", ["dark background for contrast"]))
        lighting = random.choice(config.get("lighting", ["backlit for transparency"]))
        composition = random.choice(config.get("composition_types", ["centered showcase"]))
        effect = random.choice(config.get("effects", ["rainbow dispersion"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{effect}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "glass material, transparent 3D, crystal clear",
            "caustics, refraction, high quality render, 8K"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "opaque, solid, matte, low quality, blurry, no transparency, flat"

