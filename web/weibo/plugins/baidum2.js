import Highcharts from "highcharts"
export  default function echartsLine2(container,ContainerX,containerY){
    var chart = Highcharts.chart('baidu-container2', {
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
        series: [
            {name:"收录数",data:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1580,1580,1580,1580,1990,1990,1990]}
        ],
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
