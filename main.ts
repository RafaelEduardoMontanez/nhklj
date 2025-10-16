let distancia = 0
basic.showIcon(IconNames.Heart)

basic.forever(function () {
    distancia = sonar. ping(
        DigitalPin.P1,
        DigitalPin.P2,
 PingUnit.Centimeters
    )

    if (distancia < 10) {
        basic.showIcon(IconNames.Sad)   // Muy cerca 😢
    } else {
        basic.showIcon(IconNames.Happy) // Lejos 😃
    }

    basic.pause(500)
})
