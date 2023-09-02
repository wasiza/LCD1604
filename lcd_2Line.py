from RPLCD.i2c import CharLCD

# Initialize the LCD
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2, lcd.backlight_enabled = True)

try:
    # Display "Hello" on the first line
    lcd.write_string("Hello")
    
    # Set the cursor to the beginning of the second line
    lcd.cursor_pos = (1, 0)
    
    # Display "World!" on the second line
    lcd.write_string("World!")

    # Print "Hello, World!" on the terminal
    print("Hello, World!")

    # Wait for user input to exit
    input("Press Enter to exit...")

finally:
    # Clear the display and close the LCD
    lcd.clear()
    lcd.close()
    lcd.backlight_enabled = False
