"""Bauhaus art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BauhausHandler(BaseThemeHandler):
    """Handler for Bauhaus art style prompt generation.
    
    Generates prompts for Bauhaus artwork with geometric forms,
    primary colors, and functional design.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Bauhaus prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("bauhaus.subjects", "geometric abstraction")
        
        composition = self._get_random_choice("bauhaus.composition_types", "geometric grid")
        element = self._get_random_choice("bauhaus.elements", "primary shapes")
        color_palette = self._get_random_choice("bauhaus.color_palettes", "red yellow blue")
        
        components["subject"] = (
            f"((Bauhaus masterpiece)), {subject}, "
            f"{composition}, {element}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("bauhaus.moods", "functional clarity")
            
            components["environment"] = (
                f"{mood}, unified design, "
                f"form follows function, rational order"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("bauhaus.influences", "Kandinsky abstract")
            
            components["style"] = (
                f"{influence}, Weimar Bauhaus school, "
                f"German modernism, museum quality, "
                f"design school masterpiece"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"clean lines, geometric precision, "
                f"primary colors, bold typography, "
                f"industrial aesthetic, modular design"
            )
        else:
            components["effects"] = ""
        
        return components

