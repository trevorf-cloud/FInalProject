DESTOP ASSIGNMENT NOTIFIER INSTRUCTIONS:
1. Set up ESP32 broadboard circuit as shown in the circuit diagram. I have the LED connected to P21 and the button connected to P18.
2. Plug in the ESP32 via USB to your PC.
3. Open "assignments.xlsx" and type in your assignments and their due dates. Leave the 3rd column blank.
4. Open the main.py file in Thonny and save it to your ESP32. Now it will always run when you connect your ESP32 to your PC.
5. Hit run and then close Thonny.
6. Open CMD on your PC, navigate to the assignment notifiers folder, and type "python bridge.py." This starts the system. Leave CMD open.
7. When the LED on your breadboard lights up, it means you have 24 hours to complete an assignment! Open the command prompt to see what it is.
8. When you've finished the assignment, press the button on the breadboard and the script will automatically update the assignments spreadsheet to list that assignment as done.
9. The breadboard LED turns off until the next assignment is almost due!
