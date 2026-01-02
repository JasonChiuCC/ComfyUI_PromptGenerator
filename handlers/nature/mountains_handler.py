from typing import Dict
from ...base_handler import BaseThemeHandler


class MountainsHandler(BaseThemeHandler):
    """Handler for Mountains theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "mountains"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "mountain peak")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "dramatic peak panorama")

        components["subject"] = (
            f"((mountain landscape photography)) of {subject}, "
            f"{view_type}, majestic alpine scenery, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "mountain range")
                environment = location
            weather = self._get_random_choice(f"{theme_name}.weather", "clear sky")
            components["environment"] = f"in {environment}, {weather}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "majestic grandeur")
            season = self._get_random_choice(f"{theme_name}.seasons", "summer")
            components["style"] = f"{mood}, {season}, landscape photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "sharp detail, dramatic scale, natural lighting"
        else:
            components["effects"] = ""

        return components



