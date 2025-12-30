"""Pastel style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PastelHandler(BaseThemeHandler):
    """Handler for pastel painting style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate pastel painting prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("pastel.subjects", "gentle portrait")
        
        composition = self._get_random_choice("pastel.composition_types", "soft portrait")
        technique = self._get_random_choice("pastel.techniques", "soft blending")
        pastel_type = self._get_random_choice("pastel.pastel_types", "soft pastels")
        
        components["subject"] = (
            f"((pastel painting)), {subject}, "
            f"{composition}, {technique}, using {pastel_type}"
        )
        
        if include_environment:
            paper = self._get_random_choice("pastel.paper_surfaces", "sanded paper")
            mood = self._get_random_choice("pastel.moods", "soft romance")
            
            components["environment"] = (
                f"on {paper}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"traditional pastel art, soft chalk medium, "
                f"impressionistic quality, fine art finish"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"velvety texture, luminous color, "
                f"soft edges, dreamy atmosphere"
            )
        else:
            components["effects"] = ""
        
        return components





