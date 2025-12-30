"""Film Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FilmPortraitHandler(BaseThemeHandler):
    """Handler for Film Portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate film portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("film_portrait.subjects", "model")
        
        expression = self._get_random_choice("film_portrait.expressions", "natural expression")
        pose = self._get_random_choice("film_portrait.poses", "relaxed authentic pose")
        outfit = self._get_random_choice("film_portrait.outfits", "everyday clothing")
        shot_type = self._get_random_choice("film_portrait.shot_types", "film portrait")
        
        components["subject"] = (
            f"((analog film photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("film_portrait.locations", "natural setting")
            lighting = self._get_random_choice("film_portrait.lighting", "natural film lighting")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            film_stock = self._get_random_choice("film_portrait.film_stocks", "Portra 400")
            style = self._get_random_choice("film_portrait.styles", "analog film photography")
            components["style"] = f"{style}, shot on {film_stock}, organic film grain"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("film_portrait.effects", "film grain")
            components["effects"] = f"{effect}, analog warmth, authentic film look"
        else:
            components["effects"] = ""
        
        return components
