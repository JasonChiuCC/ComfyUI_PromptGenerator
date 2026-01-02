from typing import Dict
from ...base_handler import BaseThemeHandler


class CherryBlossomHandler(BaseThemeHandler):
    """Handler for Cherry Blossom theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "cherry_blossom"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "cherry blossom tree")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "cherry blossom canopy")

        components["subject"] = (
            f"((sakura photography)) of {subject}, "
            f"{view_type}, spring beauty, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "Japanese garden")
                environment = location
            variety = self._get_random_choice(f"{theme_name}.varieties", "Somei Yoshino")
            components["environment"] = f"in {environment}, {variety}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "romantic beauty")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "soft spring sunlight")
            components["style"] = f"{mood}, {lighting}, cherry blossom photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "falling petals, pink blossoms, spring atmosphere"
        else:
            components["effects"] = ""

        return components



