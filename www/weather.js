/*
#========
# name: ws.py
# date: 2018NOV02
#       2018NOV01
#       2018OCT30
#       2018OCT27
# prog: pr
# desc: grab your local BOM data & save to file, simplify data if needed
#       save as json to new (web) directory for use.
#       
#       WSD ☀️🌤️🌦️🌧️
#========
*/


// HEADER
d3.json("http://127.0.0.1:8000/data/latest-simple-weather-header.json").then( function(data) {
    return data;
})
.then(function(d) {
    // label
    d3.select("body") 
      .selectAll("h4") 
      .data(d)
      .enter() 
      .append("h4")
      .text(function(d) {
	   return d;
      });
})
.catch( error => console.log("Error: " + error) );

// FUNCTIONS
var parser = d3.timeParse("%m/%dT%H%M");
var color = d3.scaleLinear()
              .domain([0, 10, 20, 30, 40, 50])
              .range(["blue", "green", "yellow", "red", "purple"]);

// DATA
d3.json("http://127.0.0.1:8000/data/latest-simple-weather.json").then( function(data) {
    return data;
})
.then( function (data) {
    var d = [];
    for (i = 0; i < data.length; i++) {

        // create a Date object
        var dt = new Date(data[i].local_date_time_iso);

        // format dt to hour
        var hourFormater = d3.timeFormat("%H:%M%");
        var hour = d3.timeHour.round(dt);

        // create dict for d3
        d[i] = {'temp':  data[i].apparent_t,
                'wind':  data[i].gust_kmh,
                'rain':  data[i].rain_trace,
                'humid': data[i].rel_hum, 
                'hour':  hourFormater(hour)};
        
    }
    return d;
})
.then( function (data) {
    var w = 800;
    var h = 200;
    var barPadding = 0.8;

    // svg container for weather
    var svg = d3.select("body")
    .append("svg")
    .attr("width", w)  
    .attr("height", h);

    // show height of temp
    svg.selectAll("rect")
       .data(data)
       .enter()
       .append("rect")
       .attr("y", function(d) {
           return h - (d['temp'] * 4);
       })
       .attr("height", function(d) {
           return d['temp'] * 40;
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
           return color(d['temp']);
       })

     // show data point of temp
     svg.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("cy", function(d) {
           return h - (d['temp'] * 4) + 2;
        })
        .attr("cx", function(d, i) {
           return i * (w / data.length) + (w / data.length - barPadding) / 2
        })
        .attr("r", 1)
        .attr("fill", function(d) {
            if ((d['temp'] <= 15.0)) {
                return "white";
            } else {
                return "black";
            }
        })

     // rainfall
     svg.selectAll("rect")
       .data(data)
       .enter()
       .append("rect")
       .attr("y", function(d) {
           return h - (d['rain'] * 4);
       })
       .attr("height", function(d) {
           return d['rain'] * 40;
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
           return "blue";
       })


     // show temp value
     /*
     svg.selectAll("text")
        .data(data)
        .enter()
        .append("text")
        .text(function(d) {
            //return Math.floor(d);
            return "";
        })
        .attr("font-family", "sans-serif")
        .attr("font-size", "6pt")
        .attr("fill", "black")
        .attr("y", function(d) {
            return h - (d['temp'] * 4) - 10;
        })
        .attr("x", function(d, i) {
            return (i * (w / data.length) + (w / data.length - barPadding) / 2 ) - 6
        });
        */
})
.catch( error => console.log("Error: " + error) );


// HEADER
d3.json("http://127.0.0.1:8000/data/latest-simple-weather-header.json").then( function(data) {
    return data;
})
.then(function(d) {
    // label
    d3.select("body") 
      .selectAll("h4")
      .data(d)
      .enter() 
      .append("h4")
      .text(function(d) {
	   return d;
       })
})
.catch( error => console.log("Error: " + error) );


