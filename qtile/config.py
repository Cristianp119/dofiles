# *************************** #
# Configuracion de Cristian   #
# *************************** #
from typing import List  
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
# import psutil
import os

mod = "mod4"
terminal = guess_terminal()

colorventana = "#3dfffc"
colorventana_normal = "#4a1154"

keys = [

    # -------- atajos de teclado de rofi -------- #
    Key([mod], "z", lazy.spawn("rofi -show drun")),
    Key([mod], "x", lazy.spawn("rofi -show run")),
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod], "b", lazy.spawn("brave")),
    Key([mod], "f", lazy.spawn("flameshot")),
    Key([mod], "t", lazy.spawn("Thunar")),
    Key([mod, "shift"], "z", lazy.spawn("rofi -show")),


    # Redshift
    # key([mod], "q", lazy.spawn("redshift -O 2400")),
    # key([mod, "shift"], "q", lazy.spawn("redshift -x")),

    # --------       Control BRillo     --------- #
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    
    # -------- control de teclas volumen -------- #
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # --------          Programas        -------- #

    # Key([], "imp", lazy.spawn("flameshot")),


    # -------- control teclas de layouts -------- #
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # -------- control direccion de ventanas -------- #
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If8 current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in [
    "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layouts = [
    # layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_width = 2,
        border_focus = colorventana,
        single_border_width = 0,
        margin = 4,
        # border_normal = colorventana_normal,
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=18,
    padding=5,
)
extension_defaults = widget_defaults.copy()

#  funciones

def icon(text, background):
    return widget.TextBox(
        text = text,
        background = background,
    )


screens = [
    Screen(
        top=bar.Bar(
            [   
                widget.GroupBox(
                    background = "#010308",
                    fontsize = 30,
                    margin = 2.5,
                    padding = 4,
                ),
                widget.TextBox(text = '', background="#010308", foreground="#010308", padding=2, fontsize=85, width=30),
                widget.Prompt(),
                widget.WindowName(
                    format = " ",
                    background = "#010308"
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(text = '', background="#010308", foreground="#51AD59", padding=4, fontsize=85, width=25),
                widget.CheckUpdates(
                    background = "#51AD59",
                    execute = "sudo pacman -Sy",
                    display_format = "  {updates}",
                    no_update_string = '  0',
                    update_interval = 1800,
                ),
                widget.TextBox(text = '', background="#51AD59", foreground="#0a939e", padding= -4, fontsize=85, width=22),
                icon (text = "", background = "#0a939e"),
                widget.Memory(
                    background = "#0a939e",
                    format = '{MemUsed: .0f}·MB',
                    update_interval = 1.0,

                ),
                widget.TextBox(text = '', background="#0a939e", foreground="#6d229c", padding=4, fontsize=85, width=25),
                icon(text = " ", background = "#6d229c"),
                widget.Backlight(
                    background = "#6d229c",
                    backlight_name = "amdgpu_bl1",
                    brightness_file = "/sys/class/backlight/amdgpu_bl1/actual_brightness",
                    max_brightness_file = "/sys/class/backlight/amdgpu_bl1/max_brightness",
                    format = '{percent:2.0%}'
                ),
                widget.TextBox(text = '', background="#6d229c", foreground="#6c0964", padding=-2, fontsize=85, width=25),
                widget.CurrentLayoutIcon( background ="#6c0964", scale = 0.8, padding = 3),
                widget.CurrentLayout(
                    background = "#6c0964"
                ),
                widget.TextBox(text = '', background="#6c0964", foreground="#A21266", padding=4, fontsize=85, width=25),
                icon(text= " ", background="#A21266"),
                widget.Clock(
                       
                            format = '%d/%m/%Y   %H:%M', 
                            background = "#A21266"
                ),
                widget.TextBox(text = '', background="#A21266", foreground="#010308", padding=-3, fontsize=85, width=25),
                widget.Systray(
                    background = "#010308"
                ),
                widget.QuickExit(
                    background = "#010308",
                    default_text = "  "),

                # ---------------------------------------
            ],
            24,
            background = "#0d0c0c"
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"


cmd = [
    "feh --bg-scale /home/manchitas/Imágenes/wallpaper//07.jpg",
    # "picom"
]

for x in cmd:
    os.system(x)
