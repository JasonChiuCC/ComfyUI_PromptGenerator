import random
from ...base_handler import BaseThemeHandler

class DocumentaryHandler(BaseThemeHandler):
    """Handler for Documentary photography style"""
    
    def get_theme_name(self) -> str:
        return "documentary"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["documentary moment"]))
        style = random.choice(config.get("styles", ["documentary photography"]))
        lighting = random.choice(config.get("lighting", ["natural available light"]))
        environment = random.choice(config.get("environments", ["real world setting"]))
        shot_type = random.choice(config.get("shot_types", ["environmental portrait"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{shot_type}",
            f"{environment}",
            f"{lighting}",
            "documentary, photojournalism, authentic",
            "raw emotion, storytelling, unposed"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "posed, artificial, studio, glamorous, over-processed, fake"






