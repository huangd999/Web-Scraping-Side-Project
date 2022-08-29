# Web-Scraping-Side-Project

Packages Used: BeautifulSoup, requests, Pandas

Goal: Collect price information off of the wiki pages of Old School Runescape

In order to accomplish this goal, I had to scrape this information off of several thousand pages. However, seeing as it was inefficient to manually conduct this, I chose to instead try and automate the process. To do this, I first familiarized myself with the templates of the item pages on the Old School Runescape. After noticing a trend with no variation items (no button headers to select different variations of an item), and items with variations (button headers). 

With this information, I wrote code for both no variation and variation items. However, for the variation items I noticed that while it worked for some (such as consumables), it did not work for equippable items, since those have an extra set of header buttons for the stats table. To remedy this, I wrote separate code for the equippable items that had variations.

Once I had the code prepared for the no variation, variation but not equippable, and variation and equippable items, I put the three together in the final file. The conditions for each of the three sections were no button headers, one set of button headers, and two set of button headers. 

The end result allowed me to collect the prices off of the web page without having to go through roughly around 3000 separate pages.
