from typing import Dict
from ...base_handler import BaseThemeHandler


class JapaneseArchHandler(BaseThemeHandler):
    """Handler for Japanese Architecture theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "japanese_arch"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "Japanese temple")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "zen garden perspective")
        element = self._get_random_choice(f"{theme_name}.elements", "curved roof tiles")

        components["subject"] = (
            f"((Japanese architecture)) of {subject}, "
            f"{view_type}, {element}, "
            f"traditional craftsmanship, architectural photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                style = self._get_random_choice(f"{theme_name}.styles", "Wabi-sabi aesthetic")
                environment = f"{style}"
            season = self._get_random_choice(f"{theme_name}.seasons", "cherry blossom spring")
            components["environment"] = f"{environment}, {season}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "zen tranquility")
            components["style"] = f"Japanese aesthetic, {mood}, harmonious design"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "natural materials, refined simplicity, nature integration"
        else:
            components["effects"] = ""

        return components

