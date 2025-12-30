from typing import Dict
from ...base_handler import BaseThemeHandler


class FogHandler(BaseThemeHandler):
    """Handler for Fog theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "fog"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "misty scene")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "foggy forest path")

        components["subject"] = (
            f"((fog photography)) of {subject}, "
            f"{view_type}, atmospheric mist, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                setting = self._get_random_choice(f"{theme_name}.settings", "mysterious forest")
                environment = setting
            fog_type = self._get_random_choice(f"{theme_name}.fog_types", "morning fog")
            components["environment"] = f"in {environment}, {fog_type}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "mysterious atmosphere")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "diffused soft light")
            components["style"] = f"{mood}, {lighting}, fog photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "soft edges, layered depth, ethereal atmosphere"
        else:
            components["effects"] = ""

        return components

