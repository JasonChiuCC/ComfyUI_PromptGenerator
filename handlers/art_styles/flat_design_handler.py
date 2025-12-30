"""Flat Design style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FlatDesignHandler(BaseThemeHandler):
    """Handler for Flat Design style prompt generation.
    
    Generates prompts for flat design artwork with clean lines,
    solid colors, and modern minimalist aesthetic.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Flat Design prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("flat_design.subjects", "geometric character")
        
        composition = self._get_random_choice("flat_design.composition_types", "centered icon layout")
        element = self._get_random_choice("flat_design.elements", "geometric shapes")
        color_palette = self._get_random_choice("flat_design.color_palettes", "material design colors")
        
        components["subject"] = (
            f"((flat design illustration)), {subject}, "
            f"{composition}, {element}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("flat_design.moods", "modern clean")
            
            components["environment"] = (
                f"{mood}, minimal background, "
                f"negative space, clean layout"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            technique = self._get_random_choice("flat_design.techniques", "vector illustration")
            
            components["style"] = (
                f"{technique}, UI/UX design style, "
                f"modern digital illustration, "
                f"professional graphic design"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"no gradients, solid colors, "
                f"clean edges, simple shadows, "
                f"crisp vector quality"
            )
        else:
            components["effects"] = ""
        
        return components

