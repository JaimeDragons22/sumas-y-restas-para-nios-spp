basic.show_leds("""
    . # # # .
        . . . . #
        . . . # .
        . . # . .
        . # # # #
""")
basic.show_string("Hola 2ºB hoy vamos a hacer sumas y restas para niños, Quereis?")
basic.show_leds("""
    # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
""")
basic.show_string("Creditos a Jaime Sanchez Benavent")
music.play_melody("- - - - - - - - ", 120)
input.button_is_pressed(Button.A)
