from typing import Dict
from ...base_handler import BaseThemeHandler


class NightSkyHandler(BaseThemeHandler):
    """Handler for Night Sky theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "night_sky"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "starry sky")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "milky way panorama")

        components["subject"] = (
            f"((astrophotography)) of {subject}, "
            f"{view_type}, night sky wonder, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "dark sky location")
                environment = location
            celestial = self._get_random_choice(f"{theme_name}.celestial_objects", "Milky Way")
            components["environment"] = f"at {environment}, {celestial}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "cosmic wonder")
            technique = self._get_random_choice(f"{theme_name}.techniques", "long exposure")
            components["style"] = f"{mood}, {technique}, astrophotography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "star points, milky way detail, night atmosphere"
        else:
            components["effects"] = ""

        return components



