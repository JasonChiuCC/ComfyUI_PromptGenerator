"""DreamWorks animation theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DreamworksHandler(BaseThemeHandler):
    """Handler for DreamWorks animation style prompt generation.
    
    Generates prompts inspired by DreamWorks animation style,
    featuring action-comedy aesthetics and dynamic character designs.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate DreamWorks style prompt components."""
        components = {}
        
        # Generate character/subject
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("dreamworks.characters", "DreamWorks character")
        
        char_style = self._get_random_choice("dreamworks.character_styles", "dynamic design")
        expression = self._get_random_choice("dreamworks.expressions", "expressive face")
        shot_type = self._get_random_choice("dreamworks.shot_types", "full body action shot")
        
        components["subject"] = (
            f"((DreamWorks animation style)) {character}, "
            f"{shot_type}, {char_style}, {expression}, "
            f"stylized 3D character, DreamWorks design"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("dreamworks.locations", "adventure setting")
            
            action = self._get_random_choice("dreamworks.action_elements", "dynamic action")
            
            components["environment"] = (
                f"in {location}, "
                f"{action}, "
                f"DreamWorks world design"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            mood = self._get_random_choice("dreamworks.moods", "action comedy")
            
            components["style"] = (
                f"DreamWorks Animation quality, "
                f"{mood}, "
                f"stylized 3D render, "
                f"cinematic animation, dynamic composition"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            lighting = self._get_random_choice("dreamworks.lighting", "dramatic lighting")
            
            components["effects"] = (
                f"{lighting}, "
                f"dynamic visual effects, "
                f"action movie quality, cinematic finish"
            )
        else:
            components["effects"] = ""
        
        return components

