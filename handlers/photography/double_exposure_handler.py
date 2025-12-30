import random
from ...base_handler import BaseThemeHandler

class DoubleExposureHandler(BaseThemeHandler):
    """Handler for Double Exposure photography style"""
    
    def get_theme_name(self) -> str:
        return "double_exposure"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["portrait with nature"]))
        style = random.choice(config.get("styles", ["double exposure"]))
        blend_element = random.choice(config.get("blend_elements", ["forest trees"]))
        technique = random.choice(config.get("techniques", ["silhouette base"]))
        composition = random.choice(config.get("composition_types", ["profile silhouette"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{composition}",
            f"blended with {blend_element}",
            f"{technique}",
            "double exposure, multiple exposure, overlay",
            "surreal, dreamlike, artistic photography"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "single exposure, normal photo, no overlay, simple, plain"





