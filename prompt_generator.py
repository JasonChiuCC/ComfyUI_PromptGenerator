"""
Prompt Generator Node for ComfyUI

This module contains the main node class, configuration manager, and theme registry
for generating prompts using various themes with random element combinations.
"""

import os
import json
import random
import importlib
from typing import Dict, List, Tuple, Optional, Any

from .base_handler import BaseThemeHandler


# =============================================================================
# ConfigManager - Configuration Loading and Hot Reload
# =============================================================================

class ConfigManager:
    """Manages configuration loading from JSON files with hot reload support.
    
    Loads all JSON files from the configs/ directory and provides access
    to configuration values using dot-notation keys.
    """
    
    def __init__(self, seed: Optional[int] = None):
        """Initialize the configuration manager.
        
        Args:
            seed: Optional random seed for reproducible selections
        """
        self.configs: Dict[str, Any] = {}
        self.random = random.Random(seed) if seed is not None else random.Random()
        self._config_dir = os.path.join(os.path.dirname(__file__), "configs")
        self._load_configs()
    
    def _load_configs(self):
        """Load all JSON configuration files from the configs directory (including subdirectories)."""
        self.configs = {}
        
        if not os.path.exists(self._config_dir):
            return
        
        # Walk through all subdirectories
        for root, dirs, files in os.walk(self._config_dir):
            for filename in files:
                if filename.endswith('.json'):
                    filepath = os.path.join(root, filename)
                    # Get relative path for logging
                    rel_path = os.path.relpath(filepath, self._config_dir)
                    # Use filename (without .json) as config key
                    config_name = filename[:-5]  # Remove .json extension
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            config_data = json.load(f)
                            # Merge config data directly (JSON already has theme_name as key)
                            self.configs.update(config_data)
                    except Exception:
                        pass  # Silently skip failed configs
    
    def reload(self):
        """Reload all configurations from disk (hot reload)."""
        self._load_configs()
    
    def set_seed(self, seed: int):
        """Set random seed for reproducible selections.
        
        Args:
            seed: Random seed value
        """
        self.random.seed(seed)
    
    def get_config(self, key: str) -> Any:
        """Get configuration value by dot-notation key.
        
        Args:
            key: Dot-notation key (e.g., 'realistic.cameras')
            
        Returns:
            Configuration value
            
        Raises:
            KeyError: If key is not found
        """
        keys = key.split('.')
        value = self.configs
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                raise KeyError(f"Configuration key not found: {key}")
        
        return value
    
    def get_available_themes(self) -> List[str]:
        """Get list of available theme names.
        
        Returns:
            List of theme names found in configurations
        """
        return list(self.configs.keys())


# =============================================================================
# ThemeRegistry - Theme Handler Management
# =============================================================================

class ThemeRegistry:
    """Registry for managing theme handlers.
    
    Handles loading, initialization, and hot reloading of theme handlers.
    """
    
    # Display name to internal name mapping
    THEME_DISPLAY_NAMES = {
        "🎲 Dynamic Random": "random",
        "📸 Realistic": "realistic",
        "⚔️ Fantasy": "fantasy",
    }
    
    def __init__(self, config_manager: ConfigManager, debug: bool = False):
        """Initialize the theme registry.
        
        Args:
            config_manager: ConfigManager instance
            debug: Enable debug output
        """
        self.config_manager = config_manager
        self.debug = debug
        self.handlers: Dict[str, BaseThemeHandler] = {}
        self._init_handlers()
    
    def _debug_print(self, message: str):
        """Print debug message if debug mode is enabled."""
        if self.debug:
            print(f"[DEBUG] ThemeRegistry - {message}")
    
    def _init_handlers(self):
        """Initialize all theme handlers.
        
        Uses the new auto-discovery system:
        1. Custom handlers from handlers/ subfolders (for special logic)
        2. GenericThemeHandler for any config without a custom handler
        """
        self._debug_print("Initializing theme handlers...")
        self.handlers = {}
        
        try:
            from .handlers import get_all_handlers
            
            # Get all handlers (custom + generic fallback)
            self.handlers = get_all_handlers(self.config_manager)
            self._debug_print(f"Loaded {len(self.handlers)} handlers (custom + generic)")
            
        except ImportError as e:
            # Fallback: try legacy method
            self._debug_print(f"Falling back to legacy handler loading: {e}")
            try:
                from .handlers import HANDLER_CLASSES
                for theme_name, handler_class in HANDLER_CLASSES.items():
                    try:
                        self.handlers[theme_name] = handler_class(self.config_manager)
                    except Exception:
                        pass
            except ImportError:
                pass
    
    def reload_handlers(self):
        """Hot reload all handlers (reimport Python modules)."""
        try:
            # Reload the handlers module
            from . import handlers
            importlib.reload(handlers)
            
            # Re-initialize handlers
            self._init_handlers()
            
        except Exception:
            pass  # Silently handle reload errors
    
    def get_handler(self, theme: str) -> Optional[BaseThemeHandler]:
        """Get handler for a specific theme.
        
        Args:
            theme: Internal theme name
            
        Returns:
            Theme handler instance or None if not found
        """
        return self.handlers.get(theme)
    
    def get_internal_theme(self, display_name: str) -> str:
        """Convert display name to internal theme name.
        
        Args:
            display_name: Theme display name (with emoji)
            
        Returns:
            Internal theme name
        """
        return self.THEME_DISPLAY_NAMES.get(display_name, "realistic")
    
    def get_random_theme(self) -> str:
        """Get a random theme name from available themes.
        
        Returns:
            Random internal theme name
        """
        available = list(self.handlers.keys())
        if not available:
            return "realistic"
        return self.config_manager.random.choice(available)
    
    def get_all_display_themes(self) -> List[str]:
        """Get all available theme display names for UI.
        
        Returns:
            List of display theme names
        """
        return list(self.THEME_DISPLAY_NAMES.keys())


# =============================================================================
# PromptGeneratorNode - Main ComfyUI Node
# =============================================================================

class PromptGeneratorNode:
    """ComfyUI node for generating prompts using theme-based random combinations.
    
    This node provides a user interface for selecting themes and generating
    prompts with optional custom subject and location overrides.
    """
    
    def __init__(self):
        """Initialize the prompt generator node."""
        self.config_manager = ConfigManager()
        self.theme_registry = ThemeRegistry(self.config_manager)
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict:
        """Define input types for the node UI.
        
        Returns:
            Dictionary of required and optional inputs
        """
        # Create a temporary registry to get available themes
        temp_config = ConfigManager()
        temp_registry = ThemeRegistry(temp_config)
        available_themes = temp_registry.get_all_display_themes()
        
        return {
            "required": {
                "theme": (available_themes, {
                    "default": "🎲 Dynamic Random"
                }),
            },
            "optional": {
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 0xffffffffffffffff
                }),
                "custom_subject": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Optional: Override random subject"
                }),
                "custom_location": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Optional: Override random location"
                }),
                "include_environment": (["yes", "no"], {"default": "yes"}),
                "include_style": (["yes", "no"], {"default": "yes"}),
                "include_effects": (["yes", "no"], {"default": "yes"}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "INT")
    RETURN_NAMES = ("prompt", "selected_theme", "subject", "environment", "style", "seed")
    FUNCTION = "generate"
    CATEGORY = "JC/PromptGenerator"
    
    def generate(
        self,
        theme: str,
        seed: int = 0,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: str = "yes",
        include_style: str = "yes",
        include_effects: str = "yes"
    ) -> Tuple[str, str, str, str, str, int]:
        """Generate a prompt using the selected theme.
        
        Args:
            theme: Theme display name
            seed: Random seed for reproducibility
            custom_subject: Optional custom subject override
            custom_location: Optional custom location override
            include_environment: Whether to include environment
            include_style: Whether to include style
            include_effects: Whether to include effects
            
        Returns:
            Tuple of (prompt, selected_theme, subject, environment, style, seed)
        """
        # Set seed for reproducibility
        self.config_manager.set_seed(seed)
        
        # Get internal theme name
        internal_theme = self.theme_registry.get_internal_theme(theme)
        selected_theme_display = theme
        
        # Handle random theme selection
        if internal_theme == "random":
            internal_theme = self.theme_registry.get_random_theme()
            # Find display name for the randomly selected theme
            for display_name, internal_name in self.theme_registry.THEME_DISPLAY_NAMES.items():
                if internal_name == internal_theme:
                    selected_theme_display = display_name
                    break
        
        if is_debug:
            print(f"[DEBUG] Selected theme: {internal_theme}")
        
        # Get handler
        handler = self.theme_registry.get_handler(internal_theme)
        
        if not handler:
            error_msg = f"Error: Handler not found for theme '{internal_theme}'"
            return (error_msg, theme, "", "", "", seed)
        
        # Set debug mode on handler
        handler.set_debug(is_debug)
        
        # Generate components
        try:
            components = handler.generate(
                custom_subject=custom_subject,
                custom_location=custom_location,
                include_environment=(include_environment == "yes"),
                include_style=(include_style == "yes"),
                include_effects=(include_effects == "yes")
            )
        except Exception as e:
            error_msg = f"Error generating prompt: {e}"
            return (error_msg, theme, "", "", "", seed)
        
        # Extract components
        subject = components.get("subject", "")
        environment = components.get("environment", "")
        style = components.get("style", "")
        effects = components.get("effects", "")
        
        # Combine into final prompt
        prompt_parts = [p for p in [subject, environment, style, effects] if p]
        final_prompt = ", ".join(prompt_parts)
        
        if is_debug:
            print(f"[DEBUG] Generated prompt: {final_prompt[:100]}...")
        
        return (
            final_prompt,
            selected_theme_display,
            subject,
            environment,
            style,
            seed
        )


# =============================================================================
# CategoryPromptBase - Base Class for Category-specific Nodes
# =============================================================================

class CategoryPromptBase:
    """Base class for category-specific prompt generator nodes.
    
    Each category (Animation, Art Style, etc.) has its own node.
    Subclasses define AVAILABLE_THEMES and ALL_THEMES for that category.
    
    Theme format: (display_name, internal_name)
    - If internal_name is None, it's a section header (displayed as dropdown label)
    - Otherwise it's a selectable theme (displayed as checkbox)
    """
    
    # Override in subclass: list of (display_name, internal_name) tuples
    AVAILABLE_THEMES: List[Tuple[str, Optional[str]]] = []
    
    # Override in subclass: list of all internal_names for "Select All" functionality
    ALL_THEMES: List[str] = []
    
    # Override in subclass: display name for "Select All" checkbox
    SELECT_ALL_LABEL: str = "✅ Select All"
    
    def __init__(self):
        """Initialize the category prompt generator node."""
        self.config_manager = ConfigManager()
        self.theme_registry = ThemeRegistry(self.config_manager)
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict:
        """Define input types with theme checkboxes."""
        
        theme_widgets = {}
        
        # Add "Select All" checkbox first
        theme_widgets[cls.SELECT_ALL_LABEL] = ("BOOLEAN", {"default": False})
        
        # Add individual theme checkboxes
        for display_name, internal_name in cls.AVAILABLE_THEMES:
            if internal_name is None:
                # Section header - use single-option dropdown (looks like label)
                theme_widgets[display_name] = (["▼"],)
            else:
                # Selectable theme - use checkbox
                theme_widgets[display_name] = ("BOOLEAN", {"default": False})
        
        return {
            "required": {
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 0xffffffffffffffff
                }),
                "batch_count": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 100,
                    "step": 1,
                }),
            },
            "optional": {
                **theme_widgets,
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("prompts", "theme_names")
    OUTPUT_IS_LIST = (True, True)
    FUNCTION = "generate"
    CATEGORY = "JC/PromptGenerator"
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        """Force regeneration by returning a unique value each time."""
        import time
        return time.time()
    
    def generate(
        self,
        seed: int = 0,
        batch_count: int = 1,
        **kwargs
    ) -> Tuple[List[str], List[str]]:
        """Generate prompts for all enabled themes."""
        
        # Check if "Select All" is enabled
        select_all = kwargs.get(self.SELECT_ALL_LABEL, False)
        
        # Collect enabled themes
        enabled_themes = []
        
        for display_name, internal_name in self.AVAILABLE_THEMES:
            if internal_name is None:
                continue  # Skip section headers
            
            # Theme is enabled if individually selected OR select_all is checked
            if select_all or kwargs.get(display_name, False):
                enabled_themes.append((display_name, internal_name))
        
        # If no themes enabled, raise error
        if not enabled_themes:
            raise ValueError("⚠️ 請至少選擇一個主題！\n\nPlease select at least one theme!")
        
        # Generate prompts for each enabled theme
        prompts = []
        theme_names = []
        prompt_index = 0
        
        for display_name, internal_name in enabled_themes:
            handler = self.theme_registry.get_handler(internal_name)
            if not handler:
                prompts.append(f"Error: Handler not found for {internal_name}")
                theme_names.append(display_name)
                prompt_index += 1
                continue
            
            # Generate multiple prompts per theme
            for j in range(batch_count):
                # Use larger seed spacing to ensure different random sequences
                # Different themes: prompt_index * 10000
                # Different batches within same theme: j * 1000
                theme_seed = (seed + prompt_index * 10000 + j * 1000) % 0xffffffffffffffff
                self.config_manager.set_seed(theme_seed)
                prompt_index += 1
                
                try:
                    components = handler.generate(
                        custom_subject="",
                        custom_location="",
                        include_environment=True,
                        include_style=True,
                        include_effects=True
                    )
                    
                    subject = components.get("subject", "")
                    environment = components.get("environment", "")
                    style = components.get("style", "")
                    effects = components.get("effects", "")
                    
                    prompt_parts = [p for p in [subject, environment, style, effects] if p]
                    final_prompt = ", ".join(prompt_parts)
                    
                    prompts.append(final_prompt)
                    if batch_count > 1:
                        theme_names.append(f"{display_name} #{j+1}")
                    else:
                        theme_names.append(display_name)
                    
                except Exception as e:
                    prompts.append(f"Error: {e}")
                    theme_names.append(display_name)
        
        return (prompts, theme_names)


# =============================================================================
# Animation Category Nodes
# =============================================================================

class AnimationPromptEN(CategoryPromptBase):
    """English Animation prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All"
    
    AVAILABLE_THEMES = [
        # Japanese
        ("      Anime", "anime"),
        ("      Ghibli", "ghibli"),
        ("      Manga", "manga"),
        ("      Mecha", "mecha"),
        ("      Shonen", "shonen"),
        ("      Retro Anime", "retro_anime"),
        # Korean
        ("      Webtoon", "webtoon"),
        # Western
        ("      Disney", "disney"),
        ("      Pixar", "pixar"),
        ("      Dreamworks", "dreamworks"),
        ("      Illumination", "illumination"),
        ("      Looney Tunes", "looney_tunes"),
        ("      South Park", "south_park"),
        # Comics
        ("      Marvel", "marvel"),
        ("      DC Comics", "dc_comics"),
        # Other
        ("      Stop Motion", "stop_motion"),
        ("      Chibi", "chibi"),
    ]
    
    ALL_THEMES = [
        "anime", "ghibli", "manga", "mecha", "shonen", "retro_anime",
        "webtoon", "disney", "pixar", "dreamworks", "illumination",
        "looney_tunes", "south_park", "marvel", "dc_comics",
        "stop_motion", "chibi"
    ]
    
    CATEGORY = "JC Prompt Generator/Animation 動畫"


class AnimationPromptZH(CategoryPromptBase):
    """Chinese Animation prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選"
    
    AVAILABLE_THEMES = [
        # 日式
        ("      動漫", "anime"),
        ("      吉卜力", "ghibli"),
        ("      漫畫", "manga"),
        ("      機甲動畫", "mecha"),
        ("      少年向", "shonen"),
        ("      復古動畫", "retro_anime"),
        # 韓式
        ("      韓漫", "webtoon"),
        # 西方
        ("      迪士尼", "disney"),
        ("      皮克斯", "pixar"),
        ("      夢工廠", "dreamworks"),
        ("      照明娛樂", "illumination"),
        ("      樂一通", "looney_tunes"),
        ("      南方公園", "south_park"),
        # 美漫
        ("      漫威", "marvel"),
        ("      DC漫畫", "dc_comics"),
        # 其他
        ("      定格動畫", "stop_motion"),
        ("      Q版", "chibi"),
    ]
    
    ALL_THEMES = [
        "anime", "ghibli", "manga", "mecha", "shonen", "retro_anime",
        "webtoon", "disney", "pixar", "dreamworks", "illumination",
        "looney_tunes", "south_park", "marvel", "dc_comics",
        "stop_motion", "chibi"
    ]
    
    CATEGORY = "JC Prompt Generator/Animation 動畫"


# =============================================================================
# Art Style Category Nodes (placeholder - to be implemented)
# =============================================================================

class ArtStylePromptEN(CategoryPromptBase):
    """English Art Style prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All"
    
    AVAILABLE_THEMES = [
        ("      Abstract", "abstract"),
        ("      Concept Art", "concept_art"),
        ("      Minimalist", "minimalist"),
        ("      Surrealism", "surrealism"),
        ("      Pop Art", "pop_art"),
        ("      Art Nouveau", "art_nouveau"),
        ("      Art Deco", "art_deco"),
        ("      Cubism", "cubism"),
        ("      Expressionism", "expressionism"),
        ("      Impressionism", "impressionism"),
        ("      Baroque", "baroque"),
        ("      Renaissance", "renaissance"),
        ("      Psychedelic", "psychedelic"),
        ("      Glitch Art", "glitch_art"),
        ("      Graffiti", "graffiti"),
        ("      Flat Design", "flat_design"),
        ("      Pointillism", "pointillism"),
        ("      Fauvism", "fauvism"),
        ("      Romanticism", "romanticism"),
        ("      Bauhaus", "bauhaus"),
        ("      Gothic Art", "gothic_art"),
        ("      Street Art", "street_art"),
    ]
    
    ALL_THEMES = [
        "abstract", "concept_art", "minimalist", "surrealism", "pop_art",
        "art_nouveau", "art_deco", "cubism", "expressionism", "impressionism",
        "baroque", "renaissance", "psychedelic", "glitch_art", "graffiti",
        "flat_design", "pointillism", "fauvism", "romanticism", "bauhaus",
        "gothic_art", "street_art"
    ]
    
    CATEGORY = "JC Prompt Generator/Art Style 藝術風格"


class ArtStylePromptZH(CategoryPromptBase):
    """Chinese Art Style prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選"
    
    AVAILABLE_THEMES = [
        ("      抽象", "abstract"),
        ("      概念藝術", "concept_art"),
        ("      極簡", "minimalist"),
        ("      超現實", "surrealism"),
        ("      普普藝術", "pop_art"),
        ("      新藝術", "art_nouveau"),
        ("      裝飾藝術", "art_deco"),
        ("      立體派", "cubism"),
        ("      表現主義", "expressionism"),
        ("      印象派", "impressionism"),
        ("      巴洛克", "baroque"),
        ("      文藝復興", "renaissance"),
        ("      迷幻", "psychedelic"),
        ("      故障藝術", "glitch_art"),
        ("      塗鴉", "graffiti"),
        ("      扁平化", "flat_design"),
        ("      點描派", "pointillism"),
        ("      野獸派", "fauvism"),
        ("      浪漫主義", "romanticism"),
        ("      包浩斯", "bauhaus"),
        ("      哥德藝術", "gothic_art"),
        ("      街頭藝術", "street_art"),
    ]
    
    ALL_THEMES = [
        "abstract", "concept_art", "minimalist", "surrealism", "pop_art",
        "art_nouveau", "art_deco", "cubism", "expressionism", "impressionism",
        "baroque", "renaissance", "psychedelic", "glitch_art", "graffiti",
        "flat_design", "pointillism", "fauvism", "romanticism", "bauhaus",
        "gothic_art", "street_art"
    ]
    
    CATEGORY = "JC Prompt Generator/Art Style 藝術風格"


# =============================================================================
# Sketch & Drawing Category Nodes
# =============================================================================

class SketchPromptEN(CategoryPromptBase):
    """English Sketch & Drawing prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All"
    
    AVAILABLE_THEMES = [
        ("      Pencil Sketch", "pencil_sketch"),
        ("      Charcoal", "charcoal"),
        ("      Ink Drawing", "ink_drawing"),
        ("      Ballpoint Pen", "ballpoint_pen"),
        ("      Blueprint", "blueprint"),
        ("      Technical Drawing", "technical_drawing"),
        ("      Conte Crayon", "conte"),
        ("      Graphite", "graphite"),
        ("      Gesture Drawing", "gesture"),
        ("      Stippling", "stippling"),
        ("      Calligraphy", "calligraphy"),
    ]
    
    ALL_THEMES = [
        "pencil_sketch", "charcoal", "ink_drawing", "ballpoint_pen",
        "blueprint", "technical_drawing", "conte", "graphite",
        "gesture", "stippling", "calligraphy"
    ]
    
    CATEGORY = "JC Prompt Generator/Sketch 素描線稿"


class SketchPromptZH(CategoryPromptBase):
    """Chinese Sketch & Drawing prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選"
    
    AVAILABLE_THEMES = [
        ("      鉛筆素描", "pencil_sketch"),
        ("      炭筆", "charcoal"),
        ("      墨水線稿", "ink_drawing"),
        ("      原子筆畫", "ballpoint_pen"),
        ("      藍圖", "blueprint"),
        ("      技術圖", "technical_drawing"),
        ("      康特筆", "conte"),
        ("      石墨畫", "graphite"),
        ("      速寫", "gesture"),
        ("      點描素描", "stippling"),
        ("      書法線條", "calligraphy"),
    ]
    
    ALL_THEMES = [
        "pencil_sketch", "charcoal", "ink_drawing", "ballpoint_pen",
        "blueprint", "technical_drawing", "conte", "graphite",
        "gesture", "stippling", "calligraphy"
    ]
    
    CATEGORY = "JC Prompt Generator/Sketch 素描線稿"


# =============================================================================
# Painting Category Nodes
# =============================================================================

class PaintingPromptEN(CategoryPromptBase):
    """English Painting prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All"
    
    AVAILABLE_THEMES = [
        ("      Oil Painting", "oil_painting"),
        ("      Watercolor", "watercolor"),
        ("      Acrylic", "acrylic"),
        ("      Gouache", "gouache"),
        ("      Ink Wash", "ink_wash"),
        ("      Pastel", "pastel"),
        ("      Colored Pencil", "colored_pencil"),
        ("      Spray Paint", "spray_paint"),
        ("      Crayon", "crayon"),
        ("      Fresco", "fresco"),
        ("      Tempera", "tempera"),
        ("      Encaustic", "encaustic"),
        ("      Digital Painting", "digital_painting"),
        ("      Mixed Media", "mixed_media"),
        ("      Impasto", "impasto"),
    ]
    
    ALL_THEMES = [
        "oil_painting", "watercolor", "acrylic", "gouache", "ink_wash",
        "pastel", "colored_pencil", "spray_paint", "crayon",
        "fresco", "tempera", "encaustic", "digital_painting",
        "mixed_media", "impasto"
    ]
    
    CATEGORY = "JC Prompt Generator/Painting 繪畫媒材"


class PaintingPromptZH(CategoryPromptBase):
    """Chinese Painting prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選"
    
    AVAILABLE_THEMES = [
        ("      油畫", "oil_painting"),
        ("      水彩", "watercolor"),
        ("      壓克力", "acrylic"),
        ("      不透明水彩", "gouache"),
        ("      水墨", "ink_wash"),
        ("      粉彩", "pastel"),
        ("      色鉛筆", "colored_pencil"),
        ("      噴漆", "spray_paint"),
        ("      蠟筆", "crayon"),
        ("      濕壁畫", "fresco"),
        ("      蛋彩畫", "tempera"),
        ("      蠟畫", "encaustic"),
        ("      數位繪畫", "digital_painting"),
        ("      複合媒材", "mixed_media"),
        ("      厚塗法", "impasto"),
    ]
    
    ALL_THEMES = [
        "oil_painting", "watercolor", "acrylic", "gouache", "ink_wash",
        "pastel", "colored_pencil", "spray_paint", "crayon",
        "fresco", "tempera", "encaustic", "digital_painting",
        "mixed_media", "impasto"
    ]
    
    CATEGORY = "JC Prompt Generator/Painting 繪畫媒材"


# =============================================================================
# Photography Category Nodes
# =============================================================================

class PhotographyPromptEN(CategoryPromptBase):
    """English Photography prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All"
    
    AVAILABLE_THEMES = [
        ("      Cinematic", "cinematic"),
        ("      Studio Photo", "studio_photo"),
        ("      Street Photography", "street_photo"),
        ("      Documentary", "documentary"),
        ("      Macro", "macro"),
        ("      Long Exposure", "long_exposure"),
        ("      Aerial Drone", "aerial_drone"),
        ("      Tilt Shift", "tilt_shift"),
        ("      Bokeh", "bokeh"),
        ("      Double Exposure", "double_exposure"),
        ("      HDR", "hdr"),
        ("      Black & White", "black_white"),
        ("      Film Grain", "film_grain"),
        ("      Food Photography", "food_photo"),
        ("      Sports Photography", "sports_photo"),
        ("      Wildlife Photography", "wildlife_photo"),
        ("      Golden Hour", "golden_hour"),
        ("      Blue Hour", "blue_hour"),
        ("      Silhouette", "silhouette"),
    ]
    
    ALL_THEMES = [
        "cinematic", "studio_photo", "street_photo", "documentary", "macro",
        "long_exposure", "aerial_drone", "tilt_shift", "bokeh", "double_exposure",
        "hdr", "black_white", "film_grain", "food_photo", "sports_photo",
        "wildlife_photo", "golden_hour", "blue_hour", "silhouette"
    ]
    
    CATEGORY = "JC Prompt Generator/Photography 攝影"


class PhotographyPromptZH(CategoryPromptBase):
    """Chinese Photography prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選"
    
    AVAILABLE_THEMES = [
        ("      電影感", "cinematic"),
        ("      棚拍", "studio_photo"),
        ("      街拍", "street_photo"),
        ("      紀實", "documentary"),
        ("      微距", "macro"),
        ("      長曝光", "long_exposure"),
        ("      空拍", "aerial_drone"),
        ("      移軸", "tilt_shift"),
        ("      散景", "bokeh"),
        ("      雙重曝光", "double_exposure"),
        ("      HDR", "hdr"),
        ("      黑白", "black_white"),
        ("      底片", "film_grain"),
        ("      美食攝影", "food_photo"),
        ("      運動攝影", "sports_photo"),
        ("      野生動物", "wildlife_photo"),
        ("      黃金時刻", "golden_hour"),
        ("      藍調時刻", "blue_hour"),
        ("      剪影", "silhouette"),
    ]
    
    ALL_THEMES = [
        "cinematic", "studio_photo", "street_photo", "documentary", "macro",
        "long_exposure", "aerial_drone", "tilt_shift", "bokeh", "double_exposure",
        "hdr", "black_white", "film_grain", "food_photo", "sports_photo",
        "wildlife_photo", "golden_hour", "blue_hour", "silhouette"
    ]
    
    CATEGORY = "JC Prompt Generator/Photography 攝影"


# =============================================================================
# Portrait & People Category Nodes
# =============================================================================

class PortraitPromptEN(CategoryPromptBase):
    """English Portrait & People prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All"
    
    AVAILABLE_THEMES = [
        # Classic
        ("      Classic Portrait", "classic_portrait"),
        ("      Fine Art Portrait", "fine_art_portrait"),
        ("      Environmental Portrait", "environmental_portrait"),
        # Mood
        ("      Moody Portrait", "moody_portrait"),
        ("      Dramatic Portrait", "dramatic_portrait"),
        ("      Ethereal", "ethereal"),
        # Commercial
        ("      Fashion", "fashion"),
        ("      Beauty", "beauty"),
        ("      Editorial", "editorial"),
        ("      Corporate Headshot", "corporate"),
        ("      Glamour", "glamour"),
        # Lifestyle
        ("      Lifestyle", "lifestyle"),
        ("      Fitness", "fitness"),
        ("      Boudoir", "boudoir"),
        ("      Cosplay", "cosplay"),
        ("      Maternity", "maternity"),
        # People
        ("      Headshot", "headshot"),
        ("      Couple", "couple"),
        ("      Group Photo", "group_photo"),
        # Style Variations
        ("      Street Style", "street_style"),
        ("      Vintage Portrait", "vintage_portrait"),
        ("      Candid Portrait", "candid_portrait"),
        ("      Character Portrait", "character_portrait"),
        ("      Film Portrait", "film_portrait"),
    ]
    
    ALL_THEMES = [
        "classic_portrait", "fine_art_portrait", "environmental_portrait",
        "moody_portrait", "dramatic_portrait", "ethereal",
        "fashion", "beauty", "editorial", "corporate", "glamour",
        "lifestyle", "fitness", "boudoir", "cosplay", "maternity",
        "headshot", "couple", "group_photo",
        "street_style", "vintage_portrait", "candid_portrait",
        "character_portrait", "film_portrait"
    ]
    
    CATEGORY = "JC Prompt Generator/Portrait 人像"


class PortraitPromptZH(CategoryPromptBase):
    """Chinese Portrait & People prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選"
    
    AVAILABLE_THEMES = [
        # 經典人像
        ("      經典人像", "classic_portrait"),
        ("      藝術人像", "fine_art_portrait"),
        ("      環境人像", "environmental_portrait"),
        # 情緒氛圍
        ("      情緒人像", "moody_portrait"),
        ("      戲劇人像", "dramatic_portrait"),
        ("      空靈夢幻", "ethereal"),
        # 商業/職業
        ("      時尚", "fashion"),
        ("      美妝", "beauty"),
        ("      雜誌風", "editorial"),
        ("      商務形象照", "corporate"),
        ("      魅力寫真", "glamour"),
        # 生活/特殊
        ("      生活風", "lifestyle"),
        ("      健身", "fitness"),
        ("      閨房寫真", "boudoir"),
        ("      角色扮演", "cosplay"),
        ("      孕婦照", "maternity"),
        # 人群/場景
        ("      大頭照", "headshot"),
        ("      情侶照", "couple"),
        ("      團體照", "group_photo"),
        # 風格變化
        ("      街頭風格", "street_style"),
        ("      復古人像", "vintage_portrait"),
        ("      抓拍人像", "candid_portrait"),
        ("      角色人像", "character_portrait"),
        ("      底片人像", "film_portrait"),
    ]
    
    ALL_THEMES = [
        "classic_portrait", "fine_art_portrait", "environmental_portrait",
        "moody_portrait", "dramatic_portrait", "ethereal",
        "fashion", "beauty", "editorial", "corporate", "glamour",
        "lifestyle", "fitness", "boudoir", "cosplay", "maternity",
        "headshot", "couple", "group_photo",
        "street_style", "vintage_portrait", "candid_portrait",
        "character_portrait", "film_portrait"
    ]
    
    CATEGORY = "JC Prompt Generator/Portrait 人像"


# =============================================================================
# Animals & Creatures Category Nodes
# =============================================================================

class AnimalsPromptEN(CategoryPromptBase):
    """English Animals & Creatures prompt generator."""
    
    AVAILABLE_THEMES = [
        # Common Animals
        ("      Cat", "cat"),
        ("      Dog", "dog"),
        ("      Wolf", "wolf"),
        ("      Fox", "fox"),
        ("      Horse", "horse"),
        # Nature & Wildlife
        ("      Wildlife Art", "wildlife_art"),
        ("      Pets", "pets"),
        ("      Birds", "birds"),
        ("      Marine Life", "marine_life"),
        ("      Underwater Creatures", "underwater_creatures"),
        ("      Insects", "insects"),
        # Fantasy Creatures
        ("      Dragon", "dragon"),
        ("      Unicorn", "unicorn"),
        ("      Phoenix", "phoenix"),
        ("      Dinosaur", "dinosaur"),
        ("      Kaiju", "kaiju"),
        ("      Mythical Beasts", "mythical_beasts"),
        ("      Mermaid", "mermaid"),
        ("      Monster", "monster"),
    ]
    
    ALL_THEMES = [
        "cat", "dog", "wolf", "fox", "horse",
        "wildlife_art", "pets", "birds", "marine_life",
        "underwater_creatures", "insects",
        "dragon", "unicorn", "phoenix", "dinosaur",
        "kaiju", "mythical_beasts", "mermaid", "monster"
    ]
    
    SELECT_ALL_LABEL = "✅ Select All Animals"
    CATEGORY = "JC Prompt Generator/Animals 動物生物"


class AnimalsPromptZH(CategoryPromptBase):
    """Chinese Animals & Creatures prompt generator."""
    
    AVAILABLE_THEMES = [
        # 常見動物
        ("      貓咪", "cat"),
        ("      狗狗", "dog"),
        ("      狼", "wolf"),
        ("      狐狸", "fox"),
        ("      馬", "horse"),
        # 自然生態
        ("      野生動物藝術", "wildlife_art"),
        ("      寵物攝影", "pets"),
        ("      鳥類", "birds"),
        ("      海洋生物", "marine_life"),
        ("      深海生物", "underwater_creatures"),
        ("      昆蟲微距", "insects"),
        # 幻想生物
        ("      龍", "dragon"),
        ("      獨角獸", "unicorn"),
        ("      鳳凰", "phoenix"),
        ("      恐龍", "dinosaur"),
        ("      怪獸", "kaiju"),
        ("      神話異獸", "mythical_beasts"),
        ("      人魚", "mermaid"),
        ("      怪物", "monster"),
    ]
    
    ALL_THEMES = [
        "cat", "dog", "wolf", "fox", "horse",
        "wildlife_art", "pets", "birds", "marine_life",
        "underwater_creatures", "insects",
        "dragon", "unicorn", "phoenix", "dinosaur",
        "kaiju", "mythical_beasts", "mermaid", "monster"
    ]
    
    SELECT_ALL_LABEL = "✅ 全選動物生物"
    CATEGORY = "JC Prompt Generator/Animals 動物生物"


# =============================================================================
# Sci-Fi Node
# =============================================================================

class SciFiPromptEN(CategoryPromptBase):
    """English Sci-Fi Prompt Generator Node."""
    
    AVAILABLE_THEMES = [
        ("      Cyberpunk", "cyberpunk"),
        ("      Steampunk", "steampunk"),
        ("      Dieselpunk", "dieselpunk"),
        ("      Atompunk", "atompunk"),
        ("      Solarpunk", "solarpunk"),
        ("      Biopunk", "biopunk"),
        ("      Raypunk", "raypunk"),
        ("      Space Opera", "space_opera"),
        ("      Spacecraft", "spacecraft"),
        ("      Space Station", "space_station"),
        ("      Alien World", "alien_world"),
        ("      Colony Planet", "colony_planet"),
        ("      Futuristic City", "futuristic_city"),
        ("      Neon Future", "neon_future"),
        ("      AI Dystopia", "ai_dystopia"),
        ("      Post Apocalyptic", "post_apocalyptic"),
        ("      Robot", "robot"),
        ("      Retrofuturism", "retrofuturism"),
        ("      Hard Sci-Fi", "hard_scifi"),
        ("      Pulp Sci-Fi", "pulp_scifi"),
    ]
    
    ALL_THEMES = [
        "cyberpunk", "steampunk", "dieselpunk", "atompunk",
        "solarpunk", "biopunk", "raypunk",
        "space_opera", "spacecraft", "space_station",
        "alien_world", "colony_planet",
        "futuristic_city", "neon_future", "ai_dystopia", "post_apocalyptic",
        "robot", "retrofuturism", "hard_scifi", "pulp_scifi"
    ]
    
    SELECT_ALL_LABEL = "✅ Select All Sci-Fi"
    CATEGORY = "JC Prompt Generator/Sci-Fi 科幻"


class SciFiPromptZH(CategoryPromptBase):
    """Chinese Sci-Fi Prompt Generator Node."""
    
    AVAILABLE_THEMES = [
        ("      賽博龐克", "cyberpunk"),
        ("      蒸汽龐克", "steampunk"),
        ("      柴油龐克", "dieselpunk"),
        ("      原子龐克", "atompunk"),
        ("      太陽龐克", "solarpunk"),
        ("      生物龐克", "biopunk"),
        ("      雷槍龐克", "raypunk"),
        ("      太空歌劇", "space_opera"),
        ("      太空船", "spacecraft"),
        ("      太空站", "space_station"),
        ("      外星世界", "alien_world"),
        ("      殖民星球", "colony_planet"),
        ("      未來城市", "futuristic_city"),
        ("      霓虹未來", "neon_future"),
        ("      AI反烏托邦", "ai_dystopia"),
        ("      末日後", "post_apocalyptic"),
        ("      機器人", "robot"),
        ("      復古未來", "retrofuturism"),
        ("      硬科幻", "hard_scifi"),
        ("      通俗科幻", "pulp_scifi"),
    ]
    
    ALL_THEMES = [
        "cyberpunk", "steampunk", "dieselpunk", "atompunk",
        "solarpunk", "biopunk", "raypunk",
        "space_opera", "spacecraft", "space_station",
        "alien_world", "colony_planet",
        "futuristic_city", "neon_future", "ai_dystopia", "post_apocalyptic",
        "robot", "retrofuturism", "hard_scifi", "pulp_scifi"
    ]
    
    SELECT_ALL_LABEL = "✅ 全選科幻"
    CATEGORY = "JC Prompt Generator/Sci-Fi 科幻"


# =============================================================================
# Fantasy Node
# =============================================================================

class FantasyPromptEN(CategoryPromptBase):
    """English Fantasy Prompt Generator Node."""
    
    AVAILABLE_THEMES = [
        ("      Epic Fantasy", "epic_fantasy"),
        ("      Dark Fantasy", "dark_fantasy"),
        ("      High Fantasy", "high_fantasy"),
        ("      Low Fantasy", "low_fantasy"),
        ("      Urban Fantasy", "urban_fantasy"),
        ("      Grimdark", "grimdark"),
        ("      Fairy Tale", "fairy_tale"),
        ("      Sword & Sorcery", "sword_sorcery"),
        ("      Portal Fantasy", "portal_fantasy"),
        ("      Wizard", "wizard"),
        ("      Elven", "elven"),
        ("      Dwarven", "dwarven"),
        ("      Greek Mythology", "greek_mythology"),
        ("      Norse Mythology", "norse_mythology"),
        ("      Celtic Fantasy", "celtic_fantasy"),
        ("      Arabian Fantasy", "arabian_fantasy"),
        ("      Arthurian", "arthurian"),
        ("      Wuxia", "wuxia"),
        ("      Xianxia", "xianxia"),
        ("      Isekai", "isekai"),
    ]
    
    ALL_THEMES = [
        "epic_fantasy", "dark_fantasy", "high_fantasy", "low_fantasy",
        "urban_fantasy", "grimdark", "fairy_tale", "sword_sorcery",
        "portal_fantasy", "wizard", "elven", "dwarven",
        "greek_mythology", "norse_mythology", "celtic_fantasy", "arabian_fantasy",
        "arthurian", "wuxia", "xianxia", "isekai"
    ]
    
    SELECT_ALL_LABEL = "✅ Select All Fantasy"
    CATEGORY = "JC Prompt Generator/Fantasy 奇幻"


class FantasyPromptZH(CategoryPromptBase):
    """Chinese Fantasy Prompt Generator Node."""
    
    AVAILABLE_THEMES = [
        ("      史詩奇幻", "epic_fantasy"),
        ("      暗黑奇幻", "dark_fantasy"),
        ("      高魔奇幻", "high_fantasy"),
        ("      低魔奇幻", "low_fantasy"),
        ("      都市奇幻", "urban_fantasy"),
        ("      黑暗殘酷", "grimdark"),
        ("      童話", "fairy_tale"),
        ("      劍與魔法", "sword_sorcery"),
        ("      穿越奇幻", "portal_fantasy"),
        ("      法師", "wizard"),
        ("      精靈", "elven"),
        ("      矮人", "dwarven"),
        ("      希臘神話", "greek_mythology"),
        ("      北歐神話", "norse_mythology"),
        ("      凱爾特奇幻", "celtic_fantasy"),
        ("      阿拉伯奇幻", "arabian_fantasy"),
        ("      亞瑟王傳說", "arthurian"),
        ("      武俠", "wuxia"),
        ("      仙俠", "xianxia"),
        ("      異世界", "isekai"),
    ]
    
    ALL_THEMES = [
        "epic_fantasy", "dark_fantasy", "high_fantasy", "low_fantasy",
        "urban_fantasy", "grimdark", "fairy_tale", "sword_sorcery",
        "portal_fantasy", "wizard", "elven", "dwarven",
        "greek_mythology", "norse_mythology", "celtic_fantasy", "arabian_fantasy",
        "arthurian", "wuxia", "xianxia", "isekai"
    ]
    
    SELECT_ALL_LABEL = "✅ 全選奇幻"
    CATEGORY = "JC Prompt Generator/Fantasy 奇幻"


# =============================================================================
# Horror & Dark Category Nodes
# =============================================================================

class HorrorPromptEN(CategoryPromptBase):
    """English Horror & Dark prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All Horror"
    
    AVAILABLE_THEMES = [
        # Classic Monsters
        ("      Vampire", "vampire"),
        ("      Werewolf", "werewolf"),
        ("      Zombie", "zombie"),
        ("      Witch", "witch"),
        # Horror Types
        ("      Slasher", "slasher"),
        ("      J-Horror", "j_horror"),
        ("      Psychological", "psychological"),
        ("      Body Horror", "body_horror"),
        ("      Folk Horror", "folk_horror"),
        ("      Survival Horror", "survival_horror"),
        # Gothic & Atmosphere
        ("      Victorian Gothic", "victorian_gothic"),
        ("      Southern Gothic", "southern_gothic"),
        ("      Haunted", "haunted"),
        ("      Nightmare", "nightmare"),
        # Supernatural & Occult
        ("      Lovecraftian", "lovecraftian"),
        ("      Demonic", "demonic"),
        ("      Occult", "occult"),
        ("      Creepypasta", "creepypasta"),
    ]
    
    ALL_THEMES = [
        "vampire", "werewolf", "zombie", "witch",
        "slasher", "j_horror", "psychological", "body_horror",
        "folk_horror", "survival_horror",
        "victorian_gothic", "southern_gothic", "haunted", "nightmare",
        "lovecraftian", "demonic", "occult", "creepypasta"
    ]
    
    CATEGORY = "JC Prompt Generator/Horror 恐怖"


class HorrorPromptZH(CategoryPromptBase):
    """Chinese Horror & Dark prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選恐怖"
    
    AVAILABLE_THEMES = [
        # 經典怪物
        ("      吸血鬼", "vampire"),
        ("      狼人", "werewolf"),
        ("      殭屍", "zombie"),
        ("      女巫", "witch"),
        # 恐怖類型
        ("      砍殺片", "slasher"),
        ("      日式恐怖", "j_horror"),
        ("      心理恐怖", "psychological"),
        ("      身體恐怖", "body_horror"),
        ("      民俗恐怖", "folk_horror"),
        ("      生存恐怖", "survival_horror"),
        # 氛圍美學
        ("      維多利亞哥德", "victorian_gothic"),
        ("      南方哥德", "southern_gothic"),
        ("      鬧鬼", "haunted"),
        ("      夢魘", "nightmare"),
        # 超自然神秘
        ("      克蘇魯", "lovecraftian"),
        ("      惡魔附身", "demonic"),
        ("      神秘學", "occult"),
        ("      網路怪談", "creepypasta"),
    ]
    
    ALL_THEMES = [
        "vampire", "werewolf", "zombie", "witch",
        "slasher", "j_horror", "psychological", "body_horror",
        "folk_horror", "survival_horror",
        "victorian_gothic", "southern_gothic", "haunted", "nightmare",
        "lovecraftian", "demonic", "occult", "creepypasta"
    ]
    
    CATEGORY = "JC Prompt Generator/Horror 恐怖"


# =============================================================================
# Architecture Category Nodes
# =============================================================================

class ArchitecturePromptEN(CategoryPromptBase):
    """English Architecture prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All Architecture"
    
    AVAILABLE_THEMES = [
        # Modern & Contemporary
        ("      Modern Architecture", "modern_architecture"),
        ("      Brutalist", "brutalist"),
        ("      Art Deco Architecture", "art_deco_arch"),
        ("      Skyscraper", "skyscraper"),
        # Historic & Religious
        ("      Gothic Cathedral", "gothic_cathedral"),
        ("      Castle", "castle"),
        ("      Temple", "temple"),
        ("      Victorian House", "victorian_house"),
        # Regional Styles
        ("      Japanese Architecture", "japanese_arch"),
        ("      Mediterranean", "mediterranean_arch"),
        # Infrastructure & Urban
        ("      Bridge", "bridge"),
        ("      Industrial", "industrial_arch"),
        ("      Cityscape", "cityscape"),
        ("      Village", "village"),
        # Interior & Special
        ("      Interior Design", "interior"),
        ("      Abandoned", "abandoned"),
    ]
    
    ALL_THEMES = [
        "modern_architecture", "brutalist", "art_deco_arch", "skyscraper",
        "gothic_cathedral", "castle", "temple", "victorian_house",
        "japanese_arch", "mediterranean_arch",
        "bridge", "industrial_arch", "cityscape", "village",
        "interior", "abandoned"
    ]
    
    CATEGORY = "JC Prompt Generator/Architecture 建築"


class ArchitecturePromptZH(CategoryPromptBase):
    """Chinese Architecture prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選建築"
    
    AVAILABLE_THEMES = [
        # 現代與當代
        ("      現代建築", "modern_architecture"),
        ("      粗獷主義", "brutalist"),
        ("      裝飾藝術建築", "art_deco_arch"),
        ("      摩天大樓", "skyscraper"),
        # 歷史與宗教
        ("      哥德大教堂", "gothic_cathedral"),
        ("      城堡", "castle"),
        ("      神廟", "temple"),
        ("      維多利亞建築", "victorian_house"),
        # 地域風格
        ("      日式建築", "japanese_arch"),
        ("      地中海建築", "mediterranean_arch"),
        # 基礎設施與城市
        ("      橋樑", "bridge"),
        ("      工業建築", "industrial_arch"),
        ("      城市景觀", "cityscape"),
        ("      鄉村", "village"),
        # 室內與特殊
        ("      室內設計", "interior"),
        ("      廢棄建築", "abandoned"),
    ]
    
    ALL_THEMES = [
        "modern_architecture", "brutalist", "art_deco_arch", "skyscraper",
        "gothic_cathedral", "castle", "temple", "victorian_house",
        "japanese_arch", "mediterranean_arch",
        "bridge", "industrial_arch", "cityscape", "village",
        "interior", "abandoned"
    ]
    
    CATEGORY = "JC Prompt Generator/Architecture 建築"


# =============================================================================
# Nature & Landscape Category Nodes
# =============================================================================

class NaturePromptEN(CategoryPromptBase):
    """English Nature & Landscape prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All Nature"
    
    AVAILABLE_THEMES = [
        # Terrain
        ("      Mountains", "mountains"),
        ("      Forest", "forest"),
        ("      Desert", "desert"),
        ("      Canyon", "canyon"),
        ("      Cave", "cave"),
        ("      Arctic", "arctic"),
        ("      Volcano", "volcano"),
        ("      Meadow", "meadow"),
        # Water
        ("      Ocean", "ocean"),
        ("      Underwater", "underwater"),
        ("      Waterfall", "waterfall"),
        ("      Lake", "lake"),
        ("      Coastal", "coastal"),
        # Sky & Atmosphere
        ("      Sunset", "sunset"),
        ("      Sunrise", "sunrise"),
        ("      Night Sky", "night_sky"),
        ("      Aurora", "aurora"),
        ("      Storm", "storm"),
        ("      Fog", "fog"),
        ("      Rainbow", "rainbow"),
        # Seasonal
        ("      Cherry Blossom", "cherry_blossom"),
        ("      Autumn Foliage", "autumn_foliage"),
    ]
    
    ALL_THEMES = [
        "mountains", "forest", "desert", "canyon", "cave", "arctic", "volcano", "meadow",
        "ocean", "underwater", "waterfall", "lake", "coastal",
        "sunset", "sunrise", "night_sky", "aurora", "storm", "fog", "rainbow",
        "cherry_blossom", "autumn_foliage"
    ]
    
    CATEGORY = "JC Prompt Generator/Nature 自然"


class NaturePromptZH(CategoryPromptBase):
    """Chinese Nature & Landscape prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選自然"
    
    AVAILABLE_THEMES = [
        # 地形地貌
        ("      山景", "mountains"),
        ("      森林", "forest"),
        ("      沙漠", "desert"),
        ("      峽谷", "canyon"),
        ("      洞穴", "cave"),
        ("      極地冰原", "arctic"),
        ("      火山", "volcano"),
        ("      草原花田", "meadow"),
        # 水域場景
        ("      海洋", "ocean"),
        ("      水下", "underwater"),
        ("      瀑布", "waterfall"),
        ("      湖泊", "lake"),
        ("      海岸線", "coastal"),
        # 天象景觀
        ("      日落", "sunset"),
        ("      日出", "sunrise"),
        ("      星空", "night_sky"),
        ("      極光", "aurora"),
        ("      風暴", "storm"),
        ("      霧景", "fog"),
        ("      彩虹", "rainbow"),
        # 季節風情
        ("      櫻花", "cherry_blossom"),
        ("      秋楓", "autumn_foliage"),
    ]
    
    ALL_THEMES = [
        "mountains", "forest", "desert", "canyon", "cave", "arctic", "volcano", "meadow",
        "ocean", "underwater", "waterfall", "lake", "coastal",
        "sunset", "sunrise", "night_sky", "aurora", "storm", "fog", "rainbow",
        "cherry_blossom", "autumn_foliage"
    ]
    
    CATEGORY = "JC Prompt Generator/Nature 自然"


# =============================================================================
# Holidays Category Nodes
# =============================================================================

class HolidaysPromptEN(CategoryPromptBase):
    """English Holidays prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All Holidays"
    
    AVAILABLE_THEMES = [
        # Western (Global)
        ("      Western - Christmas", "christmas"),
        ("      Western - Valentine", "valentine"),
        ("      Western - New Year", "new_year"),
        ("      Western - Easter", "easter"),
        # USA
        ("      USA - Halloween", "halloween"),
        ("      USA - Thanksgiving", "thanksgiving"),
        ("      USA - Mardi Gras", "mardi_gras"),
        ("      USA - Independence Day", "independence_day"),
        # China
        ("      China - Chinese New Year", "chinese_new_year"),
        ("      China - Mid Autumn", "mid_autumn"),
        ("      China - Dragon Boat", "dragon_boat"),
        ("      China - Lantern Festival", "lantern_festival"),
        ("      China - Qixi", "qixi"),
        ("      China - Ice Festival", "ice_festival"),
        # Taiwan
        ("      Taiwan - Sky Lantern", "sky_lantern"),
        # India
        ("      India - Diwali", "diwali"),
        ("      India - Holi", "holi"),
        # Japan
        ("      Japan - Obon", "obon"),
        # Other Countries
        ("      Ireland - St. Patrick's", "st_patricks"),
        ("      Germany - Oktoberfest", "oktoberfest"),
        ("      Thailand - Songkran", "songkran"),
        ("      Mexico - Day of Dead", "day_of_dead"),
        ("      Brazil - Carnival", "carnival"),
        ("      Italy - Venetian Carnival", "venetian_carnival"),
        ("      Islamic - Eid", "eid"),
        ("      Jewish - Hanukkah", "hanukkah"),
    ]
    
    ALL_THEMES = [
        "christmas", "halloween", "valentine", "new_year", "easter",
        "thanksgiving", "st_patricks", "mardi_gras", "independence_day", "oktoberfest",
        "chinese_new_year", "mid_autumn", "dragon_boat", "lantern_festival", "qixi", "sky_lantern",
        "diwali", "holi", "songkran", "obon",
        "eid", "hanukkah", "day_of_dead", "carnival", "venetian_carnival", "ice_festival"
    ]
    
    CATEGORY = "JC Prompt Generator/Holidays 節日"


class HolidaysPromptZH(CategoryPromptBase):
    """Chinese Holidays prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選節日"
    
    AVAILABLE_THEMES = [
        # 西方（全球）
        ("      西方 - 聖誕節", "christmas"),
        ("      西方 - 情人節", "valentine"),
        ("      西方 - 新年", "new_year"),
        ("      西方 - 復活節", "easter"),
        # 美國
        ("      美國 - 萬聖節", "halloween"),
        ("      美國 - 感恩節", "thanksgiving"),
        ("      美國 - 狂歡節", "mardi_gras"),
        ("      美國 - 獨立日", "independence_day"),
        # 中國
        ("      中國 - 農曆新年", "chinese_new_year"),
        ("      中國 - 中秋節", "mid_autumn"),
        ("      中國 - 端午節", "dragon_boat"),
        ("      中國 - 元宵節", "lantern_festival"),
        ("      中國 - 七夕", "qixi"),
        ("      中國 - 冰雪節", "ice_festival"),
        # 台灣
        ("      台灣 - 天燈節", "sky_lantern"),
        # 印度
        ("      印度 - 排燈節", "diwali"),
        ("      印度 - 灑紅節", "holi"),
        # 日本
        ("      日本 - 盂蘭盆節", "obon"),
        # 其他國家
        ("      愛爾蘭 - 聖派翠克節", "st_patricks"),
        ("      德國 - 啤酒節", "oktoberfest"),
        ("      泰國 - 潑水節", "songkran"),
        ("      墨西哥 - 亡靈節", "day_of_dead"),
        ("      巴西 - 嘉年華", "carnival"),
        ("      義大利 - 威尼斯面具節", "venetian_carnival"),
        ("      伊斯蘭 - 開齋節", "eid"),
        ("      猶太 - 光明節", "hanukkah"),
    ]
    
    ALL_THEMES = [
        "christmas", "halloween", "valentine", "new_year", "easter",
        "thanksgiving", "st_patricks", "mardi_gras", "independence_day", "oktoberfest",
        "chinese_new_year", "mid_autumn", "dragon_boat", "lantern_festival", "qixi", "sky_lantern",
        "diwali", "holi", "songkran", "obon",
        "eid", "hanukkah", "day_of_dead", "carnival", "venetian_carnival", "ice_festival"
    ]
    
    CATEGORY = "JC Prompt Generator/Holidays 節日"


# =============================================================================
# Retro Category Nodes
# =============================================================================

class RetroPromptEN(CategoryPromptBase):
    """English Retro prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All Retro"
    
    AVAILABLE_THEMES = [
        ("      Retro 50s", "retro_50s"),
        ("      Retro 60s", "retro_60s"),
        ("      Retro 70s", "retro_70s"),
        ("      Retro 80s", "retro_80s"),
        ("      Retro 90s", "retro_90s"),
        ("      Y2K", "y2k"),
        ("      Vaporwave", "vaporwave"),
    ]
    
    ALL_THEMES = ["retro_50s", "retro_60s", "retro_70s", "retro_80s", "retro_90s", "y2k", "vaporwave"]
    
    CATEGORY = "JC Prompt Generator/Retro 復古"


class RetroPromptZH(CategoryPromptBase):
    """Chinese Retro prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選復古"
    
    AVAILABLE_THEMES = [
        ("      50年代", "retro_50s"),
        ("      60年代", "retro_60s"),
        ("      70年代", "retro_70s"),
        ("      80年代", "retro_80s"),
        ("      90年代", "retro_90s"),
        ("      千禧年", "y2k"),
        ("      蒸氣波", "vaporwave"),
    ]
    
    ALL_THEMES = ["retro_50s", "retro_60s", "retro_70s", "retro_80s", "retro_90s", "y2k", "vaporwave"]
    
    CATEGORY = "JC Prompt Generator/Retro 復古"


# =============================================================================
# Cultural Category Nodes
# =============================================================================

class CulturalPromptEN(CategoryPromptBase):
    """English Cultural prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All Cultural"
    
    AVAILABLE_THEMES = [
        # East Asia
        ("      Chinese", "chinese"),
        ("      Japanese", "japanese"),
        ("      Korean", "korean"),
        ("      Thai", "thai"),
        # South Asia & Middle East
        ("      Indian", "indian"),
        ("      Arabic", "arabic"),
        ("      Persian", "persian"),
        ("      Turkish", "turkish"),
        # Africa & Mediterranean
        ("      Egyptian", "egyptian"),
        ("      Moroccan", "moroccan"),
        ("      African", "african"),
        ("      Greek", "greek"),
        ("      Mediterranean", "mediterranean"),
        # Europe & Americas
        ("      Russian", "russian"),
        ("      Nordic", "nordic"),
        ("      Celtic", "celtic"),
        ("      Mexican", "mexican"),
    ]
    
    ALL_THEMES = [
        "chinese", "japanese", "korean", "thai",
        "indian", "arabic", "persian", "turkish",
        "egyptian", "moroccan", "african", "greek", "mediterranean",
        "russian", "nordic", "celtic", "mexican"
    ]
    
    CATEGORY = "JC Prompt Generator/Cultural 文化"


class CulturalPromptZH(CategoryPromptBase):
    """Chinese Cultural prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選文化"
    
    AVAILABLE_THEMES = [
        # 東亞
        ("      中式", "chinese"),
        ("      日式", "japanese"),
        ("      韓式", "korean"),
        ("      泰式", "thai"),
        # 南亞與中東
        ("      印度", "indian"),
        ("      阿拉伯", "arabic"),
        ("      波斯", "persian"),
        ("      土耳其", "turkish"),
        # 非洲與地中海
        ("      埃及", "egyptian"),
        ("      摩洛哥", "moroccan"),
        ("      非洲", "african"),
        ("      希臘", "greek"),
        ("      地中海", "mediterranean"),
        # 歐洲與美洲
        ("      俄羅斯", "russian"),
        ("      北歐", "nordic"),
        ("      凱爾特", "celtic"),
        ("      墨西哥", "mexican"),
    ]
    
    ALL_THEMES = [
        "chinese", "japanese", "korean", "thai",
        "indian", "arabic", "persian", "turkish",
        "egyptian", "moroccan", "african", "greek", "mediterranean",
        "russian", "nordic", "celtic", "mexican"
    ]
    
    CATEGORY = "JC Prompt Generator/Cultural 文化"


# =============================================================================
# Commercial Category Nodes
# =============================================================================

class CommercialPromptEN(CategoryPromptBase):
    """English Commercial prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All Commercial"
    
    AVAILABLE_THEMES = [
        # Product & Food
        ("      Product Photo", "product"),
        ("      Food Photo", "food"),
        ("      Beverage", "beverage"),
        ("      E-commerce", "ecommerce"),
        # Business
        ("      Advertising", "advertising"),
        ("      Real Estate", "real_estate"),
        ("      Corporate", "corporate"),
        # Design & Media
        ("      Book Cover", "book_cover"),
        ("      Album Cover", "album_cover"),
        ("      Poster", "poster"),
        ("      Mockup", "mockup"),
        ("      Packaging", "packaging"),
        # Specialty
        ("      Fashion", "fashion"),
        ("      Jewelry", "jewelry"),
        ("      Cosmetics", "cosmetics"),
        ("      Automotive", "automotive"),
    ]
    
    ALL_THEMES = [
        "product", "food", "beverage", "ecommerce",
        "advertising", "real_estate", "corporate",
        "book_cover", "album_cover", "poster", "mockup", "packaging",
        "fashion", "jewelry", "cosmetics", "automotive"
    ]
    
    CATEGORY = "JC Prompt Generator/Commercial 商業"


class CommercialPromptZH(CategoryPromptBase):
    """Chinese Commercial prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選商業"
    
    AVAILABLE_THEMES = [
        # 產品與美食
        ("      產品攝影", "product"),
        ("      美食攝影", "food"),
        ("      飲料攝影", "beverage"),
        ("      電商", "ecommerce"),
        # 商務
        ("      廣告", "advertising"),
        ("      房產", "real_estate"),
        ("      企業", "corporate"),
        # 設計與媒體
        ("      書籍封面", "book_cover"),
        ("      專輯封面", "album_cover"),
        ("      海報", "poster"),
        ("      模型展示", "mockup"),
        ("      包裝", "packaging"),
        # 專業攝影
        ("      時尚攝影", "fashion"),
        ("      珠寶攝影", "jewelry"),
        ("      化妝品攝影", "cosmetics"),
        ("      汽車攝影", "automotive"),
    ]
    
    ALL_THEMES = [
        "product", "food", "beverage", "ecommerce",
        "advertising", "real_estate", "corporate",
        "book_cover", "album_cover", "poster", "mockup", "packaging",
        "fashion", "jewelry", "cosmetics", "automotive"
    ]
    
    CATEGORY = "JC Prompt Generator/Commercial 商業"


# =============================================================================
# Gaming & Digital Category Nodes
# =============================================================================

class GamingPromptEN(CategoryPromptBase):
    """English Gaming & Digital prompt generator."""
    
    SELECT_ALL_LABEL = "✅ Select All Gaming"
    
    AVAILABLE_THEMES = [
        ("      Pixel Art", "pixel_art"),
        ("      Game UI", "game_ui"),
        ("      Character Sheet", "character_sheet"),
        ("      Splash Art", "splash_art"),
        ("      Game Icon", "game_icon"),
        ("      Card Art", "card_art"),
        ("      Emote/Sticker", "emote"),
        ("      Game Background", "game_bg"),
    ]
    
    ALL_THEMES = [
        "pixel_art", "game_ui", "character_sheet", "splash_art",
        "game_icon", "card_art", "emote", "game_bg"
    ]
    
    CATEGORY = "JC Prompt Generator/Gaming 遊戲"


class GamingPromptZH(CategoryPromptBase):
    """Chinese Gaming & Digital prompt generator."""
    
    SELECT_ALL_LABEL = "✅ 全選遊戲"
    
    AVAILABLE_THEMES = [
        ("      像素藝術", "pixel_art"),
        ("      遊戲介面", "game_ui"),
        ("      角色設定圖", "character_sheet"),
        ("      遊戲立繪", "splash_art"),
        ("      遊戲圖標", "game_icon"),
        ("      卡牌插畫", "card_art"),
        ("      表情貼圖", "emote"),
        ("      遊戲背景", "game_bg"),
    ]
    
    ALL_THEMES = [
        "pixel_art", "game_ui", "character_sheet", "splash_art",
        "game_icon", "card_art", "emote", "game_bg"
    ]
    
    CATEGORY = "JC Prompt Generator/Gaming 遊戲"


# =============================================================================
# All Categories Combined Node
# =============================================================================

class AllCategoriesBase:
    """Base class for all categories combined node."""
    
    # Override in subclasses
    CATEGORY_LABELS = {}  # Widget label -> internal category key
    CATEGORY = "JC Prompt Generator/All 全部類別"
    
    def __init__(self):
        self.config_manager = ConfigManager()
        self.theme_registry = ThemeRegistry(self.config_manager)
    
    # All category themes mapping
    CATEGORY_THEMES = {
        "animation": AnimationPromptEN.ALL_THEMES,
        "art_style": ArtStylePromptEN.ALL_THEMES,
        "sketch": SketchPromptEN.ALL_THEMES,
        "painting": PaintingPromptEN.ALL_THEMES,
        "photography": PhotographyPromptEN.ALL_THEMES,
        "portrait": PortraitPromptEN.ALL_THEMES,
        "animals": AnimalsPromptEN.ALL_THEMES,
        "scifi": SciFiPromptEN.ALL_THEMES,
        "fantasy": FantasyPromptEN.ALL_THEMES,
        "horror": HorrorPromptEN.ALL_THEMES,
        "architecture": ArchitecturePromptEN.ALL_THEMES,
        "nature": NaturePromptEN.ALL_THEMES,
        "holidays": HolidaysPromptEN.ALL_THEMES,
        "retro": RetroPromptEN.ALL_THEMES,
        "cultural": CulturalPromptEN.ALL_THEMES,
        "commercial": CommercialPromptEN.ALL_THEMES,
        "gaming": GamingPromptEN.ALL_THEMES,
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        widgets = {}
        for label in cls.CATEGORY_LABELS.keys():
            widgets[label] = ("BOOLEAN", {"default": False})
        
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "batch_count": ("INT", {"default": 1, "min": 1, "max": 100}),
            },
            "optional": widgets
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("prompts", "theme_names")
    OUTPUT_IS_LIST = (True, True)
    FUNCTION = "generate"
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        import time
        return time.time()
    
    def generate(
        self,
        seed: int = 0,
        batch_count: int = 1,
        **kwargs
    ) -> Tuple[List[str], List[str]]:
        """Generate prompts from all selected categories."""
        
        # Collect all themes from enabled categories
        enabled_themes = []
        for widget_name, category_key in self.CATEGORY_LABELS.items():
            if kwargs.get(widget_name, False):
                themes = self.CATEGORY_THEMES.get(category_key, [])
                enabled_themes.extend(themes)
        
        if not enabled_themes:
            raise ValueError("⚠️ 請至少選擇一個類別！\n\nPlease select at least one category!")
        
        # Generate prompts
        prompts = []
        theme_names = []
        prompt_index = 0
        
        for theme_name in enabled_themes:
            handler = self.theme_registry.get_handler(theme_name)
            if not handler:
                prompts.append(f"Error: Handler not found for {theme_name}")
                theme_names.append(theme_name)
                prompt_index += 1
                continue
            
            for j in range(batch_count):
                # Use larger seed spacing to ensure different random sequences
                # Different themes: prompt_index * 10000
                # Different batches within same theme: j * 1000
                unique_seed = (seed + prompt_index * 10000 + j * 1000) % 0xffffffffffffffff
                self.config_manager.set_seed(unique_seed)
                
                try:
                    components = handler.generate(
                        custom_subject="",
                        custom_location="",
                        include_environment=True,
                        include_style=True,
                        include_effects=True
                    )
                    
                    prompt_parts = []
                    for key in ["subject", "environment", "style", "effects"]:
                        if key in components and components[key]:
                            prompt_parts.append(components[key])
                    
                    prompt = ", ".join(prompt_parts)
                    prompts.append(prompt)
                    theme_names.append(theme_name)
                    
                except Exception as e:
                    prompts.append(f"Error generating {theme_name}: {str(e)}")
                    theme_names.append(theme_name)
            
            prompt_index += 1
        
        return (prompts, theme_names)


class AllCategoriesPromptEN(AllCategoriesBase):
    """English version - All categories combined."""
    
    CATEGORY_LABELS = {
        "[17] ✅ All Animation": "animation",
        "[22] ✅ All Art Styles": "art_style",
        "[11] ✅ All Sketch": "sketch",
        "[15] ✅ All Painting": "painting",
        "[19] ✅ All Photography": "photography",
        "[24] ✅ All Portrait": "portrait",
        "[19] ✅ All Animals": "animals",
        "[20] ✅ All Sci-Fi": "scifi",
        "[20] ✅ All Fantasy": "fantasy",
        "[18] ✅ All Horror": "horror",
        "[16] ✅ All Architecture": "architecture",
        "[22] ✅ All Nature": "nature",
        "[26] ✅ All Holidays": "holidays",
        "[07] ✅ All Retro": "retro",
        "[17] ✅ All Cultural": "cultural",
        "[16] ✅ All Commercial": "commercial",
        "[08] ✅ All Gaming": "gaming",
    }
    
    CATEGORY = "JC Prompt Generator/All 全部類別"


class AllCategoriesPromptZH(AllCategoriesBase):
    """Chinese version - All categories combined."""
    
    CATEGORY_LABELS = {
        "[17] ✅ 全選動畫": "animation",
        "[22] ✅ 全選藝術風格": "art_style",
        "[11] ✅ 全選素描線稿": "sketch",
        "[15] ✅ 全選繪畫媒材": "painting",
        "[19] ✅ 全選攝影類型": "photography",
        "[24] ✅ 全選人像人物": "portrait",
        "[19] ✅ 全選動物生物": "animals",
        "[20] ✅ 全選科幻未來": "scifi",
        "[20] ✅ 全選奇幻魔法": "fantasy",
        "[18] ✅ 全選恐怖黑暗": "horror",
        "[16] ✅ 全選建築空間": "architecture",
        "[22] ✅ 全選自然風景": "nature",
        "[26] ✅ 全選節日主題": "holidays",
        "[07] ✅ 全選復古年代": "retro",
        "[17] ✅ 全選文化地區": "cultural",
        "[16] ✅ 全選商業用途": "commercial",
        "[08] ✅ 全選遊戲數位": "gaming",
    }
    
    CATEGORY = "JC Prompt Generator/All 全部類別"


# =============================================================================
# Node Registration
# =============================================================================

NODE_CLASS_MAPPINGS = {
    # All Categories Combined
    "JC_AllCategories_EN": AllCategoriesPromptEN,
    "JC_AllCategories_ZH": AllCategoriesPromptZH,
    # Animation
    "JC_Animation_EN": AnimationPromptEN,
    "JC_Animation_ZH": AnimationPromptZH,
    # Art Style
    "JC_ArtStyle_EN": ArtStylePromptEN,
    "JC_ArtStyle_ZH": ArtStylePromptZH,
    # Sketch
    "JC_Sketch_EN": SketchPromptEN,
    "JC_Sketch_ZH": SketchPromptZH,
    # Painting
    "JC_Painting_EN": PaintingPromptEN,
    "JC_Painting_ZH": PaintingPromptZH,
    # Photography
    "JC_Photography_EN": PhotographyPromptEN,
    "JC_Photography_ZH": PhotographyPromptZH,
    # Portrait
    "JC_Portrait_EN": PortraitPromptEN,
    "JC_Portrait_ZH": PortraitPromptZH,
    # Animals
    "JC_Animals_EN": AnimalsPromptEN,
    "JC_Animals_ZH": AnimalsPromptZH,
    # Sci-Fi
    "JC_SciFi_EN": SciFiPromptEN,
    "JC_SciFi_ZH": SciFiPromptZH,
    # Fantasy
    "JC_Fantasy_EN": FantasyPromptEN,
    "JC_Fantasy_ZH": FantasyPromptZH,
    # Horror
    "JC_Horror_EN": HorrorPromptEN,
    "JC_Horror_ZH": HorrorPromptZH,
    # Architecture
    "JC_Architecture_EN": ArchitecturePromptEN,
    "JC_Architecture_ZH": ArchitecturePromptZH,
    # Nature
    "JC_Nature_EN": NaturePromptEN,
    "JC_Nature_ZH": NaturePromptZH,
    # Holidays
    "JC_Holidays_EN": HolidaysPromptEN,
    "JC_Holidays_ZH": HolidaysPromptZH,
    # Retro
    "JC_Retro_EN": RetroPromptEN,
    "JC_Retro_ZH": RetroPromptZH,
    # Cultural
    "JC_Cultural_EN": CulturalPromptEN,
    "JC_Cultural_ZH": CulturalPromptZH,
    # Commercial
    "JC_Commercial_EN": CommercialPromptEN,
    "JC_Commercial_ZH": CommercialPromptZH,
    # Gaming
    "JC_Gaming_EN": GamingPromptEN,
    "JC_Gaming_ZH": GamingPromptZH,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # All Categories Combined
    "JC_AllCategories_EN": "🌟 JC Prompt - All Categories",
    "JC_AllCategories_ZH": "🌟 JC 提示詞 - 全部類別",
    # Animation
    "JC_Animation_EN": "🎬 JC Prompt - Animation",
    "JC_Animation_ZH": "🎬 JC 提示詞 - 動畫",
    # Art Style
    "JC_ArtStyle_EN": "🎨 JC Prompt - Art Style",
    "JC_ArtStyle_ZH": "🎨 JC 提示詞 - 藝術風格",
    # Sketch
    "JC_Sketch_EN": "✏️ JC Prompt - Sketch",
    "JC_Sketch_ZH": "✏️ JC 提示詞 - 素描線稿",
    # Painting
    "JC_Painting_EN": "🖼️ JC Prompt - Painting",
    "JC_Painting_ZH": "🖼️ JC 提示詞 - 繪畫媒材",
    # Photography
    "JC_Photography_EN": "📸 JC Prompt - Photography",
    "JC_Photography_ZH": "📸 JC 提示詞 - 攝影",
    # Portrait
    "JC_Portrait_EN": "👩 JC Prompt - Portrait",
    "JC_Portrait_ZH": "👩 JC 提示詞 - 人像",
    # Animals
    "JC_Animals_EN": "🐾 JC Prompt - Animals",
    "JC_Animals_ZH": "🐾 JC 提示詞 - 動物生物",
    # Sci-Fi
    "JC_SciFi_EN": "🚀 JC Prompt - Sci-Fi",
    "JC_SciFi_ZH": "🚀 JC 提示詞 - 科幻",
    # Fantasy
    "JC_Fantasy_EN": "⚔️ JC Prompt - Fantasy",
    "JC_Fantasy_ZH": "⚔️ JC 提示詞 - 奇幻",
    # Horror
    "JC_Horror_EN": "👻 JC Prompt - Horror",
    "JC_Horror_ZH": "👻 JC 提示詞 - 恐怖",
    # Architecture
    "JC_Architecture_EN": "🏛️ JC Prompt - Architecture",
    "JC_Architecture_ZH": "🏛️ JC 提示詞 - 建築",
    # Nature
    "JC_Nature_EN": "🌿 JC Prompt - Nature",
    "JC_Nature_ZH": "🌿 JC 提示詞 - 自然",
    # Holidays
    "JC_Holidays_EN": "🎄 JC Prompt - Holidays",
    "JC_Holidays_ZH": "🎄 JC 提示詞 - 節日",
    # Retro
    "JC_Retro_EN": "🕹️ JC Prompt - Retro",
    "JC_Retro_ZH": "🕹️ JC 提示詞 - 復古",
    # Cultural
    "JC_Cultural_EN": "🌍 JC Prompt - Cultural",
    "JC_Cultural_ZH": "🌍 JC 提示詞 - 文化",
    # Commercial
    "JC_Commercial_EN": "💼 JC Prompt - Commercial",
    "JC_Commercial_ZH": "💼 JC 提示詞 - 商業",
    # Gaming
    "JC_Gaming_EN": "🎮 JC Prompt - Gaming",
    "JC_Gaming_ZH": "🎮 JC 提示詞 - 遊戲",
}

