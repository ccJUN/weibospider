<template>
  <section class="container">
    <div>
      <h1 class="title">微博路径</h1>
      <h2 class="subtitle"></h2>
      <div id="container" class="main"></div>
      <div class="echart"></div>
    </div>
  </section>
</template>

<script>
import echarts from "echarts";
import jquery from "jquery";

export default {
  data() {
    return {
      weibojson: require("assets/json/flare.json")
    };
  },
  components: {
    echarts,
    jquery
  },
  computed: {
  },
  mounted() {
    this.draw()
  },
  methods: {
      draw: function() {
      var app = {};
      let data = this.weibojson;
      var dom = document.getElementById("container");
      var myChart = echarts.init(dom);
      var option = null;
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
      // console.log(this.weibojson)
    }
  }
};
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.main{
  position: relative;
  width: 1000px;
  height: 1000px;
}

.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
