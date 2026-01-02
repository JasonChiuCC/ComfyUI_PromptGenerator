from typing import Dict
from ...base_handler import BaseThemeHandler


class OceanHandler(BaseThemeHandler):
    """Handler for Ocean theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "ocean"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "ocean expanse")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "endless horizon seascape")

        components["subject"] = (
            f"((ocean photography)) of {subject}, "
            f"{view_type}, marine scenery, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                wave_type = self._get_random_choice(f"{theme_name}.wave_types", "rolling waves")
                environment = wave_type
            weather = self._get_random_choice(f"{theme_name}.weather", "clear day")
            components["environment"] = f"with {environment}, {weather}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "vast infinity")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden light")
            components["style"] = f"{mood}, {lighting}, seascape photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "water texture, horizon line, ocean atmosphere"
        else:
            components["effects"] = ""

        return components



