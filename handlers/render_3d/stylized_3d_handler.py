"""Stylized 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class Stylized3DHandler(BaseThemeHandler):
    """Handler for stylized 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate stylized 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("stylized_3d.subjects", "stylized character")
        
        view = self._get_random_choice("stylized_3d.view_types", "character render")
        
        components["subject"] = (
            f"((stylized 3D art)) {subject}, "
            f"{view}, artistic 3D design"
        )
        
        if include_environment:
            scene = self._get_random_choice("stylized_3d.scenes", "colorful environment")
            components["environment"] = f"in {scene}, vibrant world"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("stylized_3d.styles", "Pixar style")
            components["style"] = f"{style}, exaggerated proportions, appealing design"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "cartoon shading, vibrant colors, charming aesthetic"
        else:
            components["effects"] = ""
        
        return components
