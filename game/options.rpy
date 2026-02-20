## options.rpy
## Configuration options for THE VISIONARY

## Game metadata
define config.name = _("THE VISIONARY")
define config.version = "1.0"

define gui.show_name = True
define gui.about = _p("""
THE VISIONARY: A Philosophical Adventure

A game about consciousness, altered states, and human destiny.

Is it ethical to get ideas about humanity's future while high?
""")

## Build configuration
define build.name = "TheVisionary"

## Window settings
define config.screen_width = 1280
define config.screen_height = 720

## Save/Load configuration
define config.save_directory = "TheVisionary-1"
define config.window_title = "THE VISIONARY"

## Sound configuration (placeholders for future audio)
define config.has_sound = False
define config.has_music = False
define config.has_voice = False

## Main and game menu images (placeholders)
define gui.main_menu_background = Solid("#0a0a14")
define gui.game_menu_background = Solid("#0a0a14")

## Text speeds
define config.default_text_cps = 30

## Skip settings
define config.allow_skipping = True
define config.fast_skipping = True

## Auto-forward timing
define config.default_afm_time = 15

## Rollback (undo) visual
define config.rollback_enabled = True

## NVL mode settings
define config.nvl_list_length = None

## Layer configuration
define config.layers = [ 'master', 'transient', 'screens', 'overlay' ]

## Transitions
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.main_game_transition = fade
define config.end_game_transition = fade

## Default transforms
transform center_sprite:
    xalign 0.5
    yalign 1.0

transform right:
    xalign 0.8
    yalign 1.0

transform left:
    xalign 0.2
    yalign 1.0

## Build classification for distribution
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.rpyc', 'archive')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('**', 'archive')
