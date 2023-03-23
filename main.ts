input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Yes)
    basic.pause(100)
    basic.showIcon(IconNames.Diamond)
    basic.pause(100)
    basic.showIcon(IconNames.SmallDiamond)
    basic.showLeds(`
        . . # # .
                . # . . #
                . . . . #
                . . . # .
                . . . # .
    `)
    basic.pause(2000)
    basic.showArrow(ArrowNames.South)
    if (Math.randomBoolean()) {
        basic.showLeds(`
            . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
                        . . . . .
        `)
        music.playMelody("C5 - - - - - - - ", 120)
    } else {
        basic.showLeds(`
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        `)
        music.playMelody("C5 - - - - - - - ", 120)
    }
    
})
