from typing import Dict
from ...base_handler import BaseThemeHandler


class CaveHandler(BaseThemeHandler):
    """Handler for Cave theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "cave"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "limestone cavern")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "vast cavern interior")

        components["subject"] = (
            f"((cave photography)) of {subject}, "
            f"{view_type}, underground wonder, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                famous = self._get_random_choice(f"{theme_name}.famous_caves", "spectacular cave")
                environment = famous
            formation = self._get_random_choice(f"{theme_name}.formations", "stalactites")
            components["environment"] = f"in {environment}, {formation}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "mysterious depths")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "entrance backlight")
            components["style"] = f"{mood}, {lighting}, cave photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "underground atmosphere, geological formations, natural wonder"
        else:
            components["effects"] = ""

        return components



