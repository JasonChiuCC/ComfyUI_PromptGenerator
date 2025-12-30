"""Illumination Entertainment animation theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class IlluminationHandler(BaseThemeHandler):
    """Handler for Illumination Entertainment animation style prompt generation.
    
    Generates prompts inspired by Illumination's style (Despicable Me, Minions,
    Sing, Secret Life of Pets), featuring bright colors, cute characters,
    and comedic expressions.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Illumination style prompt components."""
        components = {}
        
        # Generate character/subject
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("illumination.characters", "cute animated character")
        
        trait = self._get_random_choice("illumination.character_traits", "adorable personality")
        expression = self._get_random_choice("illumination.expressions", "funny expression")
        shot_type = self._get_random_choice("illumination.shot_types", "full body character shot")
        
        components["subject"] = (
            f"((Illumination Entertainment style)) {character}, "
            f"{shot_type}, {trait}, {expression}, "
            f"cute 3D character, appealing cartoon design"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("illumination.locations", "colorful setting")
            
            components["environment"] = (
                f"in {location}, "
                f"bright colorful world, "
                f"Illumination movie setting"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            style = self._get_random_choice("illumination.styles", "Illumination 3D")
            mood = self._get_random_choice("illumination.moods", "family fun")
            
            components["style"] = (
                f"{style}, {mood}, "
                f"Illumination Entertainment quality, "
                f"vibrant saturated colors, "
                f"family animated movie"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            lighting = self._get_random_choice("illumination.lighting", "bright lighting")
            effect = self._get_random_choice("illumination.effects", "colorful effects")
            
            components["effects"] = (
                f"{lighting}, {effect}, "
                f"cheerful atmosphere, "
                f"polished 3D render"
            )
        else:
            components["effects"] = ""
        
        return components

