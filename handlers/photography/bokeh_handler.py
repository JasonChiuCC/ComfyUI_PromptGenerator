import random
from ...base_handler import BaseThemeHandler

class BokehHandler(BaseThemeHandler):
    """Handler for Bokeh photography style"""
    
    def get_theme_name(self) -> str:
        return "bokeh"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["portrait"]))
        style = random.choice(config.get("styles", ["bokeh photography"]))
        lighting = random.choice(config.get("lighting", ["point light sources"]))
        bokeh_type = random.choice(config.get("bokeh_types", ["circular bokeh balls"]))
        shot_type = random.choice(config.get("shot_types", ["portrait close-up"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{shot_type}",
            f"{bokeh_type}",
            f"{lighting}",
            "bokeh, shallow depth of field, f/1.4",
            "creamy background blur, 85mm lens, dreamy"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "deep focus, everything sharp, small aperture, flat background"






