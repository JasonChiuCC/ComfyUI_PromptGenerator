"""Double exposure photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DoubleExposureHandler(BaseThemeHandler):
    """Handler for double exposure photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate double exposure photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("double_exposure.subjects", "portrait silhouette")
        
        overlay = self._get_random_choice("double_exposure.overlays", "forest trees")
        
        components["subject"] = (
            f"((double exposure photography)) {subject}, "
            f"merged with {overlay}, artistic blend"
        )
        
        if include_environment:
            components["environment"] = "surreal overlay effect, multiple exposure blend"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("double_exposure.styles", "artistic double exposure")
            components["style"] = f"{style}, film technique, creative composite"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "overlay blend, silhouette fusion, dreamy composite, artistic merge"
        else:
            components["effects"] = ""
        
        return components
