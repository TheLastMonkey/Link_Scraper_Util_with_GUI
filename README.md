# Link Scraper w/ GUI Regex and output file  

#### Description  
This script will scrape a web page or html file for its links and return 
those links which can optionally be ran through regex as well as 
 output to a file.  
 If no output file is specified links are only printed to the console.  
Comes with a simple GUI.
Script and breaks easily and is not in PIP 8 compliance  

#### Imports/Requirements  
**Linux**  
selenium - Webdriver must be downloaded and added separately (see Install)  
PySimpleGUI - Imported Normally  
re - Imported Normally  

#### Install  
`sudo pip3 install selenium`  
`sudo pip3 install pySimpleGUI`   
https://www.seleniumhq.org/download/  
Make sure you get the Chrome Webdriver   
Put the Webdriver file into the "sel_driver" folder which is one layer or 
deeper than the script.  
Or option we modified the script to reflect the path of the driver. You can 
also optionally modified the script to Output the output file to a different folder.  
There are Selenium tutorials you'll be all right.

#### Options/Features  
Headless Enabled by Default - "Just do the thing."  
User Data Cookies Logins Etc Disabled by Default - see User Data  
Accept Input as a Local HTML File or a URL  
Add Regex if Desired
Add Output File if Desired  
"Some" Duplicate URL Rejection - Needs Improvement - but that would reduce performance.  
Terrible Documentation!!! :D  
Add Wait Time - useful for giving you time to scroll to capture non loaded content.  
  
#### Wait Time Bonus!  
On certain web pages as long as you keep loading and more elements the wait MAY automatically extend.  
Depending on the website you may be able to load multiple pages or follow links to new pages and continue to collect links.  

#### User Data  
This option allows you to use logins and cookies so on and so forth.  
This is useful for websites that require logging in or recognizing you in some way.  
If you need to login or perform an action simply make sure that **Headless** is **Uncheckedand**, **User Data** is **Checked**, and give yourself a wait time long enough to login or perform whatever task you need (Captcha ... Etc).  
Selenium will create a folder with your user data in it, which you can later Use/Delete if you would like. However the user data contained within that folder will only be used if you have the **User Data** checkbox **Checked**.  

#### Duplicate Link Rejection  
The current implementation only checks the current link with the previous link and rejects the current link if they are the same. It is designed to spit out links as fast as possible. There are certainly ways that this could be improved, however it would most likely impact performance. By giving you the ability to Output the links to a file I am leaving it to your discretion whether you want to run sort or De-dupe commands over that file.

#### Disclaimer/License  
You do you. This comes with no license no guarantee and will likely 
break and destroy everything in the world. You have been warned. You are
 also here by liable for everything.... just everything. What can I say this 
 is a mess and it's definitely your fault. No license No guarantee and if
 someone calls you claiming to extend this script warranty it is likely a scam 
 and you **_should give_** them your money.  
 
 ##### But on the DL:  
 
What is this thing really for?  
Although this utility has various uses I find that it's highly useful for
 finding either specific links or links off site.   
For instance if you're on Reddit you need like to get all the imgur or gfycat 
links.  
With some simple regex you can easily accomplish that.  

#### Notes/Toubleshooting

I have no idea how URL encoding works so if you have an HTML file stored locally and it has anything other than spaces and regular characters you will likely need to simplify it. Dashes "-" or anyting that encodes differently from a path to a URL will need to be changed or simplified.  
See Example  
  
file in browser look like this..  
file:///home/user/thisAPP/Cookbook%20C3%20PySimpleGUI.html  
but path looks like this..  
       /home/user/thisAPP/Cookbook\ -\ PySimpleGUI.html  
file:// and %20 for space are **auto add** but anyting that encodes differently is fucked. :(

I may update the fix this.    

You can only pick a file or a URL if you pick both it will likely break.  
