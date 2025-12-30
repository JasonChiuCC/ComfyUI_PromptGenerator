"""Retro anime theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class RetroAnimeHandler(BaseThemeHandler):
    """Handler for retro/vintage anime style prompt generation.
    
    Generates prompts for 80s and 90s anime aesthetic,
    featuring classic character designs, film grain, and nostalgic visuals.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate retro anime style prompt components."""
        components = {}
        
        # Generate character
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("retro_anime.characters", "80s anime character")
        
        outfit = self._get_random_choice("retro_anime.outfits", "vintage outfit")
        pose = self._get_random_choice("retro_anime.poses", "classic pose")
        shot_type = self._get_random_choice("retro_anime.shot_types", "full body shot")
        
        components["subject"] = (
            f"((nostalgic retro anime art)) of {character}, "
            f"{shot_type}, wearing {outfit}, {pose}, "
            f"classic anime proportions, 80s-90s anime aesthetic"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("retro_anime.locations", "80s Tokyo")
            
            time = self._get_random_choice("retro_anime.times", "nostalgic sunset")
            
            components["environment"] = (
                f"in {location}, during {time}, "
                f"vintage painted background, "
                f"hand-painted scenery"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            art_style = self._get_random_choice("retro_anime.art_styles", "hand-painted cel animation")
            series_style = self._get_random_choice("retro_anime.series_styles", "classic anime style")
            
            components["style"] = (
                f"{art_style}, {series_style}, "
                f"vintage color palette, soft airbrushed shading, "
                f"theatrical anime quality"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            effect = self._get_random_choice("retro_anime.effects", "film grain")
            lighting = self._get_random_choice("retro_anime.lighting", "nostalgic golden glow")
            
            components["effects"] = (
                f"{effect}, {lighting}, "
                f"VHS aesthetic, vintage bloom, "
                f"cel animation texture"
            )
        else:
            components["effects"] = ""
        
        return components

