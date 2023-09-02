from RPLCD.i2c import CharLCD
import time

# Initialize the LCD with backlight enabled
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2, backlight_enabled=True)

try:
    # Display "Hello" on the first line
    lcd.write_string("Hello")
    
    # Set the cursor to the beginning of the second line
    lcd.cursor_pos = (1, 0)
    
    # Display "World!" on the second line
    lcd.write_string("World!")

  # Wait for a few seconds
    time.sleep(5)

finally:
    # Turn off the backlight and close the LCD
    lcd.backlight_enabled = False
    lcd.close()
    lcd.clean()
