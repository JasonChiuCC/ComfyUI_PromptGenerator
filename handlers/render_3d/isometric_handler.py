"""Isometric 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class IsometricHandler(BaseThemeHandler):
    """Handler for isometric 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate isometric 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("isometric.subjects", "isometric building")
        
        view = self._get_random_choice("isometric.view_types", "isometric view")
        
        components["subject"] = (
            f"((isometric 3D art)) {subject}, "
            f"{view}, clean geometric design"
        )
        
        if include_environment:
            scene = self._get_random_choice("isometric.scenes", "miniature world")
            components["environment"] = f"in {scene}, diorama style"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("isometric.styles", "3D isometric")
            components["style"] = f"{style}, clean edges, flat shading, game art style"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "soft shadows, ambient occlusion, miniature aesthetic"
        else:
            components["effects"] = ""
        
        return components
