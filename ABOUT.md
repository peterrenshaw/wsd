
     _      __ ____ ___ 
    | | /| / // __// _ \
    | |/ |/ /_\ \ / // /
    |__/|__//___//____/ 
                                                            
     _      __            __   __           
    | | /| / /___  ___ _ / /_ / /  ___  ____
    | |/ |/ // -_)/ _ `// __// _ \/ -_)/ __/
    |__/|__/ \__/ \_,_/ \__//_//_/\__//_/  



WHY?
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

       # SIMPLIFY
       simplify (remove unwanted fields)
           ./ws.py -s

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


