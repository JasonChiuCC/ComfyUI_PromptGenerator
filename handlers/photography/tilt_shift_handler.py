import random
from ...base_handler import BaseThemeHandler

class TiltShiftHandler(BaseThemeHandler):
    """Handler for Tilt Shift photography style"""
    
    def get_theme_name(self) -> str:
        return "tilt_shift"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["city scene"]))
        style = random.choice(config.get("styles", ["tilt-shift photography"]))
        lighting = random.choice(config.get("lighting", ["bright daylight"]))
        environment = random.choice(config.get("environments", ["urban cityscape"]))
        composition = random.choice(config.get("composition_types", ["elevated viewpoint"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "tilt-shift, miniature effect, fake miniature",
            "toy town, diorama look, selective focus"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "normal perspective, eye level, all in focus, realistic scale"






