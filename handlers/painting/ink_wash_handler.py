"""Ink Wash style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class InkWashHandler(BaseThemeHandler):
    """Handler for ink wash painting style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate ink wash painting prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("ink_wash.subjects", "misty mountains")
        
        composition = self._get_random_choice("ink_wash.composition_types", "mountain landscape")
        technique = self._get_random_choice("ink_wash.techniques", "wet brush")
        ink_tone = self._get_random_choice("ink_wash.ink_tones", "varied gradation")
        
        components["subject"] = (
            f"((ink wash painting)), {subject}, "
            f"{composition}, {technique}, {ink_tone}"
        )
        
        if include_environment:
            tradition = self._get_random_choice("ink_wash.traditions", "Chinese shuimo")
            mood = self._get_random_choice("ink_wash.moods", "contemplative serenity")
            
            components["environment"] = (
                f"{tradition} style, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"traditional Asian ink painting, sumi-e style, "
                f"Eastern brush art, museum quality"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"flowing ink, rice paper texture, "
                f"atmospheric depth, Zen aesthetic"
            )
        else:
            components["effects"] = ""
        
        return components





