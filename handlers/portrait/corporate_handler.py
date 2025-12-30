"""Corporate Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CorporateHandler(BaseThemeHandler):
    """Handler for Corporate portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate corporate portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("corporate.subjects", "business professional")
        
        expression = self._get_random_choice("corporate.expressions", "confident smile")
        pose = self._get_random_choice("corporate.poses", "professional stance")
        outfit = self._get_random_choice("corporate.outfits", "business attire")
        shot_type = self._get_random_choice("corporate.shot_types", "professional headshot")
        
        components["subject"] = (
            f"((corporate headshot)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            background = self._get_random_choice("corporate.backgrounds", "neutral office")
            lighting = self._get_random_choice("corporate.lighting", "professional studio")
            components["environment"] = f"{background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("corporate.styles", "corporate photography")
            components["style"] = f"{style}, LinkedIn quality, professional, clean"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "executive presence, trustworthy, approachable"
        else:
            components["effects"] = ""
        
        return components
