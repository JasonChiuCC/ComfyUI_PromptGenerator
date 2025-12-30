import random
from ...base_handler import BaseThemeHandler

class BlueHourHandler(BaseThemeHandler):
    """Handler for Blue Hour photography style"""
    
    def get_theme_name(self) -> str:
        return "blue_hour"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["twilight cityscape"]))
        style = random.choice(config.get("styles", ["blue hour photography"]))
        lighting = random.choice(config.get("lighting", ["deep blue sky"]))
        color = random.choice(config.get("colors", ["deep blue tones"]))
        shot_type = random.choice(config.get("shot_types", ["cityscape panorama"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{shot_type}",
            f"{lighting}",
            f"{color}",
            "blue hour, twilight, dusk",
            "cool tones, city lights, serene, magical"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "midday, harsh sun, warm tones, orange, daytime"





