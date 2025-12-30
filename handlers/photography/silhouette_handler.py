"""Silhouette photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SilhouetteHandler(BaseThemeHandler):
    """Handler for silhouette photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate silhouette photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("silhouette.subjects", "person silhouette")
        
        composition = self._get_random_choice("silhouette.composition_types", "dramatic backlit")
        
        components["subject"] = (
            f"((silhouette photography)) {subject}, "
            f"{composition}, strong contrast"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("silhouette.locations", "sunset horizon")
            components["environment"] = f"against {location}, dramatic backdrop"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("silhouette.styles", "artistic silhouette")
            components["style"] = f"{style}, high contrast, minimalist drama"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "backlit silhouette, dramatic contrast, bold shapes"
        else:
            components["effects"] = ""
        
        return components
