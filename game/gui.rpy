## gui.rpy
## GUI Configuration for THE VISIONARY

init offset = -2

## Colors - Sci-fi/philosophical theme
define gui.accent_color = '#00ff88'
define gui.idle_color = '#888888'
define gui.idle_small_color = '#aaaaaa'
define gui.hover_color = '#00ffaa'
define gui.selected_color = '#00ff88'
define gui.insensitive_color = '#444444'
define gui.muted_color = '#006644'
define gui.hover_muted_color = '#008866'
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'

## Fonts (using defaults - replace with custom fonts later)
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

## Font sizes
define gui.text_size = 24
define gui.name_text_size = 30
define gui.interface_text_size = 24
define gui.label_text_size = 30
define gui.notify_text_size = 20
define gui.title_text_size = 60

## Main and Game Menu backgrounds
define gui.main_menu_background = Solid("#0a0a14")
define gui.game_menu_background = Solid("#0a0a14")

## Dialogue window
define gui.textbox_height = 220
define gui.textbox_yalign = 1.0

## Character name placement
define gui.name_xpos = 240
define gui.name_ypos = 0
define gui.name_xalign = 0.0

## Dialogue text placement
define gui.dialogue_xpos = 240
define gui.dialogue_ypos = 60
define gui.dialogue_width = 800

## Choice buttons
define gui.choice_button_width = 800
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 8, 100, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#aaaaaa"
define gui.choice_button_text_hover_color = "#00ff88"
define gui.choice_button_text_selected_color = "#00ffcc"

## Slot buttons (save/load)
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5

## Window icon (placeholder)
define config.window_icon = None

## Dialogue box styling
init python:
    style.say_dialogue = Style(style.default)
    style.say_dialogue.color = "#ffffff"

## Quick menu preferences
define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 18
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_hover_color = gui.accent_color
define gui.quick_button_text_selected_color = gui.accent_color

## Navigation button styling
define gui.navigation_button_width = 225
define gui.navigation_xpos = 40
define gui.navigation_ypos = 80
define gui.navigation_spacing = 4
define gui.navigation_button_borders = Borders(4, 4, 4, 4)

## Scrollbar styling
define gui.scrollbar_size = 12
define gui.scrollbar_tile = False
define gui.scrollbar_borders = Borders(4, 4, 4, 4)

## History styling
define gui.history_height = 140
define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740

## NVL mode styling
define gui.nvl_borders = Borders(0, 10, 0, 20)
define gui.nvl_height = 115
define gui.nvl_spacing = 10
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_width = 780
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

## Mobile-responsive adjustments
init python:
    @renpy.pure
    def gui_preference(name, default):
        return default

## Frame styling for custom windows
define gui.frame_borders = Borders(4, 4, 4, 4)
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)
define gui.skip_frame_borders = Borders(16, 5, 50, 5)
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## Bar styling
define gui.bar_size = 25
define gui.bar_tile = False
define gui.bar_borders = Borders(4, 4, 4, 4)

## Vbar styling
define gui.vbar_borders = Borders(4, 4, 4, 4)

## Slider styling
define gui.slider_size = 25
define gui.slider_tile = False
define gui.slider_borders = Borders(4, 4, 4, 4)

## Vslider styling
define gui.vslider_borders = Borders(4, 4, 4, 4)
