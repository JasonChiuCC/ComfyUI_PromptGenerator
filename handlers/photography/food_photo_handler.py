"""Food photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FoodPhotoHandler(BaseThemeHandler):
    """Handler for food photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate food photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("food_photo.subjects", "gourmet dish")
        
        composition = self._get_random_choice("food_photo.composition_types", "overhead flat lay")
        
        components["subject"] = (
            f"((food photography)) {subject}, "
            f"{composition}, appetizing presentation"
        )
        
        if include_environment:
            styling = self._get_random_choice("food_photo.styling", "rustic table setting")
            lighting = self._get_random_choice("food_photo.lighting", "natural window light")
            components["environment"] = f"{styling}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("food_photo.styles", "editorial food")
            components["style"] = f"{style}, magazine quality, mouthwatering"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "fresh and delicious, perfect styling, culinary art"
        else:
            components["effects"] = ""
        
        return components
