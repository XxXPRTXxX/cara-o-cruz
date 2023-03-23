def on_button_pressed_a():
    basic.show_icon(IconNames.YES)
    basic.pause(100)
    basic.show_icon(IconNames.DIAMOND)
    basic.pause(100)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_leds("""
        . . # # .
                . # . . #
                . . . . #
                . . . # .
                . . . # .
    """)
    basic.pause(2000)
    basic.show_arrow(ArrowNames.SOUTH)
    if Math.random_boolean():
        basic.show_leds("""
            . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
                        . . . . .
        """)
        music.play_melody("C5 - - - - - - - ", 120)
    else:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
        music.play_melody("C5 - - - - - - - ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)
