"""Marvel Comics theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MarvelHandler(BaseThemeHandler):
    """Handler for Marvel Comics style prompt generation.
    
    Generates prompts inspired by Marvel Comics' superhero style,
    with iconic poses, dynamic action, and heroic compositions.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Marvel style prompt components."""
        components = {}
        
        # Generate character/subject
        if custom_subject:
            hero = custom_subject
        else:
            hero = self._get_random_choice("marvel.hero_types", "Marvel hero")
        
        power = self._get_random_choice("marvel.powers", "super powers")
        pose = self._get_random_choice("marvel.poses", "heroic pose")
        shot_type = self._get_random_choice("marvel.shot_types", "full body hero pose")
        
        components["subject"] = (
            f"((Marvel Comics style)) {hero}, "
            f"{shot_type}, with {power}, {pose}, "
            f"iconic costume design, Marvel character"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("marvel.locations", "Marvel universe")
            
            components["environment"] = (
                f"in {location}, "
                f"Marvel universe setting, epic scale"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            art_style = self._get_random_choice("marvel.art_styles", "Marvel art")
            mood = self._get_random_choice("marvel.moods", "heroic mood")
            
            components["style"] = (
                f"{art_style}, {mood}, "
                f"Marvel Comics quality, "
                f"professional comic art, bold colors"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            effect = self._get_random_choice("marvel.effects", "power effects")
            
            components["effects"] = (
                f"{effect}, "
                f"superhero visual effects, "
                f"dynamic action lighting"
            )
        else:
            components["effects"] = ""
        
        return components

