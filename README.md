
     _      __ ____ ___ 
    | | /| / // __// _ \
    | |/ |/ /_\ \ / // /
    |__/|__//___//____/ 
                                                            
     _      __            __   __           
    | | /| / /___  ___ _ / /_ / /  ___  ____
    | |/ |/ // -_)/ _ `// __// _ \/ -_)/ __/
    |__/|__/ \__/ \_,_/ \__//_//_/\__//_/  


TODO
* set up cron & document 


2018OCT31
* shell uses ws.py -g then ws.py -e

* basic shell script to be called via cron

* various little fixes

* minor update to make filename with date optional and replace with default until directed. 

* makes easier to have the same filename when calling from D3 code.

* changes to data filenames: allow to give unique yyyymmddThh filename and specific filename via -r option

* usage: 

       # BUILD A NEW CONFIGURATION FILE
       # only do this once, or as needed.
       new JSON configuration data file
           ./ws.py -n -t 'melbourne airport' 
                      -f "json" 
                      -u http://www.bom.gov.au/fwo/IDV60801/IDV60801.94866.json
           
       # GET LATEST WEATHER 
       # reads config file, gets the latest readings
       get (weather data using config file)
           ./ws.py -g

       # EXTRACT 
       # simplified subset of full report 
       extract (simplify weather data)
           ./ws.py -e 

       # RENAME
       # instead of generic file, create a unique simplified data file
       # with filename reflecting time created.
       rename (rename file to yyyymmmdd, else static fn)
           ./ws.py -r 

       # DEBUG
       # show some internal data states while operating
       debug
           ./ws.py -d

       help
           ./ws.py -h



2018OCT30
* bugger: needed to simplify the downloaded JSON from a complex structure to a linear list. 

* created a new json file from latest-weather.json to yyyymmmddThh.json
  using ./ws.py -e command. saves to destination directory for usage.

* it is a simplified version of the downloaded file 

* usage: 

       new JSON configuration data file
           ./ws.py -n -t 'melbourne airport' 
                      -f "json" 
                      -u http://www.bom.gov.au/fwo/IDV60801/IDV60801.94866.json
           
       get (weather data using config file)
           ./ws.py -g

       extract (simplify weather data)
           ./ws.py -e 

       debug
           ./ws.py -d
       help
           ./ws.py -h


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


* usage: 

       new JSON configuration data file
       
           ./ws.py -n -t 'melbourne airport' 
                      -f "json" 
                      -u http://www.bom.gov.au/fwo/IDV60801/IDV60801.94866.json
           
       get (weather data using config file)
       
           ./ws.py -g

       extract (simplify weather data)
           ./ws.py -e 

       debug
           ./ws.py -d
       help
           ./ws.py -h


* started 2018OCT271200


vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
