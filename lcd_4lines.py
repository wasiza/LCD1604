from RPLCD.i2c import CharLCD

# Initialize the LCD
lcd = CharLCD('PCF8574', 0x27, cols=20, rows=4,)  # Change 'cols' to 20 and 'rows' to 4 for a 4-line LCD

try:
    # Display "Hello" on the first line
    lcd.write_string("Coding is")
    
    # Set the cursor to the beginning of the second line
    lcd.cursor_pos = (1, 0)
    
    # Display "World!" on the second line
    lcd.write_string("an art")
    
    # Set the cursor to the beginning of the third line
    lcd.cursor_pos = (2, 0)
    
    # Display "GPT!" on the third line
    lcd.write_string("Let's create")
    
    # Set the cursor to the beginning of the fourth line
    lcd.cursor_pos = (3, 0)
    
    # Display "3.5!" on the fourth line
    lcd.write_string("something amazing!")

    # Wait for user input to exit
    input("Press Enter to exit...")

finally:
    # Clear the display and close the LCD
    lcd.clear()
    lcd.close()
