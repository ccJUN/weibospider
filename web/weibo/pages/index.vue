<template>
   <section class="container">
    <header>
      <h1>效果监控</h1>
    </header>
    <div class="tabs">
      <ul class="link">
        <li
          v-for="(index,value) in listenTab" 
          :class="[index.name==currentname&&'active']"
          @click="exchange(index.name,index.web)"
          >{{index.name}}</li>
      </ul>
      <button>+添加网站监控</button>
    </div>
    <div class="datalist-list">
      <ul>
        <li>
          <div class="header">
            <span class="site-name">百度</span>
          </div>
          <div class="body">
            <div class="data-info-wrap">
              <div class="rank">
                <p>{{baidupc[currentIndex].rank}}</p>
                <p class="sub-text">受宠排名</p>
              </div>
              <div class="other-rank">
                <div class="row">
                  <p>{{baidupc[currentIndex].weight}}</p>
                  <p class="sub-text">网站权重</p>
                </div>
              </div>
               <div class="ip">
                  <p>{{baidupc[currentIndex].ip}}<span class="sub-ip">IP</span></p>
                  <p class="sub-text">预计百度来源</p>
                </div>
            </div>
            <div class="ehcart2" id="baidu-container">
            </div>
            <div class="ehcart3" id="rank-container">
            </div>
          </div>
        </li>
        <li>
          <div class="header">
            <span class="site-name">百度移动</span>
          </div>
          <div class="body">
            <div class="data-info-wrap">
              <div class="rank">
                <p>{{baidum[currentIndex].rank}}</p>
                <p class="sub-text">受宠排名</p>
              </div>
              <div class="other-rank">
                <div class="row">
                  <p>{{baidum[currentIndex].weight}}</p>
                  <p class="sub-text">网站权重</p>
                </div>
              </div>
               <div class="ip">
                  <p>{{baidum[currentIndex].ip}}<span>IP</span></p>
                  <p class="sub-text">预计百度移动来源</p>
                </div>
                <div class="ehcart2" id="baidu-container2"></div>
                <div class="ehcart3" id="rank-container2"></div>
            </div>
          </div>
        </li>
        <li>
          <div class="header">
            <span class="site-name">360so</span>
          </div>
          <div class="body">
            <div class="data-info-wrap">
              <div class="rank">
                <p>{{so[currentIndex].rank}}</p>
                <p class="sub-text">受宠排名</p>
              </div>
              <div class="other-rank">
                <div class="row">
                  <p>{{so[currentIndex].weight}}</p>
                  <p class="sub-text">网站权重</p>
                </div>
              </div>
               <div class="ip">
                  <p>{{so[currentIndex].ip}}<span>IP</span></p>
                  <p class="sub-text">预计so来源</p>
                </div>
                <div class="ehcart2" id="shoulv-container"></div>
                <div class="ehcart3" id="rank-container"></div>
            </div>
          </div>
        </li>
        <li>
          <div class="header">
            <span class="site-name">搜狗</span>
          </div>
          <div class="body">
            <div class="data-info-wrap">
              <div class="rank">
                <p>-</p>
                <p class="sub-text">受宠排名</p>
              </div>
              <div class="other-rank">
                <div class="row">
                  <p>{{sogou[currentIndex].weight}}</p>
                  <p class="sub-text">网站权重</p>
                </div>
              </div>
               <div class="ip">
                  <p>{{sogou[currentIndex].ip}}<span>IP</span></p>
                  <p class="sub-text">预计搜狗来源</p>
                </div>
                <div class="ehcart2" id="report-container"></div>
                <div class="ehcart3"></div>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<style lang="scss" scoped src="~/assets/scss/index.scss"></style>
<style lang="scss" scoped src="~/assets/scss/echart.scss"></style>
<script>
import jquery from "jquery";
import echartsTree from "../plugins/tree";
import axios from 'axios'
import getApi from '../plugins/getrelation'
import echartsBar from "../plugins/bar"
import echartsLine from "../plugins/line"
import echartsLine2 from "../plugins/baidum"
import echartsLine3 from "../plugins/baidum2"

export default {
  data() {
    return {
      relativeJson: require('~/assets/json/weibo.json'),
      weibotimeline:[],
      reports:[],
      reportsSum:0,
      listenTab: [],
      currentname: '波洞',
      currentweb:'boodo.qq.com',
      currentIndex:0,
      baidupc: [
        {
          rank:'903,294',
          weight:1,
          ip:'144~168'
        },
        {
          rank:'654',
          weight:4,
          ip:'38,221~60,228'
        },
        {
          rank:'18,015',
          weight:6,
          ip:'23,509~28,410'
        }
      ],
      baidum:[
        {
          rank:'170,846',
          weight:1,
          ip:'271 ~ 301'
        },
        {
          rank:'640',
          weight:'5',
          ip:'25,223 ~ 38,506'
        },
        {
          rank:'20,681',
          weight:6,
          ip:'15,084 ~ 18,085'
        }
      ],
      so:[
        {
          rank:'528,712',
          weight:1,
          ip:'86~100'
        },
        {
          rank:'13,642',
          weight:5,
          ip:'22,932~36,136'
        },
        {
          rank:'10,874',
          weight:6,
          ip:'14,105~17,046'
        }
      ],
      sogou:[
        {
          rank:'暂无',
          weight:1,
          ip:'5~67'
        },
        {
          rank:'640',
          weight:'5',
          ip:'15288~24091'
        },
        {
          rank:'18015',
          weight:6,
          ip:'9403~11364'
        }
      ]
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
    this.getRecord();
    this.getIp();
    this.getWebsites();
    this.getListen();
    this.getTop();
    echartsLine2('baidu-container2');
    echartsLine3();
  },
  methods: {
      getListen:function(){
        self = this;
        axios.get('http://127.0.0.1:5000/getlisten').then(function(response){
          let data = response.data;
          let arr = data.split('),')
          arr.forEach(i => {
            let listenjson = {}
            listenjson.web = i.split(',')[0];
            name = i.split(',')[1];
            name = decodeURI(name).substr(2, name.length-3);
            listenjson.name = name
            self.listenTab.push(listenjson)
          });
        })
      },
      getRecord:function(){
        axios.get('http://127.0.0.1:5000/getrecord').then(function(response){
        })
      },
      //修改编码 
      decodeUnicode:function(str) {
          str = str.replace(/\\/g, "%");
          return unescape(str);
      },

      // 
      getIp: function() {
        axios.get('http://127.0.0.1:5000/getip').then(function(response){
            var res = response
            var dom = document.getElementById("container");
            echartsBar();
        })
      },

      //获取次数
      getWebsites:function(){
          var self = this;
          let selectweb = this.currentweb;
          axios.get('http://127.0.0.1:5000/getwebsites',{
            params: {
              web: selectweb
            }
          }).then(function(response){
            console.log(response.data)
            var containerY = response.data
            echartsLine('baidu-container','',containerY);
          })
      },
      //获取次数
      getTop:function(){
          var self = this;
          let selectweb = this.currentweb;
          axios.get('http://127.0.0.1:5000/gettop',{
            params: {
              web: selectweb
            }
          }).then(function(response){
            console.log(response.data)
            var containerY = response.data.result;
            echartsBar('rank-container','',containerY);
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
      },
      exchange: function(name,web){
        this.currentname = name;
        this.currentweb = web.split('(')[1].substr(1,web.length-3);
        console.log(this.currentweb)
        if(this.currentweb=='boodo.qq.com'){
          this.currentIndex = 0;
        }
        if(this.currentweb=='kuaibao.qq.com'){
          this.currentIndex = 1;
        }
        if(this.currentweb=='browser.qq.com'){
          this.currentIndex = 2;
        }
        this.getTop()
        this.getWebsites()
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
