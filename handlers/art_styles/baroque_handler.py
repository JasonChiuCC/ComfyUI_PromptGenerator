"""Baroque art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BaroqueHandler(BaseThemeHandler):
    """Handler for Baroque art style prompt generation.
    
    Generates prompts for Baroque artwork with dramatic lighting,
    rich colors, and theatrical compositions.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Baroque prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("baroque.subjects", "religious scene")
        
        composition = self._get_random_choice("baroque.composition_types", "dramatic chiaroscuro")
        element = self._get_random_choice("baroque.elements", "rich fabrics")
        technique = self._get_random_choice("baroque.techniques", "chiaroscuro")
        
        components["subject"] = (
            f"((Baroque masterpiece)), {subject}, "
            f"{composition}, {element}, {technique}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("baroque.moods", "dramatic grandeur")
            
            components["environment"] = (
                f"{mood}, theatrical staging, "
                f"divine light, ornate setting"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("baroque.influences", "Caravaggio dramatic")
            
            components["style"] = (
                f"{influence}, museum masterpiece, "
                f"17th century painting, "
                f"old master quality, gallery exhibition"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"dramatic lighting, deep shadows, "
                f"rich color palette, oil painting texture, "
                f"gold ornamentation, tenebrism"
            )
        else:
            components["effects"] = ""
        
        return components

