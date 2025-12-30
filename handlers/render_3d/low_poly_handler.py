"""Low poly 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class LowPolyHandler(BaseThemeHandler):
    """Handler for low poly 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate low poly 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("low_poly.subjects", "low poly animal")
        
        composition = self._get_random_choice("low_poly.composition_types", "geometric form")
        
        components["subject"] = (
            f"((low poly 3D art)) {subject}, "
            f"{composition}, faceted geometric design"
        )
        
        if include_environment:
            scene = self._get_random_choice("low_poly.scenes", "stylized environment")
            components["environment"] = f"in {scene}, minimal polygons"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("low_poly.styles", "geometric art")
            components["style"] = f"{style}, flat shaded, triangular facets, modern 3D"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "clean geometry, sharp edges, stylized polygons"
        else:
            components["effects"] = ""
        
        return components
