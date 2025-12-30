"""Fauvism art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FauvismHandler(BaseThemeHandler):
    """Handler for Fauvism art style prompt generation.
    
    Generates prompts for Fauvist artwork with wild colors,
    bold brushstrokes, and expressive freedom.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Fauvism prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("fauvism.subjects", "vibrant landscape")
        
        composition = self._get_random_choice("fauvism.composition_types", "bold landscape view")
        element = self._get_random_choice("fauvism.elements", "wild color")
        color_palette = self._get_random_choice("fauvism.color_palettes", "explosive warm colors")
        
        components["subject"] = (
            f"((Fauvist masterpiece)), {subject}, "
            f"{composition}, {element}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("fauvism.moods", "joyful explosion")
            
            components["environment"] = (
                f"{mood}, vibrant atmosphere, "
                f"color liberation, wild freedom"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("fauvism.influences", "Matisse master")
            
            components["style"] = (
                f"{influence}, les Fauves movement, "
                f"wild beast style, museum quality, "
                f"early modern masterpiece"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"bold brushstrokes, pure pigments, "
                f"non-naturalistic color, "
                f"simplified forms, emotional intensity"
            )
        else:
            components["effects"] = ""
        
        return components

