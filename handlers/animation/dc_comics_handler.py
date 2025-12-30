"""DC Comics theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DCComicsHandler(BaseThemeHandler):
    """Handler for DC Comics style prompt generation.
    
    Generates prompts inspired by DC Comics' superhero style,
    with iconic heroes, dramatic compositions, and legendary settings.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate DC Comics style prompt components."""
        components = {}
        
        # Generate character/subject
        if custom_subject:
            hero = custom_subject
        else:
            hero = self._get_random_choice("dc_comics.hero_types", "DC hero")
        
        power = self._get_random_choice("dc_comics.powers", "super powers")
        pose = self._get_random_choice("dc_comics.poses", "heroic pose")
        shot_type = self._get_random_choice("dc_comics.shot_types", "full body hero shot")
        
        components["subject"] = (
            f"((DC Comics style)) {hero}, "
            f"{shot_type}, with {power}, {pose}, "
            f"legendary hero design, DC character"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("dc_comics.locations", "DC universe")
            
            components["environment"] = (
                f"in {location}, "
                f"DC universe setting, legendary atmosphere"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            art_style = self._get_random_choice("dc_comics.art_styles", "DC art")
            mood = self._get_random_choice("dc_comics.moods", "heroic mood")
            
            components["style"] = (
                f"{art_style}, {mood}, "
                f"DC Comics quality, "
                f"professional comic art, dramatic lighting"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            effect = self._get_random_choice("dc_comics.effects", "power effects")
            
            components["effects"] = (
                f"{effect}, "
                f"superhero visual effects, "
                f"epic scale lighting"
            )
        else:
            components["effects"] = ""
        
        return components

