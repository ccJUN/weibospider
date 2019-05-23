import Highcharts from "highcharts"
export  default function echartsLine(ontainer,ContainerX,containerY){
    var chart = Highcharts.chart('baidu-container', {
        title: {
            text: '收录趋势'
        },
        yAxis: {
            title: {
                text: '收录数'
            }
        },
        xAxis:{
            dateTimeLabelFormats: {
				week: '%Y-%m-%d'
			}
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle'
        },
        plotOptions: {
            series: {
                label: {
                    connectorAllowed: false
                },
            }
        },
        series: [{
            name: '日收录量',
            data: containerY.result
        }],
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                }
            }]
        }
    });
}
