"""Cubism art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CubismHandler(BaseThemeHandler):
    """Handler for Cubism art style prompt generation.
    
    Generates prompts for Cubist artwork with fragmented forms,
    multiple perspectives, and geometric deconstruction.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Cubism prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("cubism.subjects", "fragmented portrait")
        
        composition = self._get_random_choice("cubism.composition_types", "multiple viewpoints")
        element = self._get_random_choice("cubism.elements", "overlapping planes")
        color_palette = self._get_random_choice("cubism.color_palettes", "earthy ochres")
        
        components["subject"] = (
            f"((Cubist masterpiece)), {subject}, "
            f"{composition}, {element}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            phase = self._get_random_choice("cubism.phases", "analytical cubism")
            
            components["environment"] = (
                f"{phase} style, fragmented reality, "
                f"simultaneous perspectives, geometric breakdown"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("cubism.influences", "Picasso style")
            
            components["style"] = (
                f"{influence}, museum quality, "
                f"revolutionary art movement, "
                f"avant-garde masterpiece, gallery exhibition"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"angular facets, interlocking shapes, "
                f"muted earth tones, textured canvas, "
                f"deconstructed forms, multiple angles"
            )
        else:
            components["effects"] = ""
        
        return components

