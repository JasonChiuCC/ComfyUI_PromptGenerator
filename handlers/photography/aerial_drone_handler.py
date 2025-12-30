import random
from ...base_handler import BaseThemeHandler

class AerialDroneHandler(BaseThemeHandler):
    """Handler for Aerial Drone photography style"""
    
    def get_theme_name(self) -> str:
        return "aerial_drone"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["aerial landscape"]))
        style = random.choice(config.get("styles", ["aerial photography"]))
        lighting = random.choice(config.get("lighting", ["golden hour aerial"]))
        environment = random.choice(config.get("environments", ["landscape"]))
        composition = random.choice(config.get("composition_types", ["straight down top-down"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "aerial photography, drone shot, bird's eye view",
            "DJI quality, high altitude, stunning perspective"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "ground level, eye level, indoor, low altitude, fisheye distortion"






