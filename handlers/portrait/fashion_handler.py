"""Fashion Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FashionHandler(BaseThemeHandler):
    """Handler for Fashion portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate fashion portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("fashion.subjects", "fashion model")
        
        expression = self._get_random_choice("fashion.expressions", "fierce model look")
        pose = self._get_random_choice("fashion.poses", "dynamic fashion pose")
        outfit = self._get_random_choice("fashion.outfits", "haute couture")
        shot_type = self._get_random_choice("fashion.shot_types", "full body fashion")
        
        components["subject"] = (
            f"((high fashion photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            background = self._get_random_choice("fashion.backgrounds", "studio seamless")
            lighting = self._get_random_choice("fashion.lighting", "fashion studio lighting")
            components["environment"] = f"{background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("fashion.styles", "high fashion photography")
            components["style"] = f"{style}, Vogue quality, editorial, luxury fashion"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "designer fashion, runway quality, avant-garde"
        else:
            components["effects"] = ""
        
        return components
