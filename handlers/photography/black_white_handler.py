"""Black and White photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BlackWhiteHandler(BaseThemeHandler):
    """Handler for black and white photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate black and white photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("black_white.subjects", "B&W portrait")
        
        composition = self._get_random_choice("black_white.composition_types", "high contrast portrait")
        
        components["subject"] = (
            f"((black and white photography)) {subject}, "
            f"{composition}, monochrome masterpiece"
        )
        
        if include_environment:
            lighting = self._get_random_choice("black_white.lighting", "dramatic side light")
            components["environment"] = f"{lighting}, atmospheric shadows"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("black_white.styles", "fine art B&W")
            tone = self._get_random_choice("black_white.tones", "deep blacks")
            components["style"] = f"{style}, {tone}, timeless classic photography"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "B&W, monochrome, film grain, Ansel Adams inspired"
        else:
            components["effects"] = ""
        
        return components
