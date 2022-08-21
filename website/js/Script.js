$(document).ready(function() {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {
  
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
  
    });

    $("#Legal").click(function(){
        $("#Legal").addClass("is-active");
        $("#Original").removeClass("is-active");
        $("#Final").removeClass("is-active");
        $(".legal").removeClass("is-hidden");
        $(".original").addClass("is-hidden");
        $(".final").addClass("is-hidden");
    });

    $("#Original").click(function(){
        $("#Legal").removeClass("is-active");
        $("#Original").addClass("is-active");
        $("#Final").removeClass("is-active");
        $(".legal").addClass("is-hidden");
        $(".original").removeClass("is-hidden");
        $(".final").addClass("is-hidden");
    });

    $("#Final").click(function(){
        $("#Legal").removeClass("is-active");
        $("#Original").removeClass("is-active");
        $("#Final").addClass("is-active");
        $(".legal").addClass("is-hidden");
        $(".original").addClass("is-hidden");
        $(".final").removeClass("is-hidden");
    });

  });

document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Fruit Consumption'
        },
        xAxis: {
            categories: ['Apples', 'Bananas', 'Oranges']
        },
        yAxis: {
            title: {
                text: 'Fruit eaten'
            }
        },
        series: [{
            name: 'Jane',
            data: [1, 0, 4]
        }, {
            name: 'John',
            data: [5, 7, 3]
        }]
    });

(async () => {

    const mapData = await fetch(
        'website/data/emilia.json'
    ).then(response => response.json());

    
    Highcharts.getJSON('website/data/MD2.json', function (data) {
    
        data.forEach(function (p) {
            p.lon = p.longitude
            p.lat = p.latitude
            p.name = p.municipality
            p.type = p.type
        });
        
        Highcharts.mapChart('container2', {
          chart: {
            map: mapData
          },
          title: {
            text: 'Water disaster in Emilia Romagna'
          },
          mapNavigation: {
            enabled: true
          },
          tooltip: {
            formatter: function () {
              if (this.point.clusteredData) {
                if (this.point.clusterPointsAmount){
                    const x = new Set();
                    const y = new Set();
                    const val = [];
                    let i = 0;
                    this.point.clusteredData.forEach (function(value) {
                        x.add(value['x']);
                        y.add(value['y']);
                        val[i] = value.options.type;
                        i++;
                    });
                    if (x.size == 1 && y.size == 1){
                      const iterator1 = x.values();
                      const iterator2 = y.values();
                      const arr = []
                      let i = 0;
                      let j = 1;
                      val.forEach (function(dis) {
                          if (arr.includes(dis) == true){
                            if (arr.length == 2){
                              arr[1] = j+1;
                            }
                            if (arr.length == 4){
                              arr[3] = j+1;
                            }
                            if (arr.length == 6){
                              arr[5] = j+1;
                            }
                            if (arr.length == 8){
                              arr[7] = j+1;
                            }
                          }
                          if (arr.includes(dis) == false){
                            arr[i] = dis;
                            i++; 
                            arr[i] = j;
                            i++;
                          }
                          console.log(arr);
                      });
    
                      return '<b>' + this.point.clusteredData[0].options.name + '</b><br>' + arr.join('-') + '</b><br>Lat: ' + iterator1.next().value.toFixed(2) + ', Lon: ' + iterator2.next().value.toFixed(2);
                    }
    
                  }
                return 'Clustered points: ' + this.point.clusterPointsAmount;
              }
              return '<b>' + this.point.municipality + '</b><br>' + this.point.type + '</b><br>Lat: ' + this.point.lat.toFixed(2) + ', Lon: ' + this.point.lon.toFixed(2);
            }
          },
          colorAxis: {
            min: 0,
            max: 20
          },
          plotOptions: {
            mappoint: {
              cluster: {
                enabled: true,
                allowOverlap: false,
                animation: {
                  duration: 450
                },
                layoutAlgorithm: {
                  type: 'grid',
                  gridSize: 70
                },
                zones: [{
                  from: 1,
                  to: 4,
                  marker: {
                    radius: 13
                  }
                }, {
                  from: 5,
                  to: 9,
                  marker: {
                    radius: 15
                  }
                }, {
                  from: 10,
                  to: 15,
                  marker: {
                    radius: 17
                  }
                }, {
                  from: 16,
                  to: 20,
                  marker: {
                    radius: 19
                  }
                }, {
                  from: 21,
                  to: 100,
                  marker: {
                    radius: 21
                  }
                }]
              }
            }
          },
          series: [{
            name: 'Basemap',
            borderColor: '#A0A0A0',
            nullColor: 'rgba(200, 200, 200, 0.3)',
            showInLegend: false
          }, {
            type: 'mappoint',
            enableMouseTracking: true,
            colorKey: 'clusterPointsAmount',
            name: 'name',
            color: Highcharts.getOptions().colors[1],
            data: data
          }]
        });
      });
    
    })();
   
});


