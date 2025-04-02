input.onButtonPressed(Button.A, function () {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
})
input.onButtonPressed(Button.AB, function () {
    control.reset()
})
input.onButtonPressed(Button.B, function () {
    music.play(music.builtInPlayableMelody(Melodies.Prelude), music.PlaybackMode.InBackground)
})
pins.setAudioPin(DigitalPin.P16)
music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Entertainer), music.PlaybackMode.InBackground)
basic.showIcon(IconNames.Asleep)
for (let index = 0; index <= 128; index++) {
    pins.analogWritePin(AnalogPin.P0, index * 8 - 1)
    basic.pause(5)
}
pins.analogWritePin(AnalogPin.P0, 0)
basic.showIcon(IconNames.Happy)
for (let index = 0; index <= 128; index++) {
    pins.analogWritePin(AnalogPin.P1, index * 8 - 1)
    basic.pause(5)
}
pins.analogWritePin(AnalogPin.P1, 0)
basic.showIcon(IconNames.StickFigure)
for (let index = 0; index <= 128; index++) {
    pins.analogWritePin(AnalogPin.P2, index * 8 - 1)
    basic.pause(5)
}
pins.analogWritePin(AnalogPin.P2, 0)
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        pins.analogWritePin(AnalogPin.P0, randint(0, 1023))
        pins.analogWritePin(AnalogPin.P1, randint(0, 1023))
        pins.analogWritePin(AnalogPin.P2, randint(0, 1023))
        pins.digitalWritePin(DigitalPin.P8, 1)
        basic.pause(100)
    } else if (input.buttonIsPressed(Button.B)) {
        pins.analogWritePin(AnalogPin.P0, randint(0, 1023))
        pins.analogWritePin(AnalogPin.P1, randint(0, 1023))
        pins.analogWritePin(AnalogPin.P2, randint(0, 1023))
        pins.digitalWritePin(DigitalPin.P9, 1)
        basic.pause(200)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 0)
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P9, 0)
    }
})
