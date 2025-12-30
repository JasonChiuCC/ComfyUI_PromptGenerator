import random
from ...base_handler import BaseThemeHandler

class MacroHandler(BaseThemeHandler):
    """Handler for Macro photography style"""
    
    def get_theme_name(self) -> str:
        return "macro"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["macro detail"]))
        style = random.choice(config.get("styles", ["macro photography"]))
        lighting = random.choice(config.get("lighting", ["soft diffused"]))
        background = random.choice(config.get("backgrounds", ["smooth bokeh blur"]))
        composition = random.choice(config.get("composition_types", ["centered subject"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{lighting}",
            f"{background}",
            "macro photography, extreme close-up, 1:1 magnification",
            "sharp focus, incredible detail, 100mm macro lens"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "wide angle, blurry subject, low detail, distant, out of focus"






