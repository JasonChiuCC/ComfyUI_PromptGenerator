"""Expressionism art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ExpressionismHandler(BaseThemeHandler):
    """Handler for Expressionism art style prompt generation.
    
    Generates prompts for Expressionist artwork with distorted forms,
    emotional intensity, and psychological depth.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Expressionism prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("expressionism.subjects", "anguished figure")
        
        composition = self._get_random_choice("expressionism.composition_types", "distorted perspective")
        element = self._get_random_choice("expressionism.elements", "bold brushstrokes")
        color_palette = self._get_random_choice("expressionism.color_palettes", "intense saturated colors")
        
        components["subject"] = (
            f"((Expressionist masterpiece)), {subject}, "
            f"{composition}, {element}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("expressionism.moods", "raw anguish")
            
            components["environment"] = (
                f"{mood}, emotional intensity, "
                f"psychological tension, inner turmoil"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("expressionism.influences", "Munch style")
            
            components["style"] = (
                f"{influence}, museum quality, "
                f"German Expressionism influence, "
                f"avant-garde movement, gallery masterpiece"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"visible brushwork, distorted forms, "
                f"jarring color contrasts, "
                f"emotional color, raw expression"
            )
        else:
            components["effects"] = ""
        
        return components

