"""Stop Motion animation theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class StopMotionHandler(BaseThemeHandler):
    """Handler for stop motion animation style prompt generation.
    
    Generates prompts for stop motion animation aesthetics,
    featuring handcrafted characters, miniature sets, and tactile textures.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate stop motion style prompt components."""
        components = {}
        
        # Generate character/subject
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("stop_motion.characters", "stop motion character")
        
        material = self._get_random_choice("stop_motion.materials", "clay")
        texture = self._get_random_choice("stop_motion.textures", "handmade texture")
        shot_type = self._get_random_choice("stop_motion.shot_types", "full puppet body shot")
        
        components["subject"] = (
            f"((stop motion animation)) {character}, "
            f"{shot_type}, made of {material}, {texture}, "
            f"handcrafted figure, claymation style"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                set_piece = custom_location
            else:
                set_piece = self._get_random_choice("stop_motion.sets", "miniature set")
            
            components["environment"] = (
                f"in {set_piece}, "
                f"miniature world, handmade set design, "
                f"practical miniature"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            style = self._get_random_choice("stop_motion.styles", "stop motion")
            mood = self._get_random_choice("stop_motion.moods", "whimsical")
            
            components["style"] = (
                f"{style}, {mood}, "
                f"frame by frame animation, "
                f"tactile quality, artisanal craftsmanship"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            lighting = self._get_random_choice("stop_motion.lighting", "practical lighting")
            
            components["effects"] = (
                f"{lighting}, "
                f"miniature photography, "
                f"shallow depth of field, handmade charm"
            )
        else:
            components["effects"] = ""
        
        return components

