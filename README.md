# WSD ☀️🌤️🌦️🌧️
                                             
![WSD: latest weather](https://github.com/peterrenshaw/wsd/blob/master/www/latest-simple-weather.png)


TODO
* cron: set up cron
        document 
* d3:   title, description
        work out axes
        how to show data values 

2018NOV05
* quick hack to change data points to either black (light colour) or 
  white (dark colour) so you can see the points across entire graph.

* using d3.scaleLinear created a colour range for temp
  with the follow colour grading:

       0,     10,      20,       30,    40,      50


        "blue", "green", "yellow", "red", "purple"

2018NOV03
* rebrand, fix js code formatting.

* in <www/index.html> remove d3js code and place into <www/weather.js>

* added header via creating a new header data file 
  until I can work out how to break down complex data in JS this
  will do.

     header <www/latest-simple-weather-header.json>

* contains multiple fields (title and description)

* added the d3js in <www/index.html> included is the output file
  <www/latest-simple-weather.json> (with redundant data). 

* to run in the www path:

     python -m http.server:8000 

* the output for <www/index.html> is svg. 

* features:

      each data point is represented by a vertical rectangle.

      the colour choice is to reflect the increase in temperature

      each data point is also indicated with a black circle

      haven't worked out how to show temp. value (axes)

* boy is d3 precise and brittle.

2018NOV02
* fix this crap:

               TODO initialisation of these fields is dodgy, verify
               add these fields to the header so we don't have problem of 
               undefined. But we have to work with this on d3js side

* reformat that local time to a ISO format so we can convert to Date in JS side 
  the objective here is to create a datetime ISO standard, then at JS side you 
  can create a date and manipulate it.

               local_date_time_full local_date_time_iso
               "20181102083000" ==> "2018-11-02T08:30:00"
 
* Note the key change:

              'local_date_time_full' ==> 'local_date_time_iso'

* doing this allows great flexability at the d3js side where you can 
  manipulate dates and times at high granular level for graphing.


2018NOV01
* Dates in JavaScript suck bad!

* So I'm left with pre-processing the dates and while I'm at it, 
  reduce the number of fields (supress) so the data is ONLY what
  I need. At the moment this is:

           * date in local time
           * temperature

* need to add a blank set of keys and blank values to avoid 'undefined'
  when reading first record. is there a better way to do this? add a 
  header? that's what got me in the first place.



2018OCT31
* shell uses ws.py -g then ws.py -e

* basic shell script to be called via cron

* various little fixes

* minor update to make filename with date optional and replace with default until directed. 

* makes easier to have the same filename when calling from D3 code.

* changes to data filenames: allow to give unique yyyymmddThh filename and specific filename via -r option




2018OCT30
* bugger: needed to simplify the downloaded JSON from a complex structure to a linear list. 

* created a new json file from latest-weather.json to yyyymmmddThh.json
  using ./ws.py -e command. saves to destination directory for usage.

* it is a simplified version of the downloaded file 


2018OCT27
* need some periodic useful data to play with D3, so I hacked 
  a quick bit of code to get periodic weather data from BOM
  (Australian Bureau of Meteorology).
 
      read more about the BOM here <http://www.bom.gov.au/inside/index.shtml>
      this is version 0.1

      add a cron job: every half hour/forty five minutes wit a cron script
      that calls ./wsd.py -g
  
      could use the RSS/HTML but I want specific files from individual 
      weather stations to play with.


* WSD (Weather Station Data)
    
      for example this Melbourne Airport data
      <http://www.bom.gov.au/fwo/IDV60801/IDV60801.94866.json>


2018OCT271200
* started


vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
