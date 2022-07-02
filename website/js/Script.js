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
});
