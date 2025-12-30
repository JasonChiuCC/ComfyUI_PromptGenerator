import random
from ...base_handler import BaseThemeHandler

class OctaneHandler(BaseThemeHandler):
    """Handler for Octane high-end GPU render style"""
    
    def get_theme_name(self) -> str:
        return "octane"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["3D object"]))
        style = random.choice(config.get("styles", ["Octane render"]))
        environment = random.choice(config.get("environments", ["studio HDRI"]))
        lighting = random.choice(config.get("lighting", ["HDRI environment lighting"]))
        composition = random.choice(config.get("composition_types", ["product hero shot"]))
        material = random.choice(config.get("materials", ["glossy metal"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{material}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "Octane render, photorealistic 3D, ultra high detail",
            "8K, physically based rendering, commercial quality"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "low quality, blurry, noisy, flat lighting, 2D, cartoon, stylized, amateur"

