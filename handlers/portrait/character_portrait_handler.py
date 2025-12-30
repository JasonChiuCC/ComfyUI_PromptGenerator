"""Character Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CharacterPortraitHandler(BaseThemeHandler):
    """Handler for Character Portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate character portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("character_portrait.subjects", "distinctive character")
        
        expression = self._get_random_choice("character_portrait.expressions", "character-defining expression")
        pose = self._get_random_choice("character_portrait.poses", "storytelling pose")
        props = self._get_random_choice("character_portrait.props", "meaningful prop")
        shot_type = self._get_random_choice("character_portrait.shot_types", "character study")
        
        components["subject"] = (
            f"((character portrait)) of {subject}, "
            f"{expression}, {pose}, with {props}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("character_portrait.locations", "contextual setting")
            lighting = self._get_random_choice("character_portrait.lighting", "dramatic character lighting")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("character_portrait.styles", "character photography")
            mood = self._get_random_choice("character_portrait.moods", "compelling")
            components["style"] = f"{style}, {mood}, storytelling, personality-driven"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "unique character, memorable face, personality capture"
        else:
            components["effects"] = ""
        
        return components
