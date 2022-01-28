Edit: Are you a n00b? there are some detailed installation instructions coming in the coming days. Stay tuned! If you know what you are donig, keep reading....

Hi!

This is a simple and crude python script to log in to your Tesla account and search the source code for your VIN (if it exists).

To get this to work you are going to need a Raspberry Pi 3 (or newer) running Raspbian with desktop and the following packages installed:

-chromium
-selenium
-yagmail
-xvfb

The reason you need the desktop version of Raspbian is because selenium will not run on a headless setup without a virtual display (it is possible, but I am not currently running my Pi in this config).  Installing and configuring Selenium on your pi can be a bit of pain, so check YouTube for help or wait for my detailed instructions (soon to follow). You will need chromedriver so that selenium can control chromium. I wrote this for the pi because it was simply too difficult to get Selenium working on Windows or MacOS.

Once you have all the packages above installed, login to your Tesla account using Chromium and make sure you save the username and password using a “default” profile. If you don’t do this, the script can’t login as it relies on your login details being saved prior.

Now edit the code and fill in the blanks with your RN etc. Also double check what your VIN begins with. In my case it is "LRW" but it varies between model years, etc. Change as necessary. Check the code for further instructions.

NOTE USING YAGMAIL IN THIS FASHION: I specifically created a throwaway gmail account for this purpose. I DO NOT RECOMMEND USING YOUR OWN PERSONAL EMAIL ACCOUNT FOR THIS. Please create a throwaway one for safety and whitelist it in your personal email account, so it isn't marked as spam. If you are not comfortable putting your password in the code, it is possible to configure yagmail so that these details are saved to your pi. Check the dev webpage to see how to do that. Or just use a throwaway account. You may also need to give yagmail permission to access your email account (for example gmail does this).

If you have done all of this correctly, the code should work. Then in the terminal, you can use the “crontab -e” command to setup a schedule to run at your leisure. It should look like this: "00 * * * * xvfb-run python3 /home/pi/teslavinchecker.py"
It will run every hour on the hour. "xvfb-run" means it will run headless and in the background.

For those wondering about the hard exit/sys flush command, I had some issues with the pi getting bogged down after days of running this script. This seems to have solved it.


As I said, the code is rushed and crude. Please improve on it! :)

Karlos
