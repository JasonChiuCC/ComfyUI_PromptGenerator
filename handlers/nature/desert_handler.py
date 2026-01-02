from typing import Dict
from ...base_handler import BaseThemeHandler


class DesertHandler(BaseThemeHandler):
    """Handler for Desert theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "desert"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "sand dunes")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "endless dune panorama")

        components["subject"] = (
            f"((desert landscape photography)) of {subject}, "
            f"{view_type}, arid wilderness, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                desert_type = self._get_random_choice(f"{theme_name}.desert_types", "Sahara desert")
                environment = desert_type
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden hour warmth")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "vast emptiness")
            components["style"] = f"{mood}, desert landscape photography"
        else:
            components["style"] = ""

        if include_effects:
            element = self._get_random_choice(f"{theme_name}.elements", "sand patterns")
            components["effects"] = f"{element}, dramatic shadows, natural textures"
        else:
            components["effects"] = ""

        return components



