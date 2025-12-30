"""Street Style Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class StreetStyleHandler(BaseThemeHandler):
    """Handler for Street Style portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate street style portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("street_style.subjects", "street fashion model")
        
        expression = self._get_random_choice("street_style.expressions", "cool confident attitude")
        pose = self._get_random_choice("street_style.poses", "street style stance")
        outfit = self._get_random_choice("street_style.outfits", "trendy streetwear")
        shot_type = self._get_random_choice("street_style.shot_types", "street fashion shot")
        
        components["subject"] = (
            f"((street style photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("street_style.locations", "urban street")
            lighting = self._get_random_choice("street_style.lighting", "natural urban light")
            components["environment"] = f"on {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("street_style.styles", "street style photography")
            components["style"] = f"{style}, urban fashion, trendsetting, authentic"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "street fashion vibe, urban cool, contemporary style"
        else:
            components["effects"] = ""
        
        return components
