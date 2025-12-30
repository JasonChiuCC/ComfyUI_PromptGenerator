from typing import Dict
from ...base_handler import BaseThemeHandler


class CanyonHandler(BaseThemeHandler):
    """Handler for Canyon theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "canyon"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "grand canyon vista")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "rim overlook panorama")

        components["subject"] = (
            f"((canyon photography)) of {subject}, "
            f"{view_type}, geological wonder, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                famous = self._get_random_choice(f"{theme_name}.famous_canyons", "Grand Canyon")
                environment = famous
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden hour rim light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "geological wonder")
            components["style"] = f"{mood}, canyon landscape photography"
        else:
            components["style"] = ""

        if include_effects:
            element = self._get_random_choice(f"{theme_name}.elements", "colorful rock layers")
            components["effects"] = f"{element}, dramatic scale, layered geology"
        else:
            components["effects"] = ""

        return components

