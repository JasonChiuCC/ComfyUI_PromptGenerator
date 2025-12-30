"""Technical Drawing style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class TechnicalDrawingHandler(BaseThemeHandler):
    """Handler for technical drawing style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate technical drawing prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("technical_drawing.subjects", "mechanical part")
        
        composition = self._get_random_choice("technical_drawing.composition_types", "orthographic projection")
        element = self._get_random_choice("technical_drawing.elements", "precise dimensions")
        standard = self._get_random_choice("technical_drawing.standards", "ISO standard")
        
        components["subject"] = (
            f"((technical drawing)), {subject}, "
            f"{composition}, with {element}, following {standard}"
        )
        
        if include_environment:
            line_type = self._get_random_choice("technical_drawing.line_types", "continuous thick")
            mood = self._get_random_choice("technical_drawing.moods", "engineering precision")
            
            components["environment"] = (
                f"using {line_type} lines, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"engineering diagram, CAD style, "
                f"manufacturing specification, production drawing"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"geometric accuracy, clean linework, "
                f"proper dimensioning, professional quality"
            )
        else:
            components["effects"] = ""
        
        return components






