import random
from ...base_handler import BaseThemeHandler

class FilmGrainHandler(BaseThemeHandler):
    """Handler for Film Grain photography style"""
    
    def get_theme_name(self) -> str:
        return "film_grain"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["film moment"]))
        style = random.choice(config.get("styles", ["film photography"]))
        film_stock = random.choice(config.get("film_stocks", ["Kodak Portra 400"]))
        characteristic = random.choice(config.get("characteristics", ["visible grain"]))
        shot_type = random.choice(config.get("shot_types", ["candid moment"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{shot_type}",
            f"shot on {film_stock}",
            f"{characteristic}",
            "film photography, 35mm film, analog",
            "film grain, nostalgic, authentic film look"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "digital, clean, noise-free, over-processed, HDR, modern"





