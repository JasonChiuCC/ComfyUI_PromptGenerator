from typing import Dict
from ...base_handler import BaseThemeHandler


class GothicCathedralHandler(BaseThemeHandler):
    """Handler for Gothic Cathedral theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "gothic_cathedral"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "Gothic cathedral")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "soaring interior nave")
        element = self._get_random_choice(f"{theme_name}.elements", "pointed arches")

        components["subject"] = (
            f"((Gothic architecture)) of {subject}, "
            f"{view_type}, {element}, "
            f"medieval grandeur, architectural photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                period = self._get_random_choice(f"{theme_name}.periods", "High Gothic")
                environment = f"{period} style"
            lighting = self._get_random_choice(f"{theme_name}.lighting", "divine light rays")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "spiritual transcendence")
            components["style"] = f"Gothic cathedral aesthetic, {mood}, sacred architecture"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "stained glass light, soaring verticality, stone tracery detail"
        else:
            components["effects"] = ""

        return components

