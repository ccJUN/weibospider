// import echarts from "echarts";

// function echartsBar(data,container){
//     var app = {};
//     let data = data;
//     var dom = container;
//     var myChart = echarts.init(dom);
//     var option = null;
//     echarts.util.each(data.children, function(datum, index) {
//       index % 2 === 0 && (datum.collapsed = true);
//     });
//     myChart.setOption(
//       ( option = {
//         tooltip: {
//           trigger: "item",
//           triggerOn: "mousemove"
//         },
//         series: [
//           {
//             type: "tree",
//             data: [data],
//             top: "1%",
//             left: "7%",
//             bottom: "1%",
//             right: "20%",

//             symbolSize: 11,

//             label: {
//               normal: {
//                 position: "left",
//                 verticalAlign: "middle",
//                 align: "right",
//                 fontSize: 14
//               }
//             },

//             leaves: {
//               label: {
//                 normal: {
//                   position: "right",
//                   verticalAlign: "middle",
//                   align: "left"
//                 }
//               }
//             },

//             expandAndCollapse: true,
//             animationDuration: 550,
//             animationDurationUpdate: 750
//           }
//         ]
//       })
//     );
// };
// export echartsBar = echartsBar;