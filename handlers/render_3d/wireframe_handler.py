import random
from ...base_handler import BaseThemeHandler

class WireframeHandler(BaseThemeHandler):
    """Handler for Wireframe 3D visualization style"""
    
    def get_theme_name(self) -> str:
        return "wireframe"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["3D model"]))
        style = random.choice(config.get("styles", ["wireframe render"]))
        environment = random.choice(config.get("environments", ["dark background"]))
        lighting = random.choice(config.get("lighting", ["edge glow lighting"]))
        composition = random.choice(config.get("composition_types", ["three-quarter view"]))
        line_style = random.choice(config.get("line_styles", ["thin white lines"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{line_style}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "wireframe mesh, polygon edges visible, topology",
            "technical visualization, 3D model showcase"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "solid surfaces, filled polygons, textured, colorful, realistic, photographic"

