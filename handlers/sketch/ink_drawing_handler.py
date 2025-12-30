"""Ink Drawing style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class InkDrawingHandler(BaseThemeHandler):
    """Handler for ink drawing style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate ink drawing prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("ink_drawing.subjects", "detailed illustration")
        
        composition = self._get_random_choice("ink_drawing.composition_types", "detailed illustration")
        technique = self._get_random_choice("ink_drawing.techniques", "fine line work")
        ink_type = self._get_random_choice("ink_drawing.ink_types", "India ink")
        tool = self._get_random_choice("ink_drawing.tools", "dip pen nib")
        
        components["subject"] = (
            f"((ink drawing)), {subject}, "
            f"{composition}, {technique}, using {ink_type} with {tool}"
        )
        
        if include_environment:
            mood = self._get_random_choice("ink_drawing.moods", "precise detail")
            
            components["environment"] = (
                f"{mood}, on quality paper"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"traditional ink illustration, pen and ink artwork, "
                f"fine art quality, professional illustration"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"crisp lines, bold contrast, "
                f"detailed linework, archival quality"
            )
        else:
            components["effects"] = ""
        
        return components





