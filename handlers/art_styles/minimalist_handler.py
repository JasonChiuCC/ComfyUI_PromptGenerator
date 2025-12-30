"""Minimalist art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MinimalistHandler(BaseThemeHandler):
    """Handler for minimalist art style prompt generation.
    
    Generates prompts for minimalist artwork with emphasis on
    simplicity, negative space, and essential elements.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate minimalist prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("minimalist.subjects", "simple geometric shape")
        
        composition = self._get_random_choice("minimalist.composition_types", "centered composition")
        principle = self._get_random_choice("minimalist.principles", "less is more")
        color_palette = self._get_random_choice("minimalist.color_palettes", "monochrome")
        
        components["subject"] = (
            f"((minimalist art)), {subject}, "
            f"{composition}, {principle}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            style = self._get_random_choice("minimalist.styles", "modern minimalism")
            
            components["environment"] = (
                f"{style}, vast negative space, "
                f"purposeful emptiness, clean design"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            mood = self._get_random_choice("minimalist.moods", "serene calm")
            
            components["style"] = (
                f"{mood}, refined aesthetic, "
                f"elegant simplicity, sophisticated design, "
                f"museum quality minimalism"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"ultra clean rendering, "
                f"perfect geometry, crisp edges, "
                f"high resolution, pristine quality"
            )
        else:
            components["effects"] = ""
        
        return components

