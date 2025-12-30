"""AI Dystopia theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class AIDystopiaHandler(BaseThemeHandler):
    """Handler for AI dystopia aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate AI dystopia prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("ai_dystopia.subjects", "AI overlord")
        
        composition = self._get_random_choice("ai_dystopia.composition_types", "oppression scene")
        
        components["subject"] = (
            f"((AI dystopia art)) of {subject}, "
            f"{composition}, machine domination aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("ai_dystopia.environments", "machine city")
            lighting = self._get_random_choice("ai_dystopia.lighting", "cold digital blue")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("ai_dystopia.styles", "Matrix inspired")
            components["style"] = f"{style}, machine nightmare, tech horror"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("ai_dystopia.effects", "digital code rain")
            components["effects"] = f"{effect}, scanning beams, digital oppression"
        else:
            components["effects"] = ""
        
        return components





