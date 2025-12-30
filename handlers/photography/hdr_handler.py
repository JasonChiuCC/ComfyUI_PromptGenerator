import random
from ...base_handler import BaseThemeHandler

class HDRHandler(BaseThemeHandler):
    """Handler for HDR photography style"""
    
    def get_theme_name(self) -> str:
        return "hdr"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["HDR scene"]))
        style = random.choice(config.get("styles", ["HDR photography"]))
        lighting = random.choice(config.get("lighting", ["high contrast scene"]))
        effect = random.choice(config.get("effects", ["enhanced details"]))
        composition = random.choice(config.get("composition_types", ["wide landscape"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{lighting}",
            f"{effect}",
            "HDR, high dynamic range, tone mapped",
            "dramatic, enhanced details, vivid colors"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "flat, low contrast, washed out, single exposure, dull"






