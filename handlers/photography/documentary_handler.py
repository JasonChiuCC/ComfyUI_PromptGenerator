"""Documentary photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DocumentaryHandler(BaseThemeHandler):
    """Handler for documentary photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate documentary photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("documentary.subjects", "documentary moment")
        
        composition = self._get_random_choice("documentary.composition_types", "candid shot")
        
        components["subject"] = (
            f"((documentary photography)) {subject}, "
            f"{composition}, authentic unposed moment"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("documentary.locations", "real world setting")
            lighting = self._get_random_choice("documentary.lighting", "available light")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("documentary.styles", "photojournalism")
            components["style"] = f"{style}, truth in photography, raw authenticity"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "unfiltered reality, natural moments, storytelling"
        else:
            components["effects"] = ""
        
        return components
