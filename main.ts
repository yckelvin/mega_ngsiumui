input.onButtonPressed(Button.A, function () {
    MuseOLED.clear()
    basic.pause(2000)
    MuseOLED.writeStringNewLine(MuseIoT.HKTIAQ(
    Key,
    "628465168d6d7a0011bea7b7",
    "62b93dcbfad13d5e68a9b175",
    MuseIoT.deviceDescription.NULL,
    MuseIoT.methodDirection.NULL
    ))
})
input.onButtonPressed(Button.AB, function () {
    MuseOLED.clear()
    basic.pause(2000)
    MuseOLED.writeStringNewLine(MuseIoT.HKTIAQ(
    Key,
    "628465168d6d7a0011bea7b7",
    "62b93dcbfad13d5e68a9b175",
    MuseIoT.deviceDescription.NULL,
    MuseIoT.methodDirection.switch_ON
    ))
})
input.onButtonPressed(Button.B, function () {
    MuseOLED.clear()
    basic.pause(2000)
    MuseOLED.writeStringNewLine(MuseIoT.HKTIAQ(
    Key,
    "628465168d6d7a0011bea7b7",
    "62b93dcbfad13d5e68a9b175",
    MuseIoT.deviceDescription.NULL,
    MuseIoT.methodDirection.switch_OFF
    ))
})
let Key = ""
basic.showNumber(0)
MuseIoT.initializeWifi()
basic.pause(5000)
basic.showNumber(1)
MuseIoT.setWifi("KLHOME", "127214529")
basic.pause(10000)
basic.showNumber(2)
MuseIoT.ConnectMuseDataMQTTbroker("KL234")
basic.pause(2000)
basic.showNumber(3)
Key = MuseIoT.GetTheSecurityKey("muselab", "muselab")
MuseOLED.writeStringNewLine(Key)