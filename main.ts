basic.forever(function () {
    if (input.temperature() > 15 && input.temperature() < 25) {
        basic.setLedColor(basic.rgb(0, 255, 0))
    } else if (input.temperature() < 15) {
        basic.setLedColor(basic.rgb(0, 0, 255))
    } else {
        if (input.temperature() > 25) {
            basic.setLedColor(basic.rgb(255, 0, 0))
        } else {
        	
        }
    }
    basic.showNumber(input.temperature())
})
