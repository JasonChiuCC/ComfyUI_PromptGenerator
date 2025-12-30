"""Wireframe 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class WireframeHandler(BaseThemeHandler):
    """Handler for wireframe 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate wireframe 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("wireframe.subjects", "wireframe model")
        
        view = self._get_random_choice("wireframe.view_types", "3D wireframe view")
        
        components["subject"] = (
            f"((wireframe 3D)) {subject}, "
            f"{view}, visible polygon mesh"
        )
        
        if include_environment:
            background = self._get_random_choice("wireframe.backgrounds", "dark background")
            components["environment"] = f"on {background}, technical visualization"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("wireframe.styles", "technical wireframe")
            components["style"] = f"{style}, edge lines visible, mesh topology, 3D modeling"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "glowing edges, mesh structure, polygon lines visible"
        else:
            components["effects"] = ""
        
        return components
