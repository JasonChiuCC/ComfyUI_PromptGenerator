from typing import Dict
from ...base_handler import BaseThemeHandler


class ArcticHandler(BaseThemeHandler):
    """Handler for Arctic theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "arctic"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "polar ice landscape")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "vast ice sheet panorama")

        components["subject"] = (
            f"((arctic photography)) of {subject}, "
            f"{view_type}, polar wilderness, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "Arctic region")
                environment = location
            lighting = self._get_random_choice(f"{theme_name}.lighting", "polar light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "pristine wilderness")
            components["style"] = f"{mood}, polar landscape photography"
        else:
            components["style"] = ""

        if include_effects:
            wildlife = self._get_random_choice(f"{theme_name}.wildlife", "polar wildlife")
            components["effects"] = f"{wildlife}, ice formations, frozen beauty"
        else:
            components["effects"] = ""

        return components



