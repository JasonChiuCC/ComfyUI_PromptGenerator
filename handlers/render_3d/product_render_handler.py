"""Product render 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ProductRenderHandler(BaseThemeHandler):
    """Handler for product render 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate product render 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("product_render.subjects", "product")
        
        composition = self._get_random_choice("product_render.composition_types", "hero shot")
        
        components["subject"] = (
            f"((product render 3D)) {subject}, "
            f"{composition}, commercial quality"
        )
        
        if include_environment:
            background = self._get_random_choice("product_render.backgrounds", "clean white")
            lighting = self._get_random_choice("product_render.lighting", "studio three-point")
            components["environment"] = f"on {background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("product_render.styles", "commercial product")
            components["style"] = f"{style}, advertising quality, e-commerce ready"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "perfect reflections, clean shadows, sharp focus, 8K detail"
        else:
            components["effects"] = ""
        
        return components
