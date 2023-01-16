**UPDATE 16/01/2023**

CODE UPDATED AND IS NOW WORKING AGAIN. PLEASE COMMENT IF ANY ISSUES.

----------------------------------------------------

INSTALLATION INSTRUCTIONS FOR TESLA VIN CHECKER

This is a relatively simple install process and should take you no more than 10 minutes. You will need a Raspberry Pi 3 or newer, running Raspberry Pi OS with Desktop.

STEP 1: If you haven’t already, go to https://www.raspberrypi.com/software/operating-systems/ and download “Raspberry Pi OS with Desktop”. The reason you need the desktop version is because Tesla is very good at detecting bots, and we need to run this in a viewable browser. Flash this to your SD card and setup as necessary.

STEP 2: Once you are up and running, install the necessary packages by opening a terminal window and entering the following commands:

	sudo apt-get update
	sudo apt-get upgrade -y
	sudo apt-get install chromium-chromedriver python3-pip xserver-xephyr -y
	sudo pip install selenium

STEP 3: Open “Thonny Python IDE” and paste the contents of “teslavinchecker.py”. You will need to enter in the following information where indicated in the code:

	Reservation Number
	Tesla account username and password
	VIN prefix 
	(In 2022 it is LRW, however this may change. Check TMC or VedaPrime’s Discord for updated information)

STEP 4: Save the file, name it whatever you like and press “Run current script” (green play icon, top left corner). The following will happen:

A blank chrome window opens
The script will login to your Tesla account, check for a VIN and logout again. If there is no VIN, it will continue to check every 60 minutes. If a VIN is found, it will close.

	Alternatively, you can SSH into your Pi and run the following command:
	DISPLAY=:0 python3 /dir_where_your_file_lives/teslavinchecker.py
	
	You can also run it directly from the terminal on your Pi with:
	python3 /dir_where_your_file_lives/teslavinchecker.py
	
NOTES: 

*Do NOT close the chrome browser window, otherwise you will need to stop the script and run it again.

*The chrome window will always remain open. While it is running, you cannot use chrome for any other purpose. If you want to surf the web, use another browser such as Firefox. I recommend using your Pi for only this purpose and run it 24/7.

*You can monitor progress by watching the comments in the shell, under the code in Thonny Python IDE. I recommend leaving this open as it will notify you when a VIN has been found. If you ran the script from the terminal (SSH for example), updates will show in there.

*I recommend that you do not check for a VIN more than once per hour, to avoid flooding Tesla's server with too many requests (or being recognised as a bot).

*I take no responsibility for anything that may happen as a result of using this script. Use at your own risk.

*Tesla is good at recognising bots, hence the need to run this in a visible browser. I am working on a way to run this completely headless, but as of yet have not had any luck getting past the bot-checker.

*If you want to run this without a monitor connected, there is a workaround: boot your Pi connected to a monitor, once it has booted to the desktop you can unplug the HDMI cable from the Pi and run the script via SSH (as described above). If you don't do it this way, Tesla will detect you are a bot and deny access. I am working on a solution to this problem.

*I have found it is easiest to install this on a Raspberry Pi. I am considering other platforms in the future.

Enjoy!

Karlos22
	
