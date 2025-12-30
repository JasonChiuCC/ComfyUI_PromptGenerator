from typing import Dict
from ...base_handler import BaseThemeHandler


class MeadowHandler(BaseThemeHandler):
    """Handler for Meadow theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "meadow"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "wildflower meadow")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "wildflower field panorama")

        components["subject"] = (
            f"((meadow photography)) of {subject}, "
            f"{view_type}, pastoral beauty, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "countryside meadow")
                environment = location
            flowers = self._get_random_choice(f"{theme_name}.flowers", "wildflowers")
            components["environment"] = f"in {environment}, {flowers}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "pastoral peace")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden hour warmth")
            components["style"] = f"{mood}, {lighting}, nature photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "vibrant colors, flower details, natural beauty"
        else:
            components["effects"] = ""

        return components

