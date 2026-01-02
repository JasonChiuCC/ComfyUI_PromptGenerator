from typing import Dict
from ...base_handler import BaseThemeHandler


class SunriseHandler(BaseThemeHandler):
    """Handler for Sunrise theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "sunrise"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "breaking dawn")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "first light horizon")

        components["subject"] = (
            f"((sunrise photography)) of {subject}, "
            f"{view_type}, morning light, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "horizon")
                environment = location
            sky_colors = self._get_random_choice(f"{theme_name}.sky_colors", "soft pink")
            components["environment"] = f"over {environment}, {sky_colors}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "new beginning")
            atmosphere = self._get_random_choice(f"{theme_name}.atmospheres", "morning mist")
            components["style"] = f"{mood}, {atmosphere}, sunrise photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "soft pastel colors, morning glow, peaceful light"
        else:
            components["effects"] = ""

        return components



