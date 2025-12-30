from typing import Dict
from ...base_handler import BaseThemeHandler


class AuroraHandler(BaseThemeHandler):
    """Handler for Aurora theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "aurora"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "aurora borealis")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "full sky aurora panorama")

        components["subject"] = (
            f"((aurora photography)) of {subject}, "
            f"{view_type}, northern lights magic, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "arctic region")
                environment = location
            foreground = self._get_random_choice(f"{theme_name}.foregrounds", "snowy landscape")
            components["environment"] = f"in {environment}, {foreground}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "magical wonder")
            colors = self._get_random_choice(f"{theme_name}.colors", "green curtains")
            components["style"] = f"{mood}, {colors}, aurora photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "dancing lights, vivid colors, celestial magic"
        else:
            components["effects"] = ""

        return components

