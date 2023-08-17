from RPLCD.i2c import CharLCD
import time
import sys

# Set up the LCD
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=4)

# Clear the LCD display
lcd.clear()

# Display a message on each of the four lines
lines = [
    "Hello, this is a",
    "Custom message on",
    "Your LCD display!",
    "Have a great day!"
]

# Truncate or pad messages to fit within 16 characters
for i in range(4):
    lines[i] = lines[i][:16].ljust(16)

# Loop through each line and display the message
for i in range(4):
    lcd.cursor_pos = (i, 0)  # Set cursor position to the current line
    lcd.write_string(lines[i])

def exit_program():
    lcd.clear()  # Clear the LCD display
    lcd.write_string("Exiting...")  # Display "Exiting" message

    # Fade in and turn on the backlight
    for brightness in range(0, 101, 10):
        lcd.backlight_enabled = True
        lcd.backlight_pwm = brightness
        time.sleep(0.2)  # Delay for fade-in effect

    lcd.clear()  # Clear the LCD display
    lcd.backlight_enabled = False  # Turn off the backlight
    sys.exit()  # Terminate the program

# Keep the message displayed and handle KeyboardInterrupt
try:
    while True:
        pass
except KeyboardInterrupt:
    exit_program()
