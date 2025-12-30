"""Abstract art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class AbstractHandler(BaseThemeHandler):
    """Handler for abstract art style prompt generation.
    
    Generates prompts for abstract art with geometric shapes,
    color fields, and non-representational compositions.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate abstract art prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("abstract.subjects", "abstract forms")
        
        composition = self._get_random_choice("abstract.composition_types", "dynamic composition")
        technique = self._get_random_choice("abstract.techniques", "abstract technique")
        color_scheme = self._get_random_choice("abstract.color_schemes", "bold colors")
        
        components["subject"] = (
            f"((abstract art masterpiece)), {subject}, "
            f"{composition}, {technique}, {color_scheme}"
        )
        
        # Generate environment (for abstract, this is mood/atmosphere)
        if include_environment:
            mood = self._get_random_choice("abstract.moods", "dynamic energy")
            
            components["environment"] = (
                f"{mood}, non-representational, pure abstraction"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("abstract.influences", "modern abstract")
            
            components["style"] = (
                f"{influence}, museum quality, "
                f"fine art painting, gallery exhibition piece, "
                f"professional abstract artwork"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"high resolution, textured canvas, "
                f"artistic brushwork, vibrant pigments, "
                f"professional fine art quality"
            )
        else:
            components["effects"] = ""
        
        return components

