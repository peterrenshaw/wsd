# WSD ☀️🌤️🌦️🌧️                                 

![WSD: latest weather](https://github.com/peterrenshaw/wsd/blob/master/www/latest-simple-weather.png)

BUGS

* 2018DEC06

abstract: problems with unit selection with recognition on internal keys in dict.

1) reproduce

```

    ./se.py -s "2018DEC05" -e "2018DEC06" -i 4 -u hour

```

2) what I want

```

   list of data between date A and date B in four hourly intervals.

```

3) what I got

```

Warning: lst2int start<10> and end<12> not inside len<9>

Warning: lst2int start<13> and end<15> not inside len<9>

Warning: lst2int start<16> and end<18> not inside len<9>
dtd=<{'second': 0, 'year': 2018, 'hour': 0, 'minute': 0, 'day': 5, 'month': 12}>
data=<{'second': 0, 'year': 2018, 'hour': 0, 'minute': 0, 'day': 5, 'month': 12}>

Warning: lst2int start<10> and end<12> not inside len<9>

Warning: lst2int start<13> and end<15> not inside len<9>

Warning: lst2int start<16> and end<18> not inside len<9>
dtd=<{'second': 0, 'year': 2018, 'hour': 0, 'minute': 0, 'day': 6, 'month': 12}>
data=<{'second': 0, 'year': 2018, 'hour': 0, 'minute': 0, 'day': 6, 'month': 12}>

Error: dt_new_delta did not supply valid unit <hour>

```


