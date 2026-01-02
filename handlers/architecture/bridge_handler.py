from typing import Dict
from ...base_handler import BaseThemeHandler


class BridgeHandler(BaseThemeHandler):
    """Handler for Bridge theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "bridge"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "suspension bridge")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "dramatic side profile")
        famous = self._get_random_choice(f"{theme_name}.famous_bridges", "iconic bridge design")

        components["subject"] = (
            f"((bridge photography)) of {subject}, "
            f"{view_type}, {famous}, "
            f"engineering architecture, professional photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                material = self._get_random_choice(f"{theme_name}.materials", "steel cables")
                environment = f"featuring {material}"
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden hour glow")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "engineering marvel")
            components["style"] = f"bridge aesthetic, {mood}, structural beauty"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "water reflection, dramatic span, urban landmark"
        else:
            components["effects"] = ""

        return components



