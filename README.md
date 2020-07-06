# COVID_Kingston_Scraper

This is a project I started to help me be more up to date with how many active cases of COVID-19 there are in my area, and because I wanted to become more familiar with the Rasberry Pi and how to use it to webscrape the internet. 

The website I scraped from: https://app.powerbi.com/view?r=eyJrIjoiNTJjYWM2NjgtNTRhZi00NDcyLTkxYzEtZDlmZTZjMDRmN2QzIiwidCI6Ijk4M2JmOTVjLTAyNDYtNDg5My05MmI4LTgwMWJkNTEwYjRmYSJ9

The data I scraped from the site would be used to display the currently active cases on a 7-segment display and the community status (red, orange, yellow, green) with an RBG LED. 

## Challenges I Faced

### Dependancy issues:
* The first major hurdle/challenge I faced occured when I found out that the exact data I was trying to scrape used JavaScript to render and didn't actually show up during the inital request to the site. This made things much harder because I wouldn't be able to use the Beautiful Soup library to parse through the html, and had to use somthing that was JavaScript friendly. So, I opted to use Selenium for this project which led me to my next hurdle.
* Installing Selenium on the pi was as straightforward as it can get, however installing the necessary webdriver to go with it was a bit tricky and I spent a lot of time trying to figure out which version of the chromium chromedriver I needed for it to be functional on the Pi. And after a couple hours I stumbled upon this random github which blessed me with the right commands to do so (https://gist.github.com/mamedshahmaliyev/ce5632d326f8f48cf42f14d484aa93e4).
* The next hurdle was learning how to set up communications with the Pi, I already knew how to ssh into it, but I wanted to be able to seamlessly push and pull remotely to reduce the amount of time it took me to test things. I did that by cloning this repo onto the Pi through ssh and created a personal access token for it to cache my credentials for me.

### Coding issues:
* The website I was trying to scrape data off was set up in a weird way that made it hard to scrape. For some reason the xpaths of the web elements on the site were changing seemingly at random times throughout the day and that caused a lot of issues with the scraper trying to identify an element and finding out it doesn't even exist. But I soon figured out that only the order of the elements in each row were changing and so I could still locate them by what row they appeared in on the site and use the text in each element to find the one carrying the data I wanted.

* The next issue I ran in to was a mix of both coding and hardware issues. The 7-segment display did not come with a module attached, so with help from this blog post I found (https://raspi.tv/2015/how-to-drive-a-7-segment-display-directly-on-raspberry-pi-in-python) I manually wired up some resistors and ensured that all 12 of the wires were plugged into the right GPIO pins. I even drew up a diagram to help me keep track of all the wires and which pins they were connected to.
<IMAGE OF DIAGRAM HERE>

* And after hooking up all the wires and triple checking that they were all connected to the right pins to my disapointment it was a total disaster as the display rendered a bunch of gibberish none of which was even close to resembling a number. And after a couple hours of debugging went by making sure there was nothing wrong with the code, I started unplugging and plugging back in each wire individually and found out that one of the wires (#12 in the diagram) responsible for turning on and off the first digit was interfering with the display of the others (when the wire was plugged in it caused all the other digits to be missing a segment). I figured this must have been due to a shortage causing all the voltage for that segment to flow through the wire back into the Pi (probably because of my failed attempts earlier in the year to try and figure out what each pin did without any resistors attached). And so because I didn't really need a 4th digit I opted to keep that wire unplugged.
  
## How to Run it:
All the wiring should make sense from the diagram above and from the blog post I linked, if not here is a picture of what it looks like in person:
<INSERT IMAGE OF PI AND WIRING>
I have also added a bunch of comments in the main.py file that reiterate this info.
  
So once you have all the wiring don you can run the main.py file and have it display the active cases and community status color. 

One thing to note is that I set this up to run a subprocess to render the display, and so when it does an update it doesn't interfere with what you are doing with it flashing on and off. I have also set a timer so it turns off during the night so that I can have it stay in my room without disrupting my sleep.

