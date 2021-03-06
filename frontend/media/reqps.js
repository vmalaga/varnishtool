// Connect to stats db
var db = openDatabase('STATSDB', '1.0', 'Stats DB', 10 * 1024);
var chart;

$(document).ready(function() {
    Highcharts.setOptions({
    	global: {
    		useUTC: false
		}
    });

    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container',
            type: 'spline',
            marginRight: 0,
            events: {
                load: function() {

                    // set up the updating of the chart each 5 seconds
                    var series = this.series[0];
                    setInterval(function() {
                           // get delta value from websql
                            db.transaction(function(tx) {
                                var query = "select (select t2.statvalue from stats t1, stats t2 where t1.statdate < t2.statdate and t1.statname='client_requests' and t2.statname='client_requests' order by t1.statdate desc limit 1) as nowvalue, (select t1.statvalue from stats t1, stats t2 where t1.statdate < t2.statdate and t1.statname='client_requests' and t2.statname='client_requests'  order by t1.statdate desc limit 1) as lastvalue"
                                tx.executeSql( query , [] , function (tx, results) {
                                    var nowvalue = results.rows.item(0).nowvalue;
                                    var lastvalue = results.rows.item(0).lastvalue;
                                    var deltavalue = nowvalue - lastvalue;
                                    var x = (new Date()).getTime() // current time
                                    series.addPoint([x, deltavalue], true, true);
                                    console.log(deltavalue);
                                });
                            });
                    }, 5000);
                }
            }
        },
        title: {
            text: 'Client Requests'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            title: {
                text: 'Requests',
                margin: 20
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }],
            min: 0
        },
        tooltip: {
            formatter: function() {
                    return '<b>'+ this.series.name +'</b><br/>'+
                    Highcharts.dateFormat('%d-%m-%Y %H:%M:%S', this.x) +'<br/>'+
                    Highcharts.numberFormat(this.y, 0);
            }
        },
        legend: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        series: [{
            name: 'Requests',
            data: (function() {
                    // generate an array of random data
                    var data = [],
                        time = (new Date()).getTime(),
                        i;
    
                    for (i = -19; i <= 0; i++) {
                        data.push({
                            x: time + i * 1000,
                            y: 0
                        });
                    }
                    return data;
                })()
        }]
    });
    });
