
     _      __ ____ ___ 
    | | /| / // __// _ \
    | |/ |/ /_\ \ / // /
    |__/|__//___//____/ 
                                                            
     _      __            __   __           
    | | /| / /___  ___ _ / /_ / /  ___  ____
    | |/ |/ // -_)/ _ `// __// _ \/ -_)/ __/
    |__/|__/ \__/ \_,_/ \__//_//_/\__//_/  


2018OCT27
* need some periodic useful data to play with D3, so I hacked 
  a quick bit of code to get periodic weather data from BOM
  (Australian Bureau of Meteorology).
 
      read more about the BOM here <<http://www.bom.gov.au/inside/index.shtml>>
      this is version 0.1

      add a cron job: every half hour/forty five minutes wit a cron script
      that calls ./wsd.py -g
  
      could use the RSS/HTML but I want specific files from individual 
      weather stations to play with.


* WSD (Weather Station Data)
    
      for example this Melbourne Airport data
      <<http://www.bom.gov.au/fwo/IDV60801/IDV60801.94866.json>>


* usage: 

       new JSON configuration data file
       
           ./ws.py -n -t 'melbourne airport' 
                      -f "json" 
                      -u http://www.bom.gov.au/fwo/IDV60801/IDV60801.94866.json
           
       get (weather data using config file)
       
           ./ws.py -g

       debug
           ./ws.py -d
       help
           ./ws.py -h


* started 2018OCT271200


vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
