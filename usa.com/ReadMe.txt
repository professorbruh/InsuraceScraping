Name:
Scraping of usa.com

Description:
This program goes to the pages in usa.com by referring the zipcodes in zipcode.csv.The trial files were used to get individual tables inside each page.

basic.py contains the main program.It processes all the information present on the page and stores them in json files.

to_json() converts the basic info tab to a dictionary which is later to be put inside the pincode key.It returns the dictionary to a variable which can be later put into the dictionary for the main pincode.

to_json2() converts the Population/Races tab.Due to the large number of zipcodes and the variations in pages, the data has been stored directly off this page and no refinement is done as of yet.

The program also stores the each page html as well.
A folder is made for each zipcode inside which each tab html is stored seperately.


testfile3.py is currently being worked on to get the information off Income/Carriers tab.We use a dictionary to store the header for each table.


The final json file is to be of the format:
[
*Zipcode*:
{
	Basic_Info: *Data*
	Population/Races: *Data*
	Income/Careers: *Data*
	Housing: *Data*
	Education: *Data*	
	Others: *Data*
}
*Zipcode*
{
	.....
}
]


Each tab will contain another dictionary so the json file will be nested.s