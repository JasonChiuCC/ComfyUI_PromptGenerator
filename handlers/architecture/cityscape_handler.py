from typing import Dict
from ...base_handler import BaseThemeHandler


class CityscapeHandler(BaseThemeHandler):
    """Handler for Cityscape theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "cityscape"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "city skyline")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "skyline panorama")
        city = self._get_random_choice(f"{theme_name}.cities", "modern metropolis")

        components["subject"] = (
            f"((cityscape photography)) of {subject}, "
            f"{view_type}, {city}, "
            f"urban landscape, professional photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                element = self._get_random_choice(f"{theme_name}.elements", "glass towers")
                environment = f"featuring {element}"
            weather = self._get_random_choice(f"{theme_name}.weather", "golden hour")
            components["environment"] = f"{environment}, {weather}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "urban energy")
            components["style"] = f"cityscape aesthetic, {mood}, metropolitan view"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "city lights, architectural density, urban atmosphere"
        else:
            components["effects"] = ""

        return components

