from RPLCD.i2c import CharLCD
import time

# Initialize the LCD
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2, backlight_enabled=True)

try:
    while True:
        lcd.clear()
        lcd.write_string("Go the beach? or")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Stay at home?")
        
        user_input = input("Select an option (1/2): ")
        
        if user_input == '1':
            lcd.clear()
            lcd.write_string("Go the beach")
            time.sleep(2)
        elif user_input == '2':
            lcd.clear()
            lcd.write_string("Fine stay @ home")
            time.sleep(2)
        else:
            lcd.clear()
            lcd.write_string("Invalid selection")
            time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    lcd.backlight_enabled = False
    lcd.close()
