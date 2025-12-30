"""Art Nouveau style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ArtNouveauHandler(BaseThemeHandler):
    """Handler for Art Nouveau style prompt generation.
    
    Generates prompts for Art Nouveau with organic flowing lines,
    floral motifs, and elegant feminine figures.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Art Nouveau prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("art_nouveau.subjects", "elegant woman")
        
        composition = self._get_random_choice("art_nouveau.composition_types", "flowing organic frame")
        element = self._get_random_choice("art_nouveau.elements", "floral motifs")
        color_palette = self._get_random_choice("art_nouveau.color_palettes", "gold and jewel colors")
        
        components["subject"] = (
            f"((Art Nouveau masterpiece)), {subject}, "
            f"{composition}, {element}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("art_nouveau.moods", "elegant beauty")
            
            components["environment"] = (
                f"{mood}, decorative borders, "
                f"organic flowing lines, whiplash curves"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("art_nouveau.influences", "Mucha poster style")
            
            components["style"] = (
                f"{influence}, Belle Epoque elegance, "
                f"decorative art masterpiece, "
                f"ornate illustration, vintage poster quality"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"intricate line work, gold leaf accents, "
                f"stained glass effect, flowing curves, "
                f"rich detailed ornamentation"
            )
        else:
            components["effects"] = ""
        
        return components

