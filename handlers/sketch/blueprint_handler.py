"""Blueprint style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BlueprintHandler(BaseThemeHandler):
    """Handler for blueprint style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate blueprint prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("blueprint.subjects", "architectural plan")
        
        composition = self._get_random_choice("blueprint.composition_types", "floor plan")
        element = self._get_random_choice("blueprint.elements", "dimension lines")
        style = self._get_random_choice("blueprint.styles", "traditional cyanotype")
        
        components["subject"] = (
            f"((blueprint)), {subject}, "
            f"{composition}, with {element}, {style}"
        )
        
        if include_environment:
            color = self._get_random_choice("blueprint.color_schemes", "classic blue on white")
            mood = self._get_random_choice("blueprint.moods", "technical precision")
            
            components["environment"] = (
                f"{color}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"technical drawing, engineering diagram, "
                f"architectural rendering, professional drafting"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"precise lines, clear annotations, "
                f"grid pattern, scale accuracy"
            )
        else:
            components["effects"] = ""
        
        return components





