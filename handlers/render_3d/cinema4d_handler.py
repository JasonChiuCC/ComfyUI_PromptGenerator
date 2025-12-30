import random
from ...base_handler import BaseThemeHandler

class Cinema4DHandler(BaseThemeHandler):
    """Handler for Cinema 4D motion graphics render style"""
    
    def get_theme_name(self) -> str:
        return "cinema4d"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["abstract 3D"]))
        style = random.choice(config.get("styles", ["Cinema 4D render"]))
        environment = random.choice(config.get("environments", ["infinite backdrop"]))
        lighting = random.choice(config.get("lighting", ["global illumination"]))
        composition = random.choice(config.get("composition_types", ["centered symmetrical"]))
        effect = random.choice(config.get("effects", ["depth of field bokeh"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{effect}",
            f"{lighting}",
            f"{environment}",
            "Cinema 4D, C4D, motion graphics, abstract 3D",
            "Redshift render, commercial quality, smooth modern"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "low quality, 2D, flat design, hand drawn, sketch, rough, amateur"

