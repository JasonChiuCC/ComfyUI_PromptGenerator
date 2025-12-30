from typing import Dict
from ...base_handler import BaseThemeHandler


class StormHandler(BaseThemeHandler):
    """Handler for Storm theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "storm"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "thunderstorm")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "supercell thunderstorm")

        components["subject"] = (
            f"((storm photography)) of {subject}, "
            f"{view_type}, atmospheric drama, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                storm_type = self._get_random_choice(f"{theme_name}.storm_types", "thunderstorm")
                environment = storm_type
            lightning = self._get_random_choice(f"{theme_name}.lightning_types", "lightning bolt")
            components["environment"] = f"featuring {environment}, {lightning}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "nature's fury")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "dramatic light")
            components["style"] = f"{mood}, {lighting}, storm photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "dramatic clouds, electrical energy, atmospheric power"
        else:
            components["effects"] = ""

        return components

