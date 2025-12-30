"""Octane Render 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class OctaneHandler(BaseThemeHandler):
    """Handler for Octane Render 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Octane Render 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("octane.subjects", "3D render subject")
        
        shot = self._get_random_choice("octane.shot_types", "beauty render")
        
        components["subject"] = (
            f"((Octane Render)) {subject}, "
            f"{shot}, photorealistic quality"
        )
        
        if include_environment:
            lighting = self._get_random_choice("octane.lighting", "HDRI lighting")
            components["environment"] = f"{lighting}, studio environment"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("octane.styles", "photorealistic render")
            components["style"] = f"{style}, path tracing, physically based materials"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "ray tracing, realistic materials, subsurface scattering, 8K"
        else:
            components["effects"] = ""
        
        return components
