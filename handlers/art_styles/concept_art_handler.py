"""Concept art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ConceptArtHandler(BaseThemeHandler):
    """Handler for concept art style prompt generation.
    
    Generates prompts for professional concept art used in
    games, films, and entertainment design.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate concept art prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("concept_art.subjects", "fantasy character")
        
        composition = self._get_random_choice("concept_art.composition_types", "character design sheet")
        style = self._get_random_choice("concept_art.styles", "painterly concept")
        purpose = self._get_random_choice("concept_art.purposes", "game development")
        
        components["subject"] = (
            f"((professional concept art)), {subject}, "
            f"{composition}, {style}, for {purpose}"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                mood = self._get_random_choice("concept_art.moods", "epic adventure")
            
            components["environment"] = (
                f"{mood} atmosphere, detailed background, "
                f"environmental storytelling"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            technique = self._get_random_choice("concept_art.techniques", "digital painting")
            
            components["style"] = (
                f"{technique}, industry standard quality, "
                f"portfolio piece, production ready, "
                f"professional entertainment art"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"highly detailed, 4k resolution, "
                f"artstation trending, professional lighting, "
                f"cinematic composition"
            )
        else:
            components["effects"] = ""
        
        return components

