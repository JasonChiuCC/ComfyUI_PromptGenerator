"""Maternity Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MaternityHandler(BaseThemeHandler):
    """Handler for Maternity portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate maternity portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("maternity.subjects", "pregnant woman")
        
        expression = self._get_random_choice("maternity.expressions", "radiant maternal glow")
        pose = self._get_random_choice("maternity.poses", "cradling baby bump")
        outfit = self._get_random_choice("maternity.outfits", "flowing maternity dress")
        shot_type = self._get_random_choice("maternity.shot_types", "maternity portrait")
        
        components["subject"] = (
            f"((maternity photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("maternity.locations", "sunlit field")
            lighting = self._get_random_choice("maternity.lighting", "soft golden hour")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("maternity.styles", "maternity photography")
            components["style"] = f"{style}, celebratory, glowing, beautiful motherhood"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "warm tones, soft focus, ethereal mother-to-be"
        else:
            components["effects"] = ""
        
        return components
