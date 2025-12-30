"""Film grain photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FilmGrainHandler(BaseThemeHandler):
    """Handler for film grain photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate film grain photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("film_grain.subjects", "vintage portrait")
        
        composition = self._get_random_choice("film_grain.composition_types", "analog film shot")
        
        components["subject"] = (
            f"((film photography)) {subject}, "
            f"{composition}, authentic analog feel"
        )
        
        if include_environment:
            lighting = self._get_random_choice("film_grain.lighting", "natural light")
            components["environment"] = f"{lighting}, nostalgic atmosphere"
        else:
            components["environment"] = ""
        
        if include_style:
            film_stock = self._get_random_choice("film_grain.film_stocks", "Kodak Portra 400")
            style = self._get_random_choice("film_grain.styles", "35mm film")
            components["style"] = f"{style}, shot on {film_stock}, analog warmth"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "film grain, slight vignette, analog color, vintage aesthetic"
        else:
            components["effects"] = ""
        
        return components
