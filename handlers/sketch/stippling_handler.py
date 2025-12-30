"""Stippling style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class StipplingHandler(BaseThemeHandler):
    """Handler for stippling style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate stippling prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("stippling.subjects", "realistic portrait")
        
        composition = self._get_random_choice("stippling.composition_types", "detailed portrait")
        technique = self._get_random_choice("stippling.techniques", "varied density")
        density = self._get_random_choice("stippling.density_levels", "gradient transition")
        
        components["subject"] = (
            f"((stippling art)), {subject}, "
            f"{composition}, {technique}, {density}"
        )
        
        if include_environment:
            tool = self._get_random_choice("stippling.tools", "fine point pen")
            mood = self._get_random_choice("stippling.moods", "meditative patience")
            
            components["environment"] = (
                f"created with {tool}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"pointillism drawing, dot art, "
                f"scientific illustration style, fine art quality"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"thousands of dots, tonal gradation, "
                f"incredible detail, textural richness"
            )
        else:
            components["effects"] = ""
        
        return components





