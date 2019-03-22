<template>
  <section class="container">
    <div>
      <h1 class="title">微博路径</h1>
      <div class="echart1">
          <h2 class="subtitle">关系链图谱</h2>
          <div id="container" class="main"></div>
          <div class="echart"></div>
      </div>
      <div class="echart2">
          <h2 class="subtitle">时间图谱</h2>
          <div id="container" class="main">
            <ul>
              <li v-for="index in nextnode" :key="index" class="content">
                  <p class="time">{{index['created_at']}}</p>
                  <p>{{index['text']}}</p>
                  <p>{{index['name']}}</p>
                  <p>粉丝数：{{index['followers_count']}}</p>
                  <p>转发数：{{index['reposts_count']}}</p>
                  <p>评论数：{{index['comments_count']}}</p>
                  <p>点赞数：{{index['attitudes_count']}}</p>
              </li>
            </ul>
          </div>

          <div class="echart"></div>
      </div>
      <div class="影响力图谱">
          <h2 class="subtitle">影响力图谱</h2>
          <div id="container" class="main"></div>
          <div class="echart"></div>
      </div>
    </div>
  </section>
</template>

<script>
import echarts from "echarts";
import jquery from "jquery";
import echartsBar from "../plugins/tree";
import { $ajax } from '../plugins/axios';
import axios from 'axios'
import getApi from '../plugins/getrelation'

export default {
  data() {
    return {
      weibojson: require('~/assets/json/weibo.json'),
      weiboSum:{},
      nextnode:''
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
    this.draw()
    this.time()
  },
  methods: {
      draw: function() {
        const weibojson = this.weibojson
        axios.get('http://127.0.0.1:5000/getRelation').then(function(response){
            var res 
            res = response
            var dom = document.getElementById("container");
            echartsBar(weibojson,dom)
        })
      },
      time:function(){
      },
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
li{
  list-style: none;
  text-align: left
}
.time{
  color: red;
  font-size: 18px;
  margin-top: 15px;
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
  font-size: 50px;
  color: #35495e;
  letter-spacing: 1px;
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
