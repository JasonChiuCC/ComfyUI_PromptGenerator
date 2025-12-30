"""Long exposure photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class LongExposureHandler(BaseThemeHandler):
    """Handler for long exposure photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate long exposure photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("long_exposure.subjects", "light trails")
        
        composition = self._get_random_choice("long_exposure.composition_types", "flowing motion")
        
        components["subject"] = (
            f"((long exposure photography)) {subject}, "
            f"{composition}, time-lapse effect"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("long_exposure.locations", "urban night scene")
            components["environment"] = f"in {location}, motion blur trails"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("long_exposure.styles", "artistic long exposure")
            components["style"] = f"{style}, silky smooth water, light painting"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "motion blur, light streaks, ethereal movement, tripod shot"
        else:
            components["effects"] = ""
        
        return components
