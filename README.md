Here I have a simple and crude python script to log in to your Tesla account and search the source code for your VIN (if it exists).

To get this to work you are going to need a Raspberry Pi 3 (or newer) running Raspbian with desktop and the following packages installed:

-chromium
-selenium
-yagmail

The reason you need the desktop version of Raspbian is because selenium will not run on a headless setup.  Installing and configuring Selenium on your pi can be a bit of pain, so check YouTube for help.

Once you have all the packages above installed, login to your Tesla account using Chromium and make sure you save the username and password using a “default” profile. If you don’t do this, the script can’t login as it relies on your login details being saved prior.

Now edit the code and fill in the blanks with your RN etc. Also double check what your VIN begins with. In my case it is "LRW" but it varies between model years, etc. Change as necessary. Check the code for further instructions.

NOTE USING YAGMAIL IN THIS FASHION: I specifically created a throwaway gmail account for this purpose. I DO NOT RECOMMEND USING YOUR OWN PERSONAL EMAIL ACCOUNT FOR THIS. Please create a throwaway one for safety and whitelist it in your personal email account, so it isn't marked as spam. If you are not comfortable putting your password in the code, it is possible to configure yagmail so that these details are saved to your pi. Check the dev webpage to see how to do that. Or just use a throwaway account.

If you have done all of this correctly, the code should work. Then you can use the “crontab -e” command to setup a schedule to run at your leisure.

As I said, the code is rushed and crude. Please improve on it! :)

Karlos
