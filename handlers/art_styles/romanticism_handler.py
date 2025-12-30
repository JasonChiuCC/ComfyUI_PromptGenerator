"""Romanticism art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class RomanticismHandler(BaseThemeHandler):
    """Handler for Romanticism art style prompt generation.
    
    Generates prompts for Romantic artwork with sublime nature,
    dramatic emotion, and heroic themes.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Romanticism prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("romanticism.subjects", "stormy landscape")
        
        composition = self._get_random_choice("romanticism.composition_types", "sublime landscape")
        element = self._get_random_choice("romanticism.elements", "turbulent nature")
        theme = self._get_random_choice("romanticism.themes", "nature's power")
        
        components["subject"] = (
            f"((Romantic masterpiece)), {subject}, "
            f"{composition}, {element}, {theme}"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                mood = self._get_random_choice("romanticism.moods", "sublime awe")
            
            components["environment"] = (
                f"{mood}, dramatic atmosphere, "
                f"wild nature, emotional intensity"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("romanticism.influences", "Turner storms")
            
            components["style"] = (
                f"{influence}, 19th century Romanticism, "
                f"museum masterpiece, "
                f"dramatic landscape painting"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"dramatic lighting, atmospheric effects, "
                f"sublime grandeur, oil painting texture, "
                f"emotional color palette"
            )
        else:
            components["effects"] = ""
        
        return components

