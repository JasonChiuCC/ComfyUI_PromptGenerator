import random
from ...base_handler import BaseThemeHandler

class ArchVizHandler(BaseThemeHandler):
    """Handler for Architectural Visualization render style"""
    
    def get_theme_name(self) -> str:
        return "arch_viz"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["modern building"]))
        style = random.choice(config.get("styles", ["architectural visualization"]))
        environment = random.choice(config.get("environments", ["realistic context"]))
        lighting = random.choice(config.get("lighting", ["natural daylight"]))
        view_type = random.choice(config.get("view_types", ["exterior front view"]))
        detail = random.choice(config.get("details", ["furniture and decor"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{view_type}",
            f"{detail}",
            f"{lighting}",
            f"{environment}",
            "architectural visualization, arch viz, photorealistic",
            "V-Ray quality, Corona render, real estate visualization, 8K"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "cartoon, stylized, low quality, blurry, unrealistic, sketch, blueprint only"

