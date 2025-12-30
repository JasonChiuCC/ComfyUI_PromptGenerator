"""Glass material 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class Glass3DHandler(BaseThemeHandler):
    """Handler for glass material 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate glass material 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("glass_3d.subjects", "glass sculpture")
        
        view = self._get_random_choice("glass_3d.view_types", "close-up render")
        
        components["subject"] = (
            f"((glass material 3D)) {subject}, "
            f"{view}, transparent beauty"
        )
        
        if include_environment:
            lighting = self._get_random_choice("glass_3d.lighting", "studio caustics")
            background = self._get_random_choice("glass_3d.backgrounds", "gradient backdrop")
            components["environment"] = f"{lighting}, {background}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("glass_3d.styles", "crystal clear glass")
            components["style"] = f"{style}, refractive material, Murano glass quality"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "caustics, refraction, transparency, prismatic light"
        else:
            components["effects"] = ""
        
        return components
