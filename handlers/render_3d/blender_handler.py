"""Blender 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BlenderHandler(BaseThemeHandler):
    """Handler for Blender 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Blender 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("blender.subjects", "3D model")
        
        render_type = self._get_random_choice("blender.render_types", "Cycles render")
        
        components["subject"] = (
            f"((Blender 3D render)) {subject}, "
            f"{render_type}, high quality 3D"
        )
        
        if include_environment:
            scene = self._get_random_choice("blender.scenes", "3D environment")
            components["environment"] = f"in {scene}, detailed scene"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("blender.styles", "Blender Cycles")
            components["style"] = f"{style}, path tracing, procedural materials"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "raytraced lighting, volumetrics, ambient occlusion"
        else:
            components["effects"] = ""
        
        return components
