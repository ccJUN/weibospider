import echarts from "echarts";

export  default function echartsBar(x,y){
    var app = {},
    option = null;
    var dom = document.getElementById("report-container");
    var myChart = echarts.init(dom);
    app.title = '转发数';
    console.log('x',x)
    console.log('y',y)
    option = {
        color: ['rgb(12, 125, 245)'],
        tooltip : {
            trigger: 'axis',
            axisPointer : {            
                type : 'shadow' 
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis : [
            {
                type : 'category',
                data : x,
                axisTick: {
                    alignWithLabel: true
                }
            }
        ],
        yAxis : [
            {
                type : 'value'
            }
        ],
        series : [
            {
                name:'转发次数',
                type:'bar',
                barWidth: '60%',
                data:y
            }
        ]
    };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
}
