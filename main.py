def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.play(music.built_in_playable_melody(Melodies.PRELUDE),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.ASLEEP)
pins.set_audio_pin(DigitalPin.P16)
music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
    music.PlaybackMode.IN_BACKGROUND)
for index in range(129):
    pins.analog_write_pin(AnalogPin.P0, index * 8 - 1)
    basic.pause(5)
pins.analog_write_pin(AnalogPin.P0, 0)
basic.show_icon(IconNames.HAPPY)
for index2 in range(129):
    pins.analog_write_pin(AnalogPin.P1, index2 * 8 - 1)
    basic.pause(5)
pins.analog_write_pin(AnalogPin.P1, 0)
basic.show_icon(IconNames.STICK_FIGURE)
for index3 in range(129):
    pins.analog_write_pin(AnalogPin.P2, index3 * 8 - 1)
    basic.pause(5)
pins.analog_write_pin(AnalogPin.P2, 0)
basic.show_icon(IconNames.HEART)

def on_forever():
    if input.button_is_pressed(Button.A):
        pins.analog_write_pin(AnalogPin.P0, randint(0, 1023))
        pins.analog_write_pin(AnalogPin.P1, randint(0, 1023))
        pins.analog_write_pin(AnalogPin.P2, randint(0, 1023))
        basic.pause(100)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
    if input.button_is_pressed(Button.B):
        pins.analog_write_pin(AnalogPin.P0, randint(0, 1023))
        pins.analog_write_pin(AnalogPin.P1, randint(0, 1023))
        pins.analog_write_pin(AnalogPin.P2, randint(0, 1023))
        basic.pause(200)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
basic.forever(on_forever)
