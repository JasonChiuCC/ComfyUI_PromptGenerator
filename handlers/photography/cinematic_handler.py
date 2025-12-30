import random
from ...base_handler import BaseThemeHandler

class CinematicHandler(BaseThemeHandler):
    """Handler for Cinematic photography style"""
    
    def get_theme_name(self) -> str:
        return "cinematic"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["dramatic scene"]))
        style = random.choice(config.get("styles", ["cinematic photography"]))
        lighting = random.choice(config.get("lighting", ["dramatic lighting"]))
        color_grade = random.choice(config.get("color_grades", ["teal and orange"]))
        shot_type = random.choice(config.get("shot_types", ["wide shot"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{shot_type}",
            f"{lighting}",
            f"{color_grade} color grading",
            "cinematic, movie still, film photography",
            "35mm film, anamorphic, high production value"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "amateur, low quality, smartphone photo, oversaturated, flat lighting"






