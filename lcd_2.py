from RPLCD.i2c import CharLCD
import time

# Set up the LCD
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=4)

# Clear the LCD display
lcd.clear()

def update_lcd(line1, line2, line3, line4):
    lcd.cursor_pos = (0, 0)
    lcd.write_string(line1)
    lcd.cursor_pos = (1, 0)
    lcd.write_string(line2)
    lcd.cursor_pos = (2, 0)
    lcd.write_string(line3)
    lcd.cursor_pos = (3, 0)
    lcd.write_string(line4)

# Display a message over 4 lines
update_lcd("This is the", "GPT-3.5 Assistant,", "here to help you", "Have a great day")

# Keep the message displayed
try:
    while True:
        time.sleep(1)  # Keep the LCD message displayed
except KeyboardInterrupt:
    lcd.clear()  # Clear the LCD display
