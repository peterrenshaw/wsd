# WSD ☀️🌤️🌦️🌧️
                                             
![WSD: latest weather](https://github.com/peterrenshaw/wsd/blob/master/www/latest-simple-weather.png)


TODO
* revise code in tools to simplify
* cron: document 
* d3:   work out axes
        how to show data values
* auto install of latest version of python requests 

2018DEC11
* added make file for quicker build and clean.

* found defect in tools.dt_new_date, forgot to return

2018DEC06
* back to work on d3, generate some time based data and graph the axis.

* bug, see docs/BUGS.md


```
   ./se.py -s '2018DEC04' -e '2018DEC05' -i 1 -u h -j

```


2018DEC05
* reduced complexity by breaking tools into smaller pieces

```
  generate.py (lots of switches, 2 different functions)
      |
      V
  generate/se.py   (generate start to end datetimes) DONE
  generate/si.py   (generate start with intervals) TODO
``` 

* add tools.dt_new_date
  read the date dictionary, build the date, return
  no error handling (yet)

* clean up code tools.py, se.py

* results: on the command line lets do the following: 
  Generate data from start date to end date at hourly intervals in json format.

```
   start date:  December 4th, 2018 (-s ...)
   end date:    December 5th, 2018 (-e ...)
   interval:    1                  (-i 1)
   unit:        hour               (-u h)
   save:        yes                (-j)
```

```
   ./se.py -s '2018DEC04' -e '2018DEC05' -i 1 -u h -j

```
    generates as a file

```
[
    "20180004T00:00.00",
    "20180004T01:00.00",
    "20180004T02:00.00",
    "20180004T03:00.00",
    "20180004T04:00.00",
    "20180004T05:00.00",
    "20180004T06:00.00",
    "20180004T07:00.00",
    "20180004T08:00.00",
    "20180004T09:00.00",
    "20180004T10:00.00",
    "20180004T11:00.00",
    "20180004T12:00.00",
    "20180004T13:00.00",
    "20180004T14:00.00",
    "20180004T15:00.00",
    "20180004T16:00.00",
    "20180004T17:00.00",
    "20180004T18:00.00",
    "20180004T19:00.00",
    "20180004T20:00.00",
    "20180004T21:00.00",
    "20180004T22:00.00",
    "20180004T23:00.00",
    "20180005T00:00.00"
]
````

* reduce complexity by breaking tools into smaller pieces

```
  generate.py (lots of switches, 2 different functions)
      |
      V
  generate/se.py   (generate start to end datetimes)
  generate/si.py   (generate start with intervals)
``` 

2018DEC01
* config updated in <config.py> and <wsd.py>
* <config.py> added
* moved functions from <generate.py> to <tools.py>
* <setup.py> done: 

```sudo python3 setup.py install```
 
* docs/
  move all README, ABOUT, LICENCE to docs
* build <setup.py>, <__init__.py>

* tools.py hack. recode inline to functions so I can re-use and make the tool do things I expect
```
   save data to json
   save data to json and pretty print
   save data as text, supply an extension
   redirect results to console as json or text
```
* <generate.lst2int> (extract list data, convert to integer) and has problem if less than what 
  is expected so a fix to lst2int means the problem of extracting from reduced string is handled and warning issued

    ./generate.py -s '2018nov30T16' -f 5 -u second

* extracing datetime components from '2018nov30T16' for example decomposes to:

```
  year:       2018
  month:      nov
  day:        30
  hour:       --
  minute:     --
  seconds:    --
```

  so above fix makes sure the func  <generate.lst2int> is called and handles
  less information.

* solving problem in <generate.py>:

   decomposing string to time components
   building time from string
   changing time using timedeltas

* these become the ideas, tools to build multiple timestamps 

2018NOV30
* new tool to create date data <generate.py> to solve the problem of specific 
  date data used to play/work with D3 so I can learn more on formatting axis

* created instead of installing python Panda which is a monster install

2018NOV13
* updated wr.sh so that cron calls this script every contrab.cron period.

* yesterdays idea is BS. So I created an option to reverse data order 
  to compensate for data that is ordered. this is important, especially 
  if in the case of weather data that is date ordered. Only available if 
  you extract and simplify. Usage below.

  ./ws.py -e -s -b

* why do this? it is easier and faster to pre-process the data and display
  the data in JavaScript as is. I can confirm the sort order change because 
  the source data has a sort_order field from the RMDB.

2018NOV12
* found the data source was coming in backwards, do the temps got colder
  during the day. Fixed this in <www/weather.js> by reversing data.

* think about this problem as data has some order. in this case it was in
  reverse date order 

2018NOV07
* usage:

> ./tools.py -f 'scale' -j "[0, 1000, 3000, 2000, 5000, 4000, 7000, 6000, 9000, 8000, 10000]" -p -d "$HOME/some/dir"

  will output file to: <.../some/dir/scale.json> and will look like (pretty printed json)

```
   [
      0,
      1000,
      3000,
      2000,
      5000,
      4000,
      7000,
      6000,
      9000,
      8000,
      10000
 ]
``` 

* added tool.py to create simple JSON files from data supplied
  by string for testing.

2018NOV06
* removed rain from graph, crontab done

* crontab testing

* funky: got the temp values from the looped instance of all data :)

```
// OLD WAY collect data
//d[i] = data[i].apparent_t;
// NEW WAY collect the data    
d[i] = {'temp':  data[i].apparent_t,
                'wind':  data[i].gust_kmh,
                'humid': data[i].rel_hum, 
                'hour':  hourFormater(hour)};
...
...
...
// show height of temp
svg.selectAll("rect")
       .data(data)                          // ALL DATA IN
       .enter()
       .append("rect")
       .attr("y", function(d) {
           return h - (d['temp'] * 4);      // SPECIFIC temp value
       })
       .attr("height", function(d) {
           return d['temp'] * 40;           // SPECIFIC temp value
       })
       .attr("x", function(d, i) {
           return i * (w / data.length);
       })
       .attr("width", w / data.length - barPadding)
       .attr("stroke", function(d) {
           return "white";
       })
       .attr("stroke-width", "0.1")
       .attr("fill", function(d) {
           return color(d['temp']);        // SPECIFIC temp value
       })
```

* added rain info, 'rain_trace' to simple processing.

* setup cron, added wr.sh conf/cron.sh, yet to test

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
