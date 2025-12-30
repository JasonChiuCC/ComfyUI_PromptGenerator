"""Looney Tunes cartoon style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class LooneyTunesHandler(BaseThemeHandler):
    """Handler for Looney Tunes cartoon style prompt generation.
    
    Generates prompts for classic Warner Bros cartoon aesthetic,
    featuring slapstick comedy, exaggerated expressions, and cartoon physics.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Looney Tunes style prompt components."""
        components = {}
        
        # Generate character
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("looney_tunes.characters", "cartoon character")
        
        expression = self._get_random_choice("looney_tunes.expressions", "exaggerated expression")
        action = self._get_random_choice("looney_tunes.actions", "slapstick action")
        prop = self._get_random_choice("looney_tunes.props", "cartoon prop")
        shot_type = self._get_random_choice("looney_tunes.shot_types", "full body cartoon shot")
        
        components["subject"] = (
            f"((classic Looney Tunes cartoon)) of {character}, "
            f"{shot_type}, with {expression}, {action}, holding {prop}, "
            f"exaggerated cartoon proportions, golden age animation"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("looney_tunes.locations", "cartoon background")
            
            components["environment"] = (
                f"in {location}, "
                f"painted backdrop style, "
                f"theatrical short background quality"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            style = self._get_random_choice("looney_tunes.styles", "classic cartoon style")
            
            components["style"] = (
                f"{style}, "
                f"bold outlines, squash and stretch animation, "
                f"vintage Technicolor palette, "
                f"Warner Bros theatrical quality"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            effect = self._get_random_choice("looney_tunes.effects", "cartoon effects")
            lighting = self._get_random_choice("looney_tunes.lighting", "bright theatrical lighting")
            
            components["effects"] = (
                f"{effect}, {lighting}, "
                f"impact stars, motion lines, "
                f"classic cartoon visual comedy"
            )
        else:
            components["effects"] = ""
        
        return components

