from typing import Dict
from ...base_handler import BaseThemeHandler


class SunsetHandler(BaseThemeHandler):
    """Handler for Sunset theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "sunset"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "brilliant sunset")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "panoramic sky ablaze")

        components["subject"] = (
            f"((sunset photography)) of {subject}, "
            f"{view_type}, golden hour magic, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "horizon")
                environment = location
            sky_colors = self._get_random_choice(f"{theme_name}.sky_colors", "fiery orange")
            components["environment"] = f"over {environment}, {sky_colors}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "romantic warmth")
            clouds = self._get_random_choice(f"{theme_name}.cloud_types", "dramatic clouds")
            components["style"] = f"{mood}, {clouds}, sunset photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "vibrant colors, silhouette effects, golden light"
        else:
            components["effects"] = ""

        return components



