"""Clay render 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ClayRenderHandler(BaseThemeHandler):
    """Handler for clay render 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate clay render 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("clay_render.subjects", "clay sculpture")
        
        view = self._get_random_choice("clay_render.view_types", "3D clay model")
        
        components["subject"] = (
            f"((clay render 3D)) {subject}, "
            f"{view}, matte clay material"
        )
        
        if include_environment:
            lighting = self._get_random_choice("clay_render.lighting", "soft studio light")
            components["environment"] = f"{lighting}, clean studio setup"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("clay_render.styles", "grey clay aesthetic")
            components["style"] = f"{style}, no texture, pure form, sculptural beauty"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "matte grey material, ambient occlusion, soft shadows"
        else:
            components["effects"] = ""
        
        return components
