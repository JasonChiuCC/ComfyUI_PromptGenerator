"""Unreal Engine 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class UnrealEngineHandler(BaseThemeHandler):
    """Handler for Unreal Engine 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Unreal Engine 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("unreal_engine.subjects", "game character")
        
        shot = self._get_random_choice("unreal_engine.shot_types", "cinematic shot")
        
        components["subject"] = (
            f"((Unreal Engine 5 render)) {subject}, "
            f"{shot}, photorealistic quality"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("unreal_engine.environments", "AAA game environment")
            lighting = self._get_random_choice("unreal_engine.lighting", "Lumen global illumination")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("unreal_engine.styles", "UE5 photorealism")
            components["style"] = f"{style}, Nanite geometry, ray tracing, 8K"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "ray traced reflections, global illumination, subsurface scattering"
        else:
            components["effects"] = ""
        
        return components
