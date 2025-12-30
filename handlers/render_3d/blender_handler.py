import random
from ...base_handler import BaseThemeHandler

class BlenderHandler(BaseThemeHandler):
    """Handler for Blender 3D artistic render style"""
    
    def get_theme_name(self) -> str:
        return "blender"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["3D scene"]))
        style = random.choice(config.get("styles", ["Blender Cycles render"]))
        environment = random.choice(config.get("environments", ["stylized background"]))
        lighting = random.choice(config.get("lighting", ["Cycles path tracing"]))
        composition = random.choice(config.get("composition_types", ["artistic camera angle"]))
        detail = random.choice(config.get("details", ["procedural textures"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{detail}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "Blender 3D, Cycles render, artistic 3D",
            "procedural materials, high quality render"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "low quality, 2D, flat, sketch, noisy, grainy, unfinished render"

