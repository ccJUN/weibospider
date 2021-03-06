import Highcharts from "highcharts"
export  default function echartsBar(container,ContainerX,containerY){
    console.log(containerY)
    var chart = Highcharts.chart(container, {
        title: {
            text: '关键词排名趋势'
        },
        yAxis: {
            title: {
                text: '排名数'
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
            {name:"Top100",data:containerY.Top100},
            {name:"Top50",data:containerY.Top50},
            {name:"Top20",data:containerY.Top20},
            {name:"Top10",data:containerY.Top10},
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
