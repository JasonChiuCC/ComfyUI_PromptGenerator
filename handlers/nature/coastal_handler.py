from typing import Dict
from ...base_handler import BaseThemeHandler


class CoastalHandler(BaseThemeHandler):
    """Handler for Coastal theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "coastal"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "dramatic coastline")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "dramatic cliff panorama")

        components["subject"] = (
            f"((coastal photography)) of {subject}, "
            f"{view_type}, seaside scenery, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                famous = self._get_random_choice(f"{theme_name}.famous_coasts", "scenic coastline")
                environment = famous
            coastal_type = self._get_random_choice(f"{theme_name}.coastal_types", "rugged shore")
            components["environment"] = f"at {environment}, {coastal_type}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "coastal serenity")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden hour beach")
            components["style"] = f"{mood}, {lighting}, coastal photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "wave motion, rocky textures, ocean atmosphere"
        else:
            components["effects"] = ""

        return components

