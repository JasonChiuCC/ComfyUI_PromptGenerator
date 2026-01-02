from typing import Dict
from ...base_handler import BaseThemeHandler


class LakeHandler(BaseThemeHandler):
    """Handler for Lake theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "lake"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "peaceful lake")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "mirror reflection panorama")

        components["subject"] = (
            f"((lake photography)) of {subject}, "
            f"{view_type}, serene water, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                famous = self._get_random_choice(f"{theme_name}.famous_lakes", "beautiful lake")
                environment = famous
            surrounding = self._get_random_choice(f"{theme_name}.surroundings", "mountain backdrop")
            components["environment"] = f"at {environment}, {surrounding}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "peaceful serenity")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "mirror reflection")
            components["style"] = f"{mood}, {lighting}, lake photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "perfect reflection, calm water, natural beauty"
        else:
            components["effects"] = ""

        return components



