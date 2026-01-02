from typing import Dict
from ...base_handler import BaseThemeHandler


class AutumnFoliageHandler(BaseThemeHandler):
    """Handler for Autumn Foliage theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "autumn_foliage"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "autumn forest")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "forest canopy colors")

        components["subject"] = (
            f"((autumn photography)) of {subject}, "
            f"{view_type}, fall colors, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "fall landscape")
                environment = location
            tree_type = self._get_random_choice(f"{theme_name}.tree_types", "maple tree")
            components["environment"] = f"in {environment}, {tree_type}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "nostalgic beauty")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden hour warm")
            components["style"] = f"{mood}, {lighting}, autumn photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "vibrant fall colors, golden leaves, seasonal beauty"
        else:
            components["effects"] = ""

        return components



