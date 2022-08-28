$(document).ready(function() {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {
  
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
  
    });

    // Check for click events on the risk chart menu
    // Hydraulic risk
    $("#Hydraulic").click(function(){
      $(".hydraulic").toggleClass("is-hidden")
      $("#Hydraulic > span > ion-icon").toggleClass("down");
      $(".landslide").addClass("is-hidden")
      $("#Landslide > span > ion-icon").removeClass("down");
      $(".hydraulic_risk").removeClass("is-hidden");
      $(".landslide_risk").addClass("is-hidden");
      $("#high_hydraulic_risk_area_p3" ).trigger('click');
    });
    
    $(".hydraulic > .panel-tabs > #Area").click(function(){
      $(".hydraulic > .panel-tabs > #Area").addClass("is-active");
      $(".hydraulic > .panel-tabs > #Population").removeClass("is-active");
      $(".hydraulic > .panel-tabs > #Families").removeClass("is-active");
      $(".hydraulic > .panel-tabs > #Buildings").removeClass("is-active");
      $(".hydraulic > .panel-tabs > #Enterprises").removeClass("is-active");
      $(".hydraulic > .panel-tabs > #C_Heritage").removeClass("is-active");
      $(".hydraulic > .area").removeClass("is-hidden");
      $(".hydraulic > .population").addClass("is-hidden");
      $(".hydraulic > .families").addClass("is-hidden");
      $(".hydraulic > .buildings").addClass("is-hidden");
      $(".hydraulic > .enterprises").addClass("is-hidden");
      $(".hydraulic > .c_heritage").addClass("is-hidden");
      $(".hydraulic_risk > .area").removeClass("is-hidden");
      $(".hydraulic_risk > .population").addClass("is-hidden");
      $(".hydraulic_risk > .families").addClass("is-hidden");
      $(".hydraulic_risk > .buildings").addClass("is-hidden");
      $(".hydraulic_risk > .enterprises").addClass("is-hidden");
      $(".hydraulic_risk > .c_heritage").addClass("is-hidden");
      $("#high_hydraulic_risk_area_p3" ).trigger('click');

  })

    $(".hydraulic > .panel-tabs > #Population").click(function(){
      $(".hydraulic > .panel-tabs > #Area").removeClass("is-active");
      $(".hydraulic > .panel-tabs > #Population").addClass("is-active");
      $(".hydraulic > .panel-tabs > #Families").removeClass("is-active");
      $(".hydraulic > .panel-tabs > #Buildings").removeClass("is-active");
      $(".hydraulic > .panel-tabs > #Enterprises").removeClass("is-active");
      $(".hydraulic > .panel-tabs > #C_Heritage").removeClass("is-active");
      $(".hydraulic > .area").addClass("is-hidden");
      $(".hydraulic > .population").removeClass("is-hidden");
      $(".hydraulic > .families").addClass("is-hidden");
      $(".hydraulic > .buildings").addClass("is-hidden");
      $(".hydraulic > .enterprises").addClass("is-hidden");
      $(".hydraulic > .c_heritage").addClass("is-hidden");
      $(".hydraulic_risk > .area").addClass("is-hidden");
        $(".hydraulic_risk > .population").removeClass("is-hidden");
        $(".hydraulic_risk > .families").addClass("is-hidden");
        $(".hydraulic_risk > .buildings").addClass("is-hidden");
        $(".hydraulic_risk > .enterprises").addClass("is-hidden");
        $(".hydraulic_risk > .c_heritage").addClass("is-hidden");
        $("#high_hydraulic_risk_population_p3" ).trigger('click');

  })

  $(".hydraulic > .panel-tabs > #Families").click(function(){
    $(".hydraulic > .panel-tabs > #Area").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Population").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Families").addClass("is-active");
    $(".hydraulic > .panel-tabs > #Buildings").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Enterprises").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #C_Heritage").removeClass("is-active");
    $(".hydraulic > .area").addClass("is-hidden");
    $(".hydraulic > .population").addClass("is-hidden");
    $(".hydraulic > .families").removeClass("is-hidden");
    $(".hydraulic > .buildings").addClass("is-hidden");
    $(".hydraulic > .enterprises").addClass("is-hidden");
    $(".hydraulic > .c_heritage").addClass("is-hidden");
    $(".hydraulic_risk > .area").addClass("is-hidden");
        $(".hydraulic_risk > .population").addClass("is-hidden");
        $(".hydraulic_risk > .families").removeClass("is-hidden");
        $(".hydraulic_risk > .buildings").addClass("is-hidden");
        $(".hydraulic_risk > .enterprises").addClass("is-hidden");
        $(".hydraulic_risk > .c_heritage").addClass("is-hidden");
        $("#high_hydraulic_risk_family_p3" ).trigger('click');

  })

  $(".hydraulic > .panel-tabs > #Buildings").click(function(){
    $(".hydraulic > .panel-tabs > #Area").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Population").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Families").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Buildings").addClass("is-active");
    $(".hydraulic > .panel-tabs > #Enterprises").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #C_Heritage").removeClass("is-active");
    $(".hydraulic > .area").addClass("is-hidden");
    $(".hydraulic > .population").addClass("is-hidden");
    $(".hydraulic > .families").addClass("is-hidden");
    $(".hydraulic > .buildings").removeClass("is-hidden");
    $(".hydraulic > .enterprises").addClass("is-hidden");
    $(".hydraulic > .c_heritage").addClass("is-hidden");
    $(".hydraulic_risk > .area").addClass("is-hidden");
        $(".hydraulic_risk > .population").addClass("is-hidden");
        $(".hydraulic_risk > .families").addClass("is-hidden");
        $(".hydraulic_risk > .buildings").removeClass("is-hidden");
        $(".hydraulic_risk > .enterprises").addClass("is-hidden");
        $(".hydraulic_risk > .c_heritage").addClass("is-hidden");
        $("#high_hydraulic_risk_building_p3" ).trigger('click');

  })

  $(".hydraulic > .panel-tabs > #Enterprises").click(function(){
    $(".hydraulic > .panel-tabs > #Area").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Population").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Families").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Buildings").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Enterprises").addClass("is-active");
    $(".hydraulic > .panel-tabs > #C_Heritage").removeClass("is-active");
    $(".hydraulic > .area").addClass("is-hidden");
    $(".hydraulic > .population").addClass("is-hidden");
    $(".hydraulic > .families").addClass("is-hidden");
    $(".hydraulic > .buildings").addClass("is-hidden");
    $(".hydraulic > .enterprises").removeClass("is-hidden");
    $(".hydraulic > .c_heritage").addClass("is-hidden");
    $(".hydraulic_risk > .area").addClass("is-hidden");
        $(".hydraulic_risk > .population").addClass("is-hidden");
        $(".hydraulic_risk > .families").addClass("is-hidden");
        $(".hydraulic_risk > .buildings").addClass("is-hidden");
        $(".hydraulic_risk > .enterprises").removeClass("is-hidden");
        $(".hydraulic_risk > .c_heritage").addClass("is-hidden");
        $("#high_hydraulic_risk_enterprise_p3" ).trigger('click');

  })

  $(".hydraulic > .panel-tabs > #C_Heritage").click(function(){
    $(".hydraulic > .panel-tabs > #Area").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Population").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Families").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Buildings").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #Enterprises").removeClass("is-active");
    $(".hydraulic > .panel-tabs > #C_Heritage").addClass("is-active");
    $(".hydraulic > .area").addClass("is-hidden");
    $(".hydraulic > .population").addClass("is-hidden");
    $(".hydraulic > .families").addClass("is-hidden");
    $(".hydraulic > .buildings").addClass("is-hidden");
    $(".hydraulic > .enterprises").addClass("is-hidden");
    $(".hydraulic > .c_heritage").removeClass("is-hidden");
    $(".hydraulic_risk > .area").addClass("is-hidden");
        $(".hydraulic_risk > .population").addClass("is-hidden");
        $(".hydraulic_risk > .families").addClass("is-hidden");
        $(".hydraulic_risk > .buildings").addClass("is-hidden");
        $(".hydraulic_risk > .enterprises").addClass("is-hidden");
        $(".hydraulic_risk > .c_heritage").removeClass("is-hidden");
        $("#high_hydraulic_risk_cultural_heritage_p3" ).trigger('click');

  })

  // Landslide risk
  $("#Landslide").click(function(){
    $(".landslide").toggleClass("is-hidden")
    $("#Landslide > span > ion-icon").toggleClass("down");
    $(".hydraulic").addClass("is-hidden")
    $("#Hydraulic > span > ion-icon").removeClass("down");
    $(".hydraulic_risk").addClass("is-hidden");
    $(".landslide_risk").removeClass("is-hidden");
    $("#very_high_landslide_risk_area_p4").trigger('click');
  });

  $(".landslide > .panel-tabs > #Area").click(function(){
    $(".landslide > .panel-tabs > #Area").addClass("is-active");
    $(".landslide > .panel-tabs > #Population").removeClass("is-active");
    $(".landslide > .panel-tabs > #Families").removeClass("is-active");
    $(".landslide > .panel-tabs > #Buildings").removeClass("is-active");
    $(".landslide > .panel-tabs > #Enterprises").removeClass("is-active");
    $(".landslide > .panel-tabs > #C_Heritage").removeClass("is-active");
    $(".landslide > .area").removeClass("is-hidden");
    $(".landslide > .population").addClass("is-hidden");
    $(".landslide > .families").addClass("is-hidden");
    $(".landslide > .buildings").addClass("is-hidden");
    $(".landslide > .enterprises").addClass("is-hidden");
    $(".landslide > .c_heritage").addClass("is-hidden");
    $(".landslide_risk > .area").removeClass("is-hidden");
        $(".landslide_risk > .population").addClass("is-hidden");
        $(".landslide_risk > .families").addClass("is-hidden");
        $(".landslide_risk > .buildings").addClass("is-hidden");
        $(".landslide_risk > .enterprises").addClass("is-hidden");
        $(".landslide_risk > .c_heritage").addClass("is-hidden");
        $("#very_high_landslide_risk_area_p4").trigger('click');
  })

  $(".landslide > .panel-tabs > #Population").click(function(){
  $(".landslide > .panel-tabs > #Area").removeClass("is-active");
  $(".landslide > .panel-tabs > #Population").addClass("is-active");
  $(".landslide > .panel-tabs > #Families").removeClass("is-active");
  $(".landslide > .panel-tabs > #Buildings").removeClass("is-active");
  $(".landslide > .panel-tabs > #Enterprises").removeClass("is-active");
  $(".landslide > .panel-tabs > #C_Heritage").removeClass("is-active");
  $(".landslide > .area").addClass("is-hidden");
  $(".landslide > .population").removeClass("is-hidden");
  $(".landslide > .families").addClass("is-hidden");
  $(".landslide > .buildings").addClass("is-hidden");
  $(".landslide > .enterprises").addClass("is-hidden");
  $(".landslide > .c_heritage").addClass("is-hidden");
  $(".landslide_risk > .area").addClass("is-hidden");
        $(".landslide_risk > .population").removeClass("is-hidden");
        $(".landslide_risk > .families").addClass("is-hidden");
        $(".landslide_risk > .buildings").addClass("is-hidden");
        $(".landslide_risk > .enterprises").addClass("is-hidden");
        $(".landslide_risk > .c_heritage").addClass("is-hidden");
        $("#very_high_landslide_risk_population_p4").trigger('click');
  })

  $(".landslide > .panel-tabs > #Families").click(function(){
  $(".landslide > .panel-tabs > #Area").removeClass("is-active");
  $(".landslide > .panel-tabs > #Population").removeClass("is-active");
  $(".landslide > .panel-tabs > #Families").addClass("is-active");
  $(".landslide > .panel-tabs > #Buildings").removeClass("is-active");
  $(".landslide > .panel-tabs > #Enterprises").removeClass("is-active");
  $(".landslide > .panel-tabs > #C_Heritage").removeClass("is-active");
  $(".landslide > .area").addClass("is-hidden");
  $(".landslide > .population").addClass("is-hidden");
  $(".landslide > .families").removeClass("is-hidden");
  $(".landslide > .buildings").addClass("is-hidden");
  $(".landslide > .enterprises").addClass("is-hidden");
  $(".landslide > .c_heritage").addClass("is-hidden");
  $(".landslide_risk > .area").addClass("is-hidden");
        $(".landslide_risk > .population").addClass("is-hidden");
        $(".landslide_risk > .families").removeClass("is-hidden");
        $(".landslide_risk > .buildings").addClass("is-hidden");
        $(".landslide_risk > .enterprises").addClass("is-hidden");
        $(".landslide_risk > .c_heritage").addClass("is-hidden");
        $("#very_high_landslide_risk_family_p4").trigger('click');
  })

  $(".landslide > .panel-tabs > #Buildings").click(function(){
  $(".landslide > .panel-tabs > #Area").removeClass("is-active");
  $(".landslide > .panel-tabs > #Population").removeClass("is-active");
  $(".landslide > .panel-tabs > #Families").removeClass("is-active");
  $(".landslide > .panel-tabs > #Buildings").addClass("is-active");
  $(".landslide > .panel-tabs > #Enterprises").removeClass("is-active");
  $(".landslide > .panel-tabs > #C_Heritage").removeClass("is-active");
  $(".landslide > .area").addClass("is-hidden");
  $(".landslide > .population").addClass("is-hidden");
  $(".landslide > .families").addClass("is-hidden");
  $(".landslide > .buildings").removeClass("is-hidden");
  $(".landslide > .enterprises").addClass("is-hidden");
  $(".landslide > .c_heritage").addClass("is-hidden");
  $(".landslide_risk > .area").addClass("is-hidden");
        $(".landslide_risk > .population").addClass("is-hidden");
        $(".landslide_risk > .families").addClass("is-hidden");
        $(".landslide_risk > .buildings").removeClass("is-hidden");
        $(".landslide_risk > .enterprises").addClass("is-hidden");
        $(".landslide_risk > .c_heritage").addClass("is-hidden");
        $("#very_high_landslide_risk_building_p4").trigger('click');
  })

  $(".landslide > .panel-tabs > #Enterprises").click(function(){
  $(".landslide > .panel-tabs > #Area").removeClass("is-active");
  $(".landslide > .panel-tabs > #Population").removeClass("is-active");
  $(".landslide > .panel-tabs > #Families").removeClass("is-active");
  $(".landslide > .panel-tabs > #Buildings").removeClass("is-active");
  $(".landslide > .panel-tabs > #Enterprises").addClass("is-active");
  $(".landslide > .panel-tabs > #C_Heritage").removeClass("is-active");
  $(".landslide > .area").addClass("is-hidden");
  $(".landslide > .population").addClass("is-hidden");
  $(".landslide > .families").addClass("is-hidden");
  $(".landslide > .buildings").addClass("is-hidden");
  $(".landslide > .enterprises").removeClass("is-hidden");
  $(".landslide > .c_heritage").addClass("is-hidden");
  $(".landslide_risk > .area").addClass("is-hidden");
        $(".landslide_risk > .population").addClass("is-hidden");
        $(".landslide_risk > .families").addClass("is-hidden");
        $(".landslide_risk > .buildings").addClass("is-hidden");
        $(".landslide_risk > .enterprises").removeClass("is-hidden");
        $(".landslide_risk > .c_heritage").addClass("is-hidden");
        $("#very_high_landslide_risk_enterprise_p4").trigger('click');
  })

  $(".landslide > .panel-tabs > #C_Heritage").click(function(){
  $(".landslide > .panel-tabs > #Area").removeClass("is-active");
  $(".landslide > .panel-tabs > #Population").removeClass("is-active");
  $(".landslide > .panel-tabs > #Families").removeClass("is-active");
  $(".landslide > .panel-tabs > #Buildings").removeClass("is-active");
  $(".landslide > .panel-tabs > #Enterprises").removeClass("is-active");
  $(".landslide > .panel-tabs > #C_Heritage").addClass("is-active");
  $(".landslide > .area").addClass("is-hidden");
  $(".landslide > .population").addClass("is-hidden");
  $(".landslide > .families").addClass("is-hidden");
  $(".landslide > .buildings").addClass("is-hidden");
  $(".landslide > .enterprises").addClass("is-hidden");
  $(".landslide > .c_heritage").removeClass("is-hidden");
  $(".landslide_risk > .area").addClass("is-hidden");
        $(".landslide_risk > .population").addClass("is-hidden");
        $(".landslide_risk > .families").addClass("is-hidden");
        $(".landslide_risk > .buildings").addClass("is-hidden");
        $(".landslide_risk > .enterprises").addClass("is-hidden");
        $(".landslide_risk > .c_heritage").removeClass("is-hidden");
        $("#very_high_landslide_risk_cultural_heritage_p4").trigger('click');
  })



    $("#LinkedIspra").click(function(){
      $(".linkedIspra").toggleClass("is-hidden");
      $("#LinkedIspra > span > ion-icon").toggleClass("down");
  })

    $("#MinERva").click(function(){
      $(".minerva").toggleClass("is-hidden");
      $("#MinERva > span > ion-icon").toggleClass("down");
  })

    $("#IdroGEO").click(function(){
      $(".idroGEO").toggleClass("is-hidden");
      $("#IdroGEO > span > ion-icon").toggleClass("down");
  })
    $("#OpenCoesione").click(function(){
      $(".openCoesione").toggleClass("is-hidden");
      $("#OpenCoesione > span > ion-icon").toggleClass("down");
  })

    $("#GitHub").click(function(){
      $(".gitHub").toggleClass("is-hidden");
      $("#GitHub > span > ion-icon").toggleClass("down");
  })

    $("#MD1").click(function(){
      $(".md1").toggleClass("is-hidden");
      $("#MD1 > span > ion-icon").toggleClass("down");
  })

    $("#MD2").click(function(){
      $(".md2").toggleClass("is-hidden");
      $("#MD2 > span > ion-icon").toggleClass("down");
  })

    $("#MD3").click(function(){
      $(".md3").toggleClass("is-hidden");
      $("#MD3 > span > ion-icon").toggleClass("down");
  })
    $("#Rendis").click(function(){
        $("#Rendis").addClass("is-active");
        $("#Luoghi").removeClass("is-active");
        $(".rendis").removeClass("is-hidden");
        $(".luoghi").addClass("is-hidden");
    })

    $("#Luoghi").click(function(){
      $("#Luoghi").addClass("is-active");
      $("#Rendis").removeClass("is-active");
      $(".luoghi").removeClass("is-hidden");
      $(".rendis").addClass("is-hidden");
  })

  $("#SegnalazioniFenomeni").click(function(){
    $("#SegnalazioniFenomeni").addClass("is-active");
    $("#OpereDifesa").removeClass("is-active");
    $("#DinamicaMeteomarina").removeClass("is-active");
    $(".segnalazioniFenomeni").removeClass("is-hidden");
    $(".opereDifesa").addClass("is-hidden");
    $(".dinamicaMeteomarina").addClass("is-hidden");
})

  $("#OpereDifesa").click(function(){
    $("#OpereDifesa").addClass("is-active");
    $("#SegnalazioniFenomeni").removeClass("is-active");
    $("#DinamicaMeteomarina").removeClass("is-active");
    $(".opereDifesa").removeClass("is-hidden");
    $(".segnalazioniFenomeni").addClass("is-hidden");
    $(".dinamicaMeteomarina").addClass("is-hidden");
  })
  $("#DinamicaMeteomarina").click(function(){
    $("#DinamicaMeteomarina").addClass("is-active");
    $("#SegnalazioniFenomeni").removeClass("is-active");
    $("#OpereDifesa").removeClass("is-active");
    $(".dinamicaMeteomarina").removeClass("is-hidden");
    $(".segnalazioniFenomeni").addClass("is-hidden");
    $(".opereDifesa").addClass("is-hidden");
  })

  $("#Progetti1").click(function(){
    $("#Progetti1").addClass("is-active");
    $("#Progetti2").removeClass("is-active");
    $(".progetti1").removeClass("is-hidden");
    $(".progetti2").addClass("is-hidden");
})

$("#Progetti2").click(function(){
  $("#Progetti2").addClass("is-active");
  $("#Progetti1").removeClass("is-active");
  $(".progetti2").removeClass("is-hidden");
  $(".progetti1").addClass("is-hidden");
})


    $("#Catalogue").click(function(){
        $("#Catalogue").addClass("is-active");
        $("#Original").removeClass("is-active");
        $("#Final").removeClass("is-active");
        $(".catalogue").removeClass("is-hidden");
        $(".original").addClass("is-hidden");
        $(".final").addClass("is-hidden");
    });

    $("#Original").click(function(){
        $("#Catalogue").removeClass("is-active");
        $("#Original").addClass("is-active");
        $("#Final").removeClass("is-active");
        $(".catalogue").addClass("is-hidden");
        $(".original").removeClass("is-hidden");
        $(".final").addClass("is-hidden");
    });

    $("#Final").click(function(){
        $("#Catalogue").removeClass("is-active");
        $("#Original").removeClass("is-active");
        $("#Final").addClass("is-active");
        $(".catalogue").addClass("is-hidden");
        $(".original").addClass("is-hidden");
        $(".final").removeClass("is-hidden");
    });

  });

document.addEventListener('DOMContentLoaded', function () {
    
  (async () => {

      const topology = await fetch(
          'website/data/emilia.json'
      ).then(response => response.json());

      //disaster cluster map
      Highcharts.getJSON('website/data/MD2.json', function (data) {
      
        data.forEach(function (p) {
            p.lon = p.longitude
            p.lat = p.latitude
            p.name = p.municipality.charAt(0).toUpperCase() + p.municipality.slice(1)
            p.type = p.type
        });
        
        Highcharts.mapChart('disaster_map', {
          chart: {
            map: topology
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
                          }s
                      });
    
                      return '<b>' + this.point.clusteredData[0].options.name + '</b><br>' + arr.join('-') + '</b><br>Lat: ' + iterator1.next().value.toFixed(2) + ', Lon: ' + iterator2.next().value.toFixed(2);
                    }
    
                  }
                return 'Clustered points: ' + this.point.clusterPointsAmount;
              }
              return '<b>' + this.point.name + '</b><br>' + this.point.type + '</b><br>Lat: ' + this.point.lat.toFixed(2) + ', Lon: ' + this.point.lon.toFixed(2);
            }
          },
          colorAxis: {
            start: 1,
            min: 0,
            max: 20,
            minColor: '#cff0eb',
            maxColor: '#01a189',
            stops: [
                [0, '#cff0eb'],
                [0.5, '#b6ffe9'],
                [0.7, '#03d1b2'],
                [1, '#01a189']
            ]
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

      const pieColors = (function () {
        const colors = [],
              base = Highcharts.getOptions().colors[9];
    
        for (i = 0; i < 10; i += 1) {
            // Start out with a darkened base color (negative brighten), and end
            // up with a much brighter color
            colors.push(Highcharts.color(base).brighten((i - 3) / 15).get());
        }
        return colors;
        
      }());

      const data_disaster = [
        {
            id: "0",
            parent: "",
            name: "Emilia-Romagna",
        },
        {
            id: "BO",
            parent: "0",
            name: "Bologna",
        },
        {
            id: "MO",
            parent: "0",
            name: "Modena",
        },
        {
          id: "FE",
          parent: "0",
          name: "Ferrara",
        },
        {
          id: "FC",
          parent: "0",
          name: "Forlì-Cesena",
        },
        {
          id: "PR",
          parent: "0",
          name: "Parma",
        },
        {
          id: "PC",
          parent: "0",
          name: "Piacenza",
        },
        {
          id: "RN",
          parent: "0",
          name: "Rimini",
        },
        {
          id: "RA",
          parent: "0",
          name: "Ravenna",
        },
        {
          id: "RE",
          parent: "0",
          name: "Reggio Emilia"
        },{
          id: "U_BO",
          parent: "BO",
          name: "Unknown",
          value: 1
        },{
        id: "WHW_BO",
        parent: "BO",
        name: "Wells with hot water",
        value:  10
        },{
          id: "GL_BO",
          parent: "BO",
          name: "Gas leaks from wells for water and / or from the ground",
          value:  7
        },{
          id: "FSG_BO",
          parent: "BO",
          name: "Presence of fractures and / or sinking into the ground",
          value: 1
        },{
          id: "I_BO",
          parent: "BO",
          name: "Idraulic",
          value: 42
        },{
          id: "L_BO",
          parent: "BO",
          name: "Landslide",
          value: 53
        },{
          id: "U_MO",
          parent: "MO",
          name: "Unknown",
          value: 2
        },{
          id: "WHW_MO",
          parent: "MO",
          name: "Wells with hot water",
          value: 30
        },{
          id: "GL_MO",
          parent: "MO",
          name: "Gas leaks from wells for water and / or from the ground",
          value:  11
        },{
          id: "FSG_MO",
          parent: "MO",
          name: "Presence of fractures and / or sinking into the ground",
          value:  3
        },{
          id: "I_MO",
          parent: "MO",
          name: "Idraulic",
          value:  9
        },{
          id: "VMS_MO",
          parent: "MO",
          name: "Volcanoes of mud and / or sand ",
          value: 2
        },{
          id: "L_MO",
          parent: "MO",
          name: "Landslide",
          value:  19
      
        },{
          id: "U_FE",
          parent: "FE",
          name: "Unknown",
          value: 1
        },{
          id: "CD_FE",
          parent: "FE",
          name: "Coastal Disruption",
          value:  2
        },{
          id: "CE_FE",
          parent: "FE",
          name: "Coast erosion",
          value: 12
        },{
          id: "WHW_FE",
          parent: "FE",
          name: "Wells with hot water",
          value: 3
        },{
          id: "GL_FE",
          parent: "FE",
          name: "Gas leaks from wells for water and / or from the ground",
          value: 10
        },{
          id: "FSG_FE",
          parent: "FE",
          name: "Presence of fractures and / or sinking into the ground",
          value:  4
        },{
          id: "I_FE",
          parent: "FE",
          name: "Idraulic",
          value: 4
        },{
          id: "VMS_FE",
          parent: "FE",
          name: "Volcanoes of mud and / or sand",
          value:  2
      
        },{
          id: "CD_FC",
          parent: "FC",
          name: "Coastal Disruption ",
          value: 1
        },{
          id: "CE_FC",
          parent: "FC",
          name: "Coastal erosion",
          value: 5
        },{
          id: "WHW_FC",
          parent: "FC",
          name: "Wells with hot water",
          value:  1
      
        },{
          id: "GL_FC",
          parent: "FC",
          name: "Gas leaks from wells for water and / or from the ground",
          value:  1
        },{
          id: "I_FC",
          parent: "FC",
          name: "Idraulic",
          value:  10
        },{
          id: "L_FC",
          parent: "FC",
          name: "Landslide",
          value: 32
        },{
          id: "I_PR",
          parent: "PR",
          name: "Idraulic",
          value:  27
        },{
          id: "L_PR",
          parent: "PR",
          name: "Landslide",
          value: 15
        },{
          id: "I_PC",
          parent: "PC",
          name: "Idraulic",
          value:  32
        },{
          id: "L_PC",
          parent: "PC",
          name: "Landslide",
          value: 23
        },{
          id: "CD_RN",
          parent: "RN",
          name: "Coastal Disruption",
          value:   5
        },{
          id: "CE_RN",
          parent: "RN",
          name: "Coast erosioN",
          value:  8
        },{
          id: "WHW_RN",
          parent: "RN",
          name: "Wells with hot water",
          value: 1
        },{
          id: "I_RN",
          parent: "RN",
          name: "Idraulic",
          value: 15
        },{
          id: "L_RN",
          parent: "RN",
          name: "Landslide",
          value: 27
        },{
          id: "CE_RA",
          parent: "RA",
          name: "Coast erosion",
          value:    13
        },{
          id: "WHW_RA",
          parent: "RA",
          name: "Wells with hot water",
          value:  2
        },{
          id: "GL_RA",
          parent: "RA",
          name: "Gas leaks from wells for water and / or from the ground",
          value: 2
        },{
          id: "I_RA",
          parent: "RA",
          name: "Idraulic",
          value:  22
        },{
          id: "L_RA",
          parent: "RA",
          name: "Landslide",
          value: 5
        },{
          id: "WHW_RE",
          parent: "RE",
          name: "Wells with hot water",
          value:  5
        },{
          id: "GL_RE",
          parent: "RE",
          name: "Gas leaks from wells for water and / or from the ground",
          value:  1
        },{
          id: "I_RE",
          parent: "RE",
          name: "Idraulic",
          value: 7
        },{
          id: "L_RE",
          parent: "RE",
          name: "Landslide",
          value: 22
        },{
          id: "VMS_RE",
          parent: "RE",
          name: "Volcanoes of mud and / or sand",
          value: 4
        }
      ];
      
      Highcharts.chart('disaster_sunburst', {
      
        chart: {
            height: '100%'
        },
      
        colors: ['transparent'].concat(Highcharts.getOptions().colors),
      
        title: {
            text: 'Water disaster divided by Emilia Romagna provinces'
        },
        
      plotOptions: {
        sunburst: {
          colors: pieColors
        }
      },
      
        series: [{
            type: 'sunburst',
            data: data_disaster,
            name: 'Root',
            allowDrillToNode: true,
            cursor: 'pointer',
            dataLabels: {
                format: '{point.name}',
                filter: {
                    property: 'innerArcLength',
                    operator: '>',
                    value: 16
                },
                rotationMode: 'circular'
            },
            levels: [{
                level: 1,
                levelIsConstant: false,
                dataLabels: {
                    filter: {
                        property: 'outerArcLength',
                        operator: '>',
                        value: 64
                    }
                }
            }, {
                level: 2,
                colorByPoint: true,
            },
            {
              level: 3,
              colorVariation: {
                  key: 'brightness',
                  to: -0.2
              },
            }]
      
        }],
      
        tooltip: {
            headerFormat: '',
            pointFormat: '<b>{point.name}</b> disasters are <b>{point.value}</b>'
        }
      });

      const radioButtons = document.querySelectorAll('input[name="data"]');
      for(const radioButton of radioButtons){
          radioButton.addEventListener('change', showSelected);
      }   

      function showSelected(e) {

          if (this.checked) {
              const value = this.value + '';
              Highcharts.getJSON('website/data/MD4.json', function (data) {
                
                  data.forEach(function (p) {
                      p.code = p.prov_code.toUpperCase();
                      p.value = p[value]
                  });

                  
          
                  // Instantiate the map
                  Highcharts.mapChart('risk_distribution_map', {

                      chart: {
                        map: topology,
                      },

                      title: {
                          text: 'Disaster risk in Emilia Romagna'
                      },

                      exporting: {
                          sourceWidth: 600,
                          sourceHeight: 500
                      },
          
                      legend: {
                          layout: 'horizontal',
                          borderWidth: 0,
                          backgroundColor: 'rgba(255,255,255,0.85)',
                          floating: true,
                          y: 25
                      },
          
                      mapNavigation: {
                          enabled: true
                      },
          
                      colorAxis: {
                        start: 1,
                        min: 0,
                        minColor: '#cff0eb',
                        maxColor: '#01a189',
                        stops: [
                            [0, '#cff0eb'],
                            [0.2, '#b6ffe9'],
                            [0.6, '#03d1b2'],
                            [1, '#01a189']
                        ]
                      },
          
                      series: [{
                          accessibility: {
                              point: {
                                  valueDescriptionFormat: '{xDescription}, {point.'+value+'3} percentage.'
                              }
                          },
                          animation: {
                              duration: 1000
                          },
                          data: data,
                          joinBy: ['postal-code', 'code'],
                          dataLabels: {
                              enabled: true,
                              color: '#FFFFFF',
                              format: '{point.code}'
                          },
                          name: 'Disaster risk factor',
                          tooltip: {
                              pointFormat: '{point.prov_name}: {point.'+value+'} %'
                          }
                      }
                  ]
                  });
              });
              
          }
      } 

      $("#high_hydraulic_risk_area_p3" ).trigger('click');

      Highcharts.chart("finance_bar", {

        chart: {
            type: "bar",
            zoomType: "y",
            height: 400,
        },
        title: {
            text: "Comparison of financing amounts per region"
        },
        xAxis: {
            labels: {
                style: {
                    fontWeight: 'bold'
                }
            },
            categories: ['Bologna',
            'Ferrara',
            'Forlì-Cesena',
            'Modena',
            'Parma',
            'Piacenza',
            'Ravenna',
            'Reggio Emilia',
            'Rimini'],
            title: {
                text: null
            },
            accessibility: {
                description: "Provinces"
            }
        },
        yAxis: {
            
            visible: false
          
        },
        plotOptions: {
            bar: {
                pointWidth: 13,
            },
            series: {
                groupPadding: 0.0,
                pointPadding: 0,
                borderWidth: 0
            }
        },
        tooltip: {
            valueSuffix: "€",
            stickOnContact: true,
            backgroundColor: "rgba(255, 255, 255, 0.95)"
        },
        legend: {
            enabled: true

        },
        series: [
            {
                "name": "Preventive measure",
                "data": [1.92315691e+09, 2.49988718e+08, 2.48306967e+08, 4.64813494e+08,
                                3.29757098e+08, 3.70357333e+08, 3.12735264e+08, 3.82570784e+08,
                                3.06467836e+08],
                 "color" : '#03d1b2'           
            },
            {
                "name": "Reparatory intervention",
                "data": [1.01115056e+08, 5.63814256e+07, 4.03156537e+07, 3.75226643e+07,
                                1.19907178e+08, 4.75190759e+07, 3.58897010e+07, 3.19237634e+07,
                                4.71110397e+07],
                "color" : '#cff0eb'
            }
        ]
        
        });


        const data_finance = [
          {
              id: "0",
              parent: "",
              name: "Emilia-Romagna",
          
          },
          {
              id: "BO",
              parent: "0",
              name: "Bologna",
          
          },
          {
              id: "MO",
              parent: "0",
              name: "Modena",
          
          },
          {
            id: "FE",
            parent: "0",
            name: "Ferrara",
        
          },
          {
            id: "FC",
            parent: "0",
            name: "Forlì-Cesena",
        
          },
          {
            id: "PR",
            parent: "0",
            name: "Parma",
        
          },
          {
            id: "PC",
            parent: "0",
            name: "Piacenza",
        
          },
          {
            id: "RN",
            parent: "0",
            name: "Rimini",
        
          },
          {
            id: "RA",
            parent: "0",
            name: "Ravenna",
        
          },
          {
            id: "RE",
            parent: "0",
            name: "Reggio Emilia",
        
          },{
            id: "EST_BO",
            parent: "BO",
            name: "Environmental safeguarding technologies",
            value: 11831375.68
          },{
            id: "CDS_BO",
            parent: "BO",
            name: "Contaminated and/or degraded sites",
            value: 3364855.0
          },{
            id: "UWN_BO",
            parent: "BO",
            name: "Urban water networks",
            value: 1430000.0
          },{
            id: "CPEME_BO",
            parent: "BO",
            name: "Control and protection of the Earth and Marino environment",
            value: 22380.68
          },{
            id: "WA_BO",
            parent: "BO",
            name: "Water adjustment",
            value: 26002685.0
          },{
            id: "W_BO",
            parent: "BO",
            name: "Waterways",
            value:  1135091.3599999999
          },{
            id: "L_BO",
            parent: "BO",
            name: "Landslide",
            value: 15187218.44
          },{
            id: "F_BO",
            parent: "BO",
            name: "Flood",
            value: 80522290.32
          }, {
            id: "O_BO",
            parent: "BO",
            name: "Others",
            value: 1884776073.43
          },{
            id: "EST_MO",
            parent: "MO",
            name: "Environmental safeguarding technologies",
            value: 4339314.98
          },{
            id: "UWN_MO",
            parent: "MO",
            name: "Urban water networks ",
            value: 2189800.0
          },{
            id: "WA_MO",
            parent: "MO",
            name: "Water adjustment",
            value: 180118.75
          },{
            id: "W_MO",
            parent: "MO",
            name: "Waterways",
            value: 2239500.0
          },{
            id: "L_MO",
            parent: "MO",
            name: "Landslide",
            value: 12717202.63
          },{
            id: "F_MO",
            parent: "MO",
            name: "Flood",
            value: 21796861.65
          },{
            id: "O_MO",
            parent: "MO",
            name: "Others",
            value: 458873360.25
          },{
            id: "EST_FE",
            parent: "FE",
            name: "Environmental safeguarding technologies",
            value: 4339314.98
          },{
            id: "UWN_FE",
            parent: "FE",
            name: "Urban water networks",
            value: 2189800.0
          },{
            id: "WA_FE",
            parent: "FE",
            name: "Water adjustmenst",
            value: 180118.75
          },{
            id: "W_FE",
            parent: "FE",
            name: "Waterways",
            value: 2239500.0
          },{
            id: "L_FE",
            parent: "FE",
            name: "Landslide",
            value: 12717202.63
          },{
            id: "F_FE",
            parent: "FE",
            name: "Flood",
            value: 21796861.65
          },{
            id: "O_FE",
            parent: "FE",
            name: "Others",
            value: 458873360.25
          },{
            id: "EST_FC",
            parent: "FC",
            name: "Environmental safeguarding technologies",
            value: 1186130.12
          },{
            id: "UWN_FC",
            parent: "FC",
            name: "Urban water networks",
            value: 800000.0
          },{
            id: "C_FC",
            parent: "FC",
            name: "Coastal",
            value: 225855.75
          },{
            id: "FIS_FC",
            parent: "FC",
            name: "Fluvial infrastructures/structures",
            value: 300000.0
          },{
            id: "WA_FC",
            parent: "FC",
            name: "Water adjustment",
            value: 150000.0
          },{
            id: "W_FC",
            parent: "FC",
            name: "Waterways",
            value: 607914.0
          },{
            id: "B_FC",
            parent: "FC",
            name: "Beaces",
            value: 215855.75
          },{
            id: "L_FC",
            parent: "FC",
            name: "Landslide",
            value: 13626347.08
          },{
            id: "F_FC",
            parent: "FC",
            name: "Flood",
            value: 23248450.9 
          },{
            id: "O_FC",
            parent: "FC",
            name: "Others",
            value: 248262067.41
          },{
            id: "EST_PR",
            parent: "PR",
            name: "Environmental safeguarding technologies",
            value: 1179898.92
          },{
            id: "UWN_PR",
            parent: "PR",
            name: "Urban water networks",
            value: 3206538.51
          },{
            id: "CDS_PR",
            parent: "PR",
            name: "Contaminated and/or degraded sites",
            value: 5817142.65
          },{
            id: "W_PR",
            parent: "PR",
            name: "Waterways",
            value: 9816100.0
          },{
            id: "L_PR",
            parent: "PR",
            name: "Landslide",
            value: 18370147.85
          },{
            id: "F_PR",
            parent: "PR",
            name: "Flood",
            value: 99987030.23
          },{
            id: "O_PR",
            parent: "PR",
            name: "Others",
            value: 311287417.44000006
          },{
            id: "EST_PC",
            parent: "PC",
            name: "Environmental safeguarding technologies",
            value: 676525.37
          },{
            id: "UWN_PC",
            parent: "PC",
            name: "Urban water network",
            value: 4043316.53
          },{
            id: "WA_PC",
            parent: "PC",
            name: "Water adjustment",
            value: 1336086.37
          },{
            id: "W_PC",
            parent: "PC",
            name: "Waterways",
            value:  135439.32
          },{
            id: "L_PC",
            parent: "PC",
            name: "Landslide",
            value: 14050175.030000001
          },{
            id: "F_PC",
            parent: "PC",
            name: "Flood",
            value: 30518900.89
          },{
            id: "O_PC",
            parent: "PC",
            name: "Others",
            value: 367115965.61
          },{
            id: "EST_RN",
            parent: "RN",
            name: "Environmental safeguarding technologies",
            value:  1772732.1
          },{
            id: "UWN_RN",
            parent: "RN",
            name: "Uban water networks",
            value: 870000.0
          },{
            id: "C_RN",
            parent: "RN",
            name: "Coastal",
            value: 8495524.7 
          },{
            id: "WA_RN",
            parent: "RN",
            name: "Water adjustment",
            value: 200000.0
          },{
            id: "W_RN",
            parent: "RN",
            name: "Waterways",
            value: 653702.8
          },{
            id: "B_RN",
            parent: "RN",
            name: "Beaches",
            value: 175124.7
          },{
            id: "L_RN",
            parent: "RN",
            name: "Landslide",
            value: 12768970.27
          },{
            id: "F_RN",
            parent: "RN",
            name: "Flood",
            value: 20304063.76
          },{
            id: "O_RN",
            parent: "RN",
            name: "Others",
            value: 308338757.08000004
          },{
            id: "EST_RA",
            parent: "RA",
            name: "Environmental safeguarding technologies",
            value:   3474685.75
          },{
            id: "UWN_RA",
            parent: "RA",
            name: "Urban water networks",
            value: 800000.0
          },{
            id: "WA_RA",
            parent: "RA",
            name: "Water adjustment",
            value: 2850000.0
          },{
            id: "W_RA",
            parent: "RA",
            name: "Waterways",
            value: 724464.0
          },{
            id: "B_RA",
            parent: "RA",
            name: "Beaches",
            value: 500000.0
          },{
            id: "L_RA",
            parent: "RA",
            name: "Landslide",
            value: 1436617.88
          },{
            id: "F_RA",
            parent: "RA",
            name: "Flood",
            value:  33953083.12
          },{
            id: "O_RA",
            parent: "RA",
            name: "Others",
            value: 304886114.56
          },{
            id: "EST_RE",
            parent: "RE",
            name: "Environmental safeguarding technologies",
            value: 4867623.59
          },{
            id: "UWN_RE",
            parent: "RE",
            name: "Urban water networks",
            value: 1740000.0
          },{
            id: "W_RE",
            parent: "RE",
            name: "Waterways",
            value: 6350000.0
          },{
            id: "L_RE",
            parent: "RE",
            name: "Landslide",
            value: 15727261.7
          },{
            id: "F_RE",
            parent: "RE",
            name: "Flood",
            value: 14225701.74
          },{
            id: "O_RE",
            parent: "RE",
            name: "Others",
            value: 371583960.73
          }
          
          
        
        ];
        
        Highcharts.chart("finance_sunburst", {
          chart: {
              height: "100%"
          },

          colors: ['transparent'].concat(Highcharts.getOptions().colors),
        
          title: {
              text: "Amount of financings - by province & type"
          },

          plotOptions: {
              sunburst: {
              colors: pieColors
            }
            },

          series: [{
            type: 'sunburst',
            data: data_finance,
            name: 'Root',
            allowDrillToNode: true,
            cursor: 'pointer',
            dataLabels: {
                format: '{point.name}',
                filter: {
                    property: 'innerArcLength',
                    operator: '>',
                    value: 16
                },
                rotationMode: 'circular'
            },
            levels: [{
                level: 1,
                levelIsConstant: false,
                dataLabels: {
                    filter: {
                        property: 'outerArcLength',
                        operator: '>',
                        value: 64
                    }
                }
            }, {
                level: 2,
                colorByPoint: true,
            },
            {
                level: 3,
                colorVariation: {
                    key: 'brightness',
                    to: -0.2
                },
            }]
      
        }],
          tooltip: {
              headerFormat: "",
              pointFormat: "<b>Financings for {point.name}:</b> {point.value} €"
          }
        });





        const csv = await fetch(
          'website/data/line_series.csv'
      ).then(response => response.text());
    
      // Very simple and case-specific CSV string splitting
      const CSVtoArray = text => text.split(',');
    
      const csvArr = csv.split(/\n/),
          province = {},
          numRegex = /^[0-9\.]+$/,
          lastCommaRegex = /,\s$/,
          quoteRegex = /['"\s]+/g;
          categories = CSVtoArray(csvArr[0]).slice(2);
    
      let provChart;
    
      // Parse the CSV into arrays, one array each prov
      csvArr.slice(1).forEach(function (line) {
          let row = CSVtoArray(line);
          let data = row.slice(2);
          
          
    
          data.forEach(function (val, i) {
              val = val.replace(quoteRegex, '');
              if (numRegex.test(val)) {
                  val = parseInt(val, 10);
              } else if (!val || lastCommaRegex.test(val)) {
                  val = null;
              }
              data[i] = val;
          });
    
          let code = row[1].replace(/\s+/g, '')
    
          province[code] = {
              name: row[0],
              code3: code,
              data: data
          };
    
          
      });
    
      // For each prov, use the latest value for current population
      const data = [];
      for (const code3 in province) {
          if (Object.hasOwnProperty.call(province, code3)) {
              const itemData = province[code3].data;
              let value = null,
                  i = itemData.length,
                  year;
    
              while (i--) {
                  if (typeof itemData[i] === 'number') {
                      value = itemData[i];
                      year = categories[i];
                      break;
                  }
              }
              data.push({
                  name: province[code3].name,
                  code3: code3,
                  value: value,
                  year: year.replace(/\s+/g, '')
              });
          }
      }
     
      // Add lower case codes to the data set for inclusion in the tooltip.pointFormat
      const mapData = Highcharts.geojson(topology);
      mapData.forEach(function (prov) {
          prov.id = prov.properties['hc-key']; // for Chart.get()
      });    
    
      // Wrap point.select to get to the total selected points
      Highcharts.wrap(Highcharts.Point.prototype, 'select', function (proceed) {
    
          proceed.apply(this, Array.prototype.slice.call(arguments, 1));
    
          const points = mapChart.getSelectedPoints();
          if (points.length) {
              if (points.length === 1) {
                  document.querySelector('#info h2').innerHTML = points[0].name;
              } else {
                  document.querySelector('#info h2').innerHTML = 'Comparing province';
    
              }
              document.querySelector('#info .subheader')
                  .innerHTML = '<h4>Funding history</h4><small><em>Shift + Click on map to compare province</em></small>';
    
              if (!provChart) {
                  provChart = Highcharts.chart('province_line_chart', {
                      chart: {
                          height: 250,
                          spacingLeft: 0
                      },
                      credits: {
                          enabled: false
                      },
                      title: {
                          text: null
                      },
                      subtitle: {
                          text: null
                      },
                      xAxis: {
                          tickPixelInterval: 50,
                          crosshair: true
                      },
                      yAxis: {
                          title: null,
                          opposite: true
                      },
                      tooltip: {
                          split: true
                      },
                      plotOptions: {
                          series: {
                              animation: {
                                  duration: 500
                              },
                              marker: {
                                  enabled: false
                              },
                              threshold: 0,
                              pointStart: parseInt(categories[0], 10)
                          }
                      }
                  });
              }
    
              provChart.series.slice(0).forEach(function (s) {
                  s.remove(false);
              });
              points.forEach(function (p) {
                  provChart.addSeries({
                      name: p.name,
                      data: province[p.code3].data,
                      type: points.length > 1 ? 'line' : 'area'
                  }, false);
              });
              provChart.redraw();
    
          } else {
              document.querySelector('#info h2').innerHTML = '';
              document.querySelector('#info .subheader').innerHTML = '';
              if (provChart) {
                  provChart = provChart.destroy();
              }
          }
      });
    
      // Initiate the map chart
      const mapChart = Highcharts.mapChart('finance_map', {
    
          chart: {
              map: topology
          },
    
          title: {
              text: 'Financing distribution in Emilia Romagna in 2021'
          },
    
          mapNavigation: {
              enabled: true,
          },
    
          colorAxis: {
            start: 1,
            min: 0,
            minColor: '#cff0eb',
            maxColor: '#01a189',
            stops: [
                [0, '#cff0eb'],
                [0.5, '#b6ffe9'],
                [0.7, '#03d1b2'],
                [1, '#01a189']
            ]
          },
    
          tooltip: {
              footerFormat: '<span style="font-size: 10px">(Click for details)</span>'
          },
    
          series: [{
              data: data,
              mapData: mapData,
              joinBy: ['postal-code', 'code3'],
              name: 'Financing ammount',
              allowPointSelect: true,
              cursor: 'pointer',
              states: {
                  select: {
                      color: '#9DC7F1',
                      borderColor: 'black',
                      dashStyle: 'shortdot'
                  }
              },
              borderWidth: 0.5
          }]
      });
    
      // Pre-select a prov
      mapChart.get('it-bo').select();
      
  })();
   
});


