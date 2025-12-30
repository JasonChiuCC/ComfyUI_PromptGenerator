"""Impasto style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ImpastoHandler(BaseThemeHandler):
    """Handler for impasto painting style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate impasto painting prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("impasto.subjects", "textured landscape")
        
        composition = self._get_random_choice("impasto.composition_types", "expressive landscape")
        technique = self._get_random_choice("impasto.techniques", "thick application")
        tool = self._get_random_choice("impasto.tools", "palette knife")
        
        components["subject"] = (
            f"((impasto painting)), {subject}, "
            f"{composition}, {technique}, using {tool}"
        )
        
        if include_environment:
            effect = self._get_random_choice("impasto.effects", "three-dimensional surface")
            mood = self._get_random_choice("impasto.moods", "passionate expression")
            
            components["environment"] = (
                f"{effect}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"Van Gogh inspired, thick paint technique, "
                f"expressive brushwork, textural painting"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"sculptural paint ridges, visible texture, "
                f"dynamic surface, light catching peaks"
            )
        else:
            components["effects"] = ""
        
        return components





