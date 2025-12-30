"""Charcoal style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CharcoalHandler(BaseThemeHandler):
    """Handler for charcoal drawing style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate charcoal drawing prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("charcoal.subjects", "expressive portrait")
        
        composition = self._get_random_choice("charcoal.composition_types", "dramatic portrait")
        technique = self._get_random_choice("charcoal.techniques", "broad strokes")
        charcoal_type = self._get_random_choice("charcoal.charcoal_types", "vine charcoal")
        
        components["subject"] = (
            f"((charcoal drawing)), {subject}, "
            f"{composition}, {technique}, using {charcoal_type}"
        )
        
        if include_environment:
            effect = self._get_random_choice("charcoal.effects", "dramatic contrast")
            mood = self._get_random_choice("charcoal.moods", "expressive depth")
            
            components["environment"] = (
                f"{effect}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"traditional charcoal artwork, expressive drawing, "
                f"fine art quality, gallery exhibition piece"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"deep blacks, rich mid-tones, "
                f"velvety texture, dramatic lighting"
            )
        else:
            components["effects"] = ""
        
        return components






