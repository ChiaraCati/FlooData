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

    const topology = await fetch(
        'website/data/emilia.json'
    ).then(response => response.json());

    
   Highcharts.getJSON('website/data/MD4.json', function (data) {
    
    
        // Instantiate the map
        Highcharts.mapChart('container2', {
    
            chart: {
                map: topology,
            },
    
            title: {
                text: 'Emilia Romagna population density (/km²)'
            },
           
            mapNavigation: {
                enabled: true
            },
    
            colorAxis: {
                min: 1,
                type: 'logarithmic',
                minColor: '#EEEEFF',
                maxColor: '#035f9c',
                stops: [
                    [0, '#EFEFFF'],
                    [0.67, '#85ceff'],
                    [1, '#035f9c']
                ]
            },
    
            series: [{
                data: data,
                joinBy: ['postal-code', 'prov_code'],
                name: 'Population density',
                states: {
                  hover: {
                    color: '#a4edba'
                  }
                },
                tooltip: {
                  valueSuffix: '/km²'
                }
              }]
            
        });
    });
    
    })();
   
});


