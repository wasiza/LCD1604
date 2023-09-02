from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2, backlight_enabled= True)

try:
    user_input = input("Enter a message: ")  # Read user input
    lcd.write_string(user_input)  # Display user input on the LCD

    input("Press Enter to exit...")  # Wait for user to press Enter

finally:
    lcd.clear()
    lcd.close()
    lcd.backlight_enabled = False
