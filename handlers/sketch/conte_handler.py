"""Conte Crayon style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ConteHandler(BaseThemeHandler):
    """Handler for conte crayon style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate conte crayon prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("conte.subjects", "classical figure")
        
        composition = self._get_random_choice("conte.composition_types", "figure study")
        technique = self._get_random_choice("conte.techniques", "side stroke shading")
        conte_color = self._get_random_choice("conte.conte_colors", "sanguine red")
        
        components["subject"] = (
            f"((conte crayon drawing)), {subject}, "
            f"{composition}, {technique}, in {conte_color}"
        )
        
        if include_environment:
            paper = self._get_random_choice("conte.paper_tones", "warm gray paper")
            mood = self._get_random_choice("conte.moods", "classical elegance")
            
            components["environment"] = (
                f"on {paper}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"French atelier tradition, academic drawing, "
                f"old master technique, fine art quality"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"warm earth tones, sculptural form, "
                f"subtle gradation, Renaissance spirit"
            )
        else:
            components["effects"] = ""
        
        return components






