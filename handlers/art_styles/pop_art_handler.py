"""Pop Art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PopArtHandler(BaseThemeHandler):
    """Handler for Pop Art style prompt generation.
    
    Generates prompts for Pop Art with bold colors,
    commercial imagery, and mass culture references.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Pop Art prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("pop_art.subjects", "celebrity portrait")
        
        composition = self._get_random_choice("pop_art.composition_types", "bold centered")
        technique = self._get_random_choice("pop_art.techniques", "screen printing")
        color_palette = self._get_random_choice("pop_art.color_palettes", "bold primary colors")
        
        components["subject"] = (
            f"((pop art masterpiece)), {subject}, "
            f"{composition}, {technique}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("pop_art.moods", "ironic commentary")
            
            components["environment"] = (
                f"{mood}, commercial aesthetic, "
                f"mass media influence, consumer culture"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("pop_art.influences", "Warhol style")
            
            components["style"] = (
                f"{influence}, gallery quality, "
                f"iconic pop art style, bold graphic design, "
                f"museum exhibition piece"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"high contrast, flat colors, "
                f"ben-day dots, bold outlines, "
                f"screen print texture, vibrant saturation"
            )
        else:
            components["effects"] = ""
        
        return components

