distancia = 0
basic.show_icon(IconNames.HEART)

def on_forever():
    global distancia
    distancia = sonar
    ping(game.start_countdown(10000),
        DigitalPin.P1,
        DigitalPin.P2,
        PingUnit.Centimeters)
    # Muy cerca 😢
    # Lejos 😃
    if distancia < 10:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.HAPPY)
    basic.pause(500)
basic.forever(on_forever)
