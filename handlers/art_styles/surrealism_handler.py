"""Surrealism art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SurrealismHandler(BaseThemeHandler):
    """Handler for surrealism art style prompt generation.
    
    Generates prompts for surrealist artwork with dreamlike imagery,
    impossible scenarios, and subconscious symbolism.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate surrealism prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("surrealism.subjects", "dreamlike figure")
        
        composition = self._get_random_choice("surrealism.composition_types", "impossible perspective")
        element = self._get_random_choice("surrealism.elements", "floating objects")
        technique = self._get_random_choice("surrealism.techniques", "photorealistic surrealism")
        
        components["subject"] = (
            f"((surrealist masterpiece)), {subject}, "
            f"{composition}, {element}, {technique}"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                mood = self._get_random_choice("surrealism.moods", "dreamlike wonder")
            
            components["environment"] = (
                f"{mood}, impossible landscape, "
                f"subconscious realm, dreamscape atmosphere"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("surrealism.influences", "Dali style")
            
            components["style"] = (
                f"{influence}, museum quality, "
                f"fine art surrealism, gallery worthy, "
                f"metaphysical painting"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"hyperdetailed, oil painting texture, "
                f"dramatic lighting, mysterious atmosphere, "
                f"photorealistic impossible scene"
            )
        else:
            components["effects"] = ""
        
        return components

