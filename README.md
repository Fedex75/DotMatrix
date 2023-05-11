# DotMatrix
The circuit accepts 3 inputs:
- Info signal: ASCII code of the character
- Dot signal: Color code (1: White, 2: Red, 3: Green, 4: Blue, 5: Yellow, 6: Magenta, 7: Cyan)
- Color signals: Any number > 0 on a color signal will set that color (use EITHER the dot signal OR a color signal)

To display digits, add 48 to the value to get the character code

Due to a limitation of the signed integer logic not all ASCII characters are available: the ~ is missing
