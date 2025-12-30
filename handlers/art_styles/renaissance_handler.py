"""Renaissance art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class RenaissanceHandler(BaseThemeHandler):
    """Handler for Renaissance art style prompt generation.
    
    Generates prompts for Renaissance artwork with classical beauty,
    anatomical accuracy, and humanist themes.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Renaissance prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("renaissance.subjects", "religious scene")
        
        composition = self._get_random_choice("renaissance.composition_types", "pyramidal composition")
        element = self._get_random_choice("renaissance.elements", "linear perspective")
        technique = self._get_random_choice("renaissance.techniques", "sfumato")
        
        components["subject"] = (
            f"((Renaissance masterpiece)), {subject}, "
            f"{composition}, {element}, {technique}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("renaissance.moods", "serene beauty")
            
            components["environment"] = (
                f"{mood}, classical architecture, "
                f"harmonious composition, ideal beauty"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("renaissance.influences", "Leonardo mastery")
            
            components["style"] = (
                f"{influence}, museum masterpiece, "
                f"High Renaissance quality, "
                f"old master painting, Uffizi gallery worthy"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"sfumato technique, oil glazing, "
                f"anatomical perfection, "
                f"golden ratio composition, tempera finish"
            )
        else:
            components["effects"] = ""
        
        return components

