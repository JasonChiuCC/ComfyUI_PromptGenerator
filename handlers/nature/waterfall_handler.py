from typing import Dict
from ...base_handler import BaseThemeHandler


class WaterfallHandler(BaseThemeHandler):
    """Handler for Waterfall theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "waterfall"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "majestic waterfall")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "full cascade panorama")

        components["subject"] = (
            f"((waterfall photography)) of {subject}, "
            f"{view_type}, natural wonder, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                famous = self._get_random_choice(f"{theme_name}.famous_waterfalls", "spectacular falls")
                environment = famous
            waterfall_type = self._get_random_choice(f"{theme_name}.waterfall_types", "plunge waterfall")
            components["environment"] = f"at {environment}, {waterfall_type}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "powerful majesty")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "rainbow in mist")
            components["style"] = f"{mood}, {lighting}, waterfall photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "silky water flow, mist spray, long exposure effect"
        else:
            components["effects"] = ""

        return components



