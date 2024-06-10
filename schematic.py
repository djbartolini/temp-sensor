import schemdraw
import schemdraw.elements as elm

# Create the schematic
d = schemdraw.Drawing()

# Draw the circuit
with d:
    # Arduino representation
    arduino = d.add(elm.RBox(w=3, h=4).label('Arduino', loc='center'))

    # Power supply connections
    d += elm.Line().left().at((arduino.center[0], arduino.center[1] - 2)).label('GND', loc='left')
    d += elm.Line().left().at((arduino.center[0], arduino.center[1] + 2)).label('5V', loc='left')

    # Thermistor and voltage divider resistor
    thermistor_start = (arduino.center[0], arduino.center[1] + 3)
    thermistor = d.add(elm.Resistor().down().at(thermistor_start).label('Thermistor').length(2))
    d.add(elm.Line().left().at(thermistor.start).length(1))
    divider_resistor = d.add(elm.Resistor().right().at(thermistor.end).label('10kΩ').length(2))
    d.add(elm.Line().right().at(divider_resistor.end).length(1))
    
    # Connecting Thermistor and resistor to Arduino analog pin (A0)
    d.add(elm.Line().up().at(divider_resistor.end).length(2).dot().label('A0', loc='right'))

    # LEDs and resistors
    for i, pin in enumerate(['D2', 'D3', 'D4']):
        led_start = (arduino.center[0] - 3, arduino.center[1] - i*2 - 1)
        led = d.add(elm.LED().right().at(led_start).label(f'LED {i+1}', loc='right'))
        d.add(elm.Resistor().right().at(led.end).label('220Ω').length(2))
        d.add(elm.Line().right().at(led.end).length(1).dot().label(pin, loc='left'))
        d.add(elm.Line().down().at(led.start).length(1).dot().label('GND', loc='left'))

# Save and display the drawing
d.save('temp-sensor-schematic.svg')
d.draw()
