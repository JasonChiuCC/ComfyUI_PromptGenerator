"""Architectural visualization 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ArchVizHandler(BaseThemeHandler):
    """Handler for architectural visualization 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate architectural visualization 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("arch_viz.subjects", "modern building")
        
        view = self._get_random_choice("arch_viz.view_types", "exterior perspective")
        
        components["subject"] = (
            f"((architectural visualization)) {subject}, "
            f"{view}, photorealistic archviz"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("arch_viz.environments", "urban context")
            lighting = self._get_random_choice("arch_viz.lighting", "natural daylight")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("arch_viz.styles", "high-end archviz")
            components["style"] = f"{style}, V-Ray quality, architectural photography style"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "realistic materials, professional lighting, real estate quality"
        else:
            components["effects"] = ""
        
        return components
