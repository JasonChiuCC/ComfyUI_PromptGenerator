"""Ghibli (Studio Ghibli) theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GhibliHandler(BaseThemeHandler):
    """Handler for Studio Ghibli style prompt generation.
    
    Generates prompts inspired by Hayao Miyazaki and Studio Ghibli's
    distinctive warm, nature-focused, and whimsical animation style.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Ghibli style prompt components.
        
        Args:
            custom_subject: Optional custom character override
            custom_location: Optional custom location override
            include_environment: Whether to include nature/setting
            include_style: Whether to include Ghibli style details
            include_effects: Whether to include atmospheric effects
            
        Returns:
            Dictionary with prompt components
        """
        components = {}
        
        # Generate character/subject
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("ghibli.characters", "young protagonist")
        
        outfit = self._get_random_choice("ghibli.outfits", "simple clothes")
        expression = self._get_random_choice("ghibli.expressions", "gentle expression")
        shot_type = self._get_random_choice("ghibli.shot_types", "full body shot")
        
        components["subject"] = (
            f"((Studio Ghibli style)) {character}, "
            f"{shot_type}, wearing {outfit}, {expression}, "
            f"Hayao Miyazaki character design"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("ghibli.locations", "beautiful landscape")
            
            nature = self._get_random_choice("ghibli.nature_elements", "lush greenery")
            weather = self._get_random_choice("ghibli.weather", "gentle atmosphere")
            creature = self._get_random_choice("ghibli.creatures", "magical spirit")
            
            components["environment"] = (
                f"in {location}, surrounded by {nature}, "
                f"{weather}, with {creature} nearby, "
                f"detailed Ghibli background"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            mood = self._get_random_choice("ghibli.moods", "whimsical feeling")
            
            components["style"] = (
                f"Studio Ghibli animation style, "
                f"hand-painted aesthetic, {mood}, "
                f"watercolor textures, soft colors, "
                f"Miyazaki masterpiece quality"
            )
        else:
            components["style"] = ""
        
        # Generate effects/lighting
        if include_effects:
            lighting = self._get_random_choice("ghibli.lighting", "soft natural light")
            
            components["effects"] = (
                f"{lighting}, "
                f"painterly atmosphere, subtle details, "
                f"nostalgic warmth, dreamy quality"
            )
        else:
            components["effects"] = ""
        
        return components

