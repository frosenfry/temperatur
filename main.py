def on_forever():
    if input.temperature() > 15 and input.temperature() < 25:
        basic.set_led_color(basic.rgb(0, 255, 0))
    else:
        if input.temperature() < 15:
            basic.set_led_color(basic.rgb(0, 0, 255))
        else:
            pass
basic.forever(on_forever)

def on_forever2():
    if input.temperature() > 25:
        basic.set_led_color(basic.rgb(255, 0, 0))
    else:
        pass
basic.forever(on_forever2)
