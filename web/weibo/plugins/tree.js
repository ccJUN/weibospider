import echarts from "echarts";

export  default function echartsBar(data,container){
    console.log(data.data,container)
    var app = {},
        data = data,
        chartDom = container,
        option = null,

    myChart = echarts.init(chartDom);
    echarts.util.each(data.children, function(datum, index) {
      index % 2 === 0 && (datum.collapsed = true);
    });
    
    myChart.setOption(
      ( option = {
        tooltip: {
          trigger: "item",
          triggerOn: "mousemove"
        },
        series: [
          {
            type: "tree",
            data: [data],
            top: "1%",
            left: "7%",
            bottom: "1%",
            right: "20%",
            symbolSize: 11,
            label: {
              normal: {
                position: "left",
                verticalAlign: "middle",
                align: "right",
                fontSize: 14
              }
            },

            leaves: {
              label: {
                normal: {
                  position: "right",
                  verticalAlign: "middle",
                  align: "left"
                }
              }
            },

            expandAndCollapse: true,
            animationDuration: 550,
            animationDurationUpdate: 750
          }
        ]
      })
    );
};
