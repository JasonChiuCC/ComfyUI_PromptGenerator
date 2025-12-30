import random
from ...base_handler import BaseThemeHandler

class FoodPhotoHandler(BaseThemeHandler):
    """Handler for Food Photography style"""
    
    def get_theme_name(self) -> str:
        return "food_photo"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["gourmet dish"]))
        style = random.choice(config.get("styles", ["food photography"]))
        lighting = random.choice(config.get("lighting", ["soft natural window"]))
        prop = random.choice(config.get("props", ["rustic wooden board"]))
        composition = random.choice(config.get("composition_types", ["overhead flat lay"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{lighting}",
            f"{prop}",
            "food photography, culinary art, delicious",
            "appetizing, restaurant quality, food styling"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "unappetizing, messy, bad lighting, amateur, unappetizing colors"






