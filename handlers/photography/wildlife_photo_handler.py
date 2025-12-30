import random
from ...base_handler import BaseThemeHandler

class WildlifePhotoHandler(BaseThemeHandler):
    """Handler for Wildlife Photography style"""
    
    def get_theme_name(self) -> str:
        return "wildlife_photo"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["wild animal"]))
        style = random.choice(config.get("styles", ["wildlife photography"]))
        lighting = random.choice(config.get("lighting", ["golden hour safari"]))
        environment = random.choice(config.get("environments", ["natural habitat"]))
        shot_type = random.choice(config.get("shot_types", ["intimate portrait"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{shot_type}",
            f"{lighting}",
            f"{environment}",
            "wildlife photography, nature documentary",
            "National Geographic, telephoto lens, stunning"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "zoo, captive, domestic, pet, stuffed, cartoon, illustration"






