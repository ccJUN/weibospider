<template>
  <section class="container">
      <div class="search">
        <input placeholder="输入搜索热点" value="" name="words">
        <button class="ui-btn" @click="startScrapy">热点分析</button>
      </div>
      <p class="tips">微博热点抓取分析需要1个小时</p>
    <div class="report-content">
      <div class="report-title">
          <h1 class="title">啥是佩奇 微博热点路径分析</h1>
          <p class="source"></p>
      </div>
      <div class="data-list">
        <div class="new-big-title"><span>转发影响</span></div>
        <div class="float small-title">
          <p>啥是佩奇，总转发<span>{{reportsSum}}</span>次数</p>
        </div>
        <div class="echart-main float">
          <div id="report-container" class="main"></div>
        </div>
      </div>
      <div class="report-line"></div>
      <div class="data-list">
          <div class="new-big-title"><span>时间图谱</span></div>
          <div>
            <h2 class="subtitle">时间图谱</h2>
          </div>
          <div id="container" class="weibo-main">
            <ul>
              <li v-for="index in weibotimeline" :key="index" class="weibo-content">
                  <p class="weibo-time">{{index.time}}</p>
                  <div class="line"></div>
                  <div class="weibo-panel">
                    <p class="weibo-anchor">{{index.anchor}}</p>
                    <p class="weibo-reports">{{index.reports}}</p>
                  </div>
              </li>
            </ul>
          </div>
          <div class="echart"></div>
      </div>
      <div class="report-line"></div>
      <div class="data-list">
          <div class="new-big-title"><span>关系链图谱</span></div>
          <h2 class="subtitle"></h2>
          <div id="container" class="main"></div>
          <div class="echart"></div>
      </div>
      <div class="report-line"></div>
      <div class="data-list">
          <div class="new-big-title"><span>媒体类型</span></div>
          <h2 class="subtitle"></h2>
          <div id="container" class="main"></div>
          <div class="echart"></div>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped src="~/assets/scss/index.scss"></style>
<script>
import echarts from "echarts";
import jquery from "jquery";
import echartsTree from "../plugins/tree";
import axios from 'axios'
import getApi from '../plugins/getrelation'
import echartBar from "../plugins/bar"
export default {
  data() {
    return {
      relativeJson: require('~/assets/json/weibo.json'),
      weibotimeline:[],
      reports:[],
      reportsSum:0,

    };
  },
  beforeCreate(){
  },
  components: {
    echarts,
    jquery
  },
  computed: {
  },
  mounted() {
    this.getReport();
    this.getSum();
    this.getTime();
  },
  methods: {
      // 开始抓取数据
      startScrapy:function(){
        axios.get('http://127.0.0.1:5000/scrapy',{
          params:{
            words:jquery("input[name=words]").val()
        }}).then(function(response){

        })
      },

      //修改编码 
      decodeUnicode:function(str) {
          str = str.replace(/\\/g, "%");
          return unescape(str);
      },

      // 
      draw: function() {
        axios.get('http://127.0.0.1:5000/getRelation',{
        params:{
          words:jquery("input[name=words]").val()
        }}).then(function(response){
            var res = response
            var dom = document.getElementById("container");
            // echartsBar(weibojson,dom);
        })
      },

      //获取次数
      getReport:function(){
          var self = this;
          axios.get('http://127.0.0.1:5000/gethotrepeat').then(function(response){
            let data = response.data.split('),');
            let anchor = [];
            let report = [];
            for(var i = 0;i<data.length;i++){
              let tem = {};
              anchor.push(self.decodeUnicode(data[i].split('(')[1].split(', u')[1].split(',')[0]));
              report.push(data[i].split('(')[1].split(',')[2]);
            }
            echartBar(anchor,report)
          })
      },

      //获取转发总次数
      getSum:function(){
          var self = this;
          axios.get('http://127.0.0.1:5000/getSum').then((response)=>{
              this.reportsSum = response.data.split('(\'')[1].split('\')')[0];
          })
      },

      //获取时间
      getTime:function(){
          axios.get('http://127.0.0.1:5000/getTime').then((response)=>{
            let data = response.data.split('),');
            for(var i =0;i<data.length;i++){
              let timeline = {};
              timeline.reports = data[i].split(', u')[1].split(',')[1];
              timeline.anchor = this.decodeUnicode(data[i].split(', u')[1].split(',')[0]);
              timeline.time = new Date(parseInt(data[i].split(', u')[2].replace(/\'/g,''))*1000)
              this.weibotimeline.push(timeline)
            }
            console.log(this.weibotimeline)
              // this.reportsSum = response.data.split('(\'')[1].split('\')')[0];
          })
      }
  }
};
</script>

<style>
li{
  list-style: none;
  text-align: left
}
.time{
  color: #888899;
  font-size: 14px;
  margin-top: 5px;
}
.main{
  position: relative;
  margin-top: 80px;
  width: 730px;
  height: 420px;
}



.subtitle {
  font-weight: 300;
  font-size: 32px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
