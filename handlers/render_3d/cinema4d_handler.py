"""Cinema 4D 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class Cinema4DHandler(BaseThemeHandler):
    """Handler for Cinema 4D 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Cinema 4D 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("cinema4d.subjects", "abstract 3D")
        
        composition = self._get_random_choice("cinema4d.composition_types", "motion graphics")
        
        components["subject"] = (
            f"((Cinema 4D render)) {subject}, "
            f"{composition}, professional 3D design"
        )
        
        if include_environment:
            scene = self._get_random_choice("cinema4d.scenes", "studio setup")
            components["environment"] = f"in {scene}, clean backdrop"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("cinema4d.styles", "C4D aesthetic")
            components["style"] = f"{style}, Redshift render, motion design quality"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "smooth geometry, dynamic simulation, professional lighting"
        else:
            components["effects"] = ""
        
        return components
