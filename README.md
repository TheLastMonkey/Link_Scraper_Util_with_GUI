# Link Scraper w/ GUI Regex and output file  

#### Description  
This script will scrape a web page or file for its links and return 
those links which can optionally be ran through regex as well as the
 output to a file.  
 If no output file is specified links are only printed to the console.  
Comes with a simple GUI.
Script and breaks easily and is not in PIP 8 compliance  
#### Imports/Requirements  
selenium - Webdriver must be downloaded and added separately (see Install)  
PySimpleGUI - Imported Normally  
re - Imported Normally  

#### Install  
sudo pip3 install selenium  
sudo pip3 install pySimpleGUI  
https://www.seleniumhq.org/download/  
Make sure you get the Chrome Webdriver   
Put the Webdriver file into the "sel_driver" folder which is one layer or 
deeper than the script.  
Or option we modified the script to reflect the path of the driver. You can 
also optionally modified the script to Output the output file to a different folder.  
There are Selenium tutorials you'll be all right.

#### Options/Features  
Headless Enabled by Default  
User Data Cookies Logins Etc Disabled by Default  
Accept Input as a Local HTML File or a URL  
Add Regex if Desired
Add Output File if Desired  
"Some" Duplicate URL Rejection  
Terrible Documentation!!! :D

#### Disclaimer/License  
You do you.this comes with no license no guarantee and will likely 
break and destroy everything in the world. You have been warned. You are
 also here by liable for everything.... just everything. What can I say this 
 is a mess and it's definitely your fault.  
 
 ##### But on the DL:  
 
What is this thing really for?  
Although this utility has various uses I find that it's highly useful for
 finding either specific links or links off site.   
For instance if you're on Reddit I need like to get all the imgur or gfycat 
links  
With some simple regex you can easily accomplish that.  


