# Obituary-web-scraper
Of Andrew Earl 9-28-2024

TLDR: Hard coded webscraper for names of obituaries from the post and curior in the charleston area

Requires various python modules, request, json, os, date, and csv

Done in python 3.10

To modify it for anywhere else you might as well make your own web scraper honestly.
Again its hard coded so you would need to refactor a lot for a new target. Especially
with the json expectations.

When participating in the charleston tax sale 2024 I wanted to compare the owner names of the 
properties listed vs the listings of obituaries in the charleston area. To see who died and 
was less likely to pay their overdue taxes due on the property in the coming year. 
(So I could buy it)

https://www.charlestoncounty.org/departments/delinquent-tax/tax-sale.php

kinda morbid I know. But its a utility I liked making and found useful as pre research for 
the upcoming tax sale. It took much longer than I expected to make it tbh. Apparently
This paticular website doesnt hide the api requests to only be from the webpage itself.
So the data can be queried directly. Not how I would have done the website but who knows.
