!function($) {
    "use strict";

    var Dashboard = function() {};

    //creates Stacked chart
    Dashboard.prototype.createChart  = function(element, data, xkey, ykeys, labels, lineColors) {
        Morris.Bar({
            element: element,
            data: data,
            xkey: xkey,
            ykeys: ykeys,
            labels: labels,
            hideHover: 'auto',
            barSizeRatio: 0.4,
            resize: true, //defaulted to true
            gridLineColor: '#eeeeee',
            barColors: lineColors
        });
    },

    Dashboard.prototype.init = function() {

        //creating Stacked chart
        var $data  = [
            { y: '10 Jul', a: 5 },
            { y: '11 Jul', a: 1 },
            { y: '12 Jul', a: 0 },
            { y: '13 Jul', a: 2 },
            { y: '14 Jul', a: 2 },
            { y: '15 Jul', a: 0 },
            { y: '16 Jul', a: 0 },
            { y: '17 Jul', a: 5 },
            { y: '18 Jul', a: 0 },
            { y: '19 Jul', a: 7 },
            { y: '20 Jul', a: 1 },
        ];
        this.createChart('morris-bar-stacked', $data, 'y', 'a', ['Commits'], ['#3db9dc']);
    },
    //init
    $.Dashboard = new Dashboard, $.Dashboard.Constructor = Dashboard
}(window.jQuery),

//initializing
function($) {
    "use strict";
    $.Dashboard.init();
}(window.jQuery);
