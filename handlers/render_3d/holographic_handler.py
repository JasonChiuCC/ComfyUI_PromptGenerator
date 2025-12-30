import random
from ...base_handler import BaseThemeHandler

class HolographicHandler(BaseThemeHandler):
    """Handler for Holographic effect render style"""
    
    def get_theme_name(self) -> str:
        return "holographic"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["hologram"]))
        style = random.choice(config.get("styles", ["holographic effect"]))
        environment = random.choice(config.get("environments", ["dark futuristic room"]))
        lighting = random.choice(config.get("lighting", ["hologram glow"]))
        composition = random.choice(config.get("composition_types", ["floating hologram"]))
        effect = random.choice(config.get("effects", ["scan lines"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{effect}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "holographic, hologram projection, sci-fi",
            "futuristic display, glowing, cyan and magenta, cyberpunk"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "solid, opaque, realistic, non-glowing, daytime, bright background, vintage"

