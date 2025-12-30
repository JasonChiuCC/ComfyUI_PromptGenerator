from typing import Dict
from ...base_handler import BaseThemeHandler


class VolcanoHandler(BaseThemeHandler):
    """Handler for Volcano theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "volcano"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "active volcano")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "eruption dramatic shot")

        components["subject"] = (
            f"((volcanic photography)) of {subject}, "
            f"{view_type}, geological power, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                famous = self._get_random_choice(f"{theme_name}.famous_volcanoes", "volcanic landscape")
                environment = famous
            lighting = self._get_random_choice(f"{theme_name}.lighting", "lava glow")
            components["environment"] = f"at {environment}, {lighting}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "raw earth power")
            components["style"] = f"{mood}, volcanic landscape photography"
        else:
            components["style"] = ""

        if include_effects:
            feature = self._get_random_choice(f"{theme_name}.volcanic_features", "lava flow")
            components["effects"] = f"{feature}, dramatic fire, geological drama"
        else:
            components["effects"] = ""

        return components

