"""Chibi (Q?? theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ChibiHandler(BaseThemeHandler):
    """Handler for chibi/super-deformed style prompt generation.
    
    Generates prompts for chibi art style, featuring cute
    big-headed characters with simplified, adorable designs.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate chibi style prompt components."""
        components = {}
        
        # Generate character/subject
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("chibi.characters", "chibi character")
        
        proportion = self._get_random_choice("chibi.proportions", "chibi proportions")
        expression = self._get_random_choice("chibi.expressions", "kawaii expression")
        pose = self._get_random_choice("chibi.poses", "cute pose")
        accessory = self._get_random_choice("chibi.accessories", "cute accessory")
        shot_type = self._get_random_choice("chibi.shot_types", "full chibi body shot")
        
        components["subject"] = (
            f"((chibi style)) {character}, "
            f"{shot_type}, {proportion}, {expression}, {pose}, "
            f"with {accessory}, super deformed, kawaii"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                background = custom_location
            else:
                background = self._get_random_choice("chibi.backgrounds", "cute background")
            
            components["environment"] = (
                f"{background}, cute setting"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            colors = self._get_random_choice("chibi.color_palettes", "pastel colors")
            
            components["style"] = (
                f"{colors}, "
                f"chibi art style, cute illustration, "
                f"clean lineart, soft shading, "
                f"kawaii aesthetic"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"sparkle effects, heart symbols, "
                f"cute atmosphere, adorable finish"
            )
        else:
            components["effects"] = ""
        
        return components

