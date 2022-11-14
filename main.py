def on_button_pressed_a():
    MuseOLED.clear()
    basic.pause(2000)
    MuseOLED.write_string_new_line(MuseIoT.HKTIAQ(Key,
            "628465168d6d7a0011bea7b7",
            "62b93dcbfad13d5e68a9b175",
            MuseIoT.deviceDescription.NULL,
            MuseIoT.methodDirection.NULL))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    MuseOLED.clear()
    basic.pause(2000)
    MuseOLED.write_string_new_line(MuseIoT.HKTIAQ(Key,
            "628465168d6d7a0011bea7b7",
            "62b93dcbfad13d5e68a9b175",
            MuseIoT.deviceDescription.NULL,
            MuseIoT.methodDirection.SWITCH_ON))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    MuseOLED.clear()
    basic.pause(2000)
    MuseOLED.write_string_new_line(MuseIoT.HKTIAQ(Key,
            "628465168d6d7a0011bea7b7",
            "62b93dcbfad13d5e68a9b175",
            MuseIoT.deviceDescription.NULL,
            MuseIoT.methodDirection.SWITCH_OFF))
input.on_button_pressed(Button.B, on_button_pressed_b)

Key = ""
basic.show_number(0)
MuseIoT.initialize_wifi()
basic.pause(5000)
basic.show_number(1)
MuseIoT.set_wifi("KLHOME", "127214529")
basic.pause(10000)
basic.show_number(2)
MuseIoT.connect_muse_data_mqt_tbroker("KL234")
basic.pause(2000)
basic.show_number(3)
Key = MuseIoT.get_the_security_key("muselab", "muselab")
MuseOLED.write_string_new_line(Key)