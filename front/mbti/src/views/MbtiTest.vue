<template>
<div>
  <banner></banner>
  <div class="container h-100 p-2" style="margin: 15%; max-width: 100%;">
    <div class="test-logo">Movie MBTI Test 🕵️‍♀️</div>
    <div id='surveyElement'>
      <survey :survey="surveyModel"></survey>
    </div>
  </div>
</div>
</template>

<script>
import * as SurveyVue from 'survey-vue' // surveyJS를 import한다
import surveyJSON from '@/assets/survey.json' // 설문조사 JSON 문항을 불러온다
import Banner from '@/components/Banner'
import axios from 'axios'
let Survey = SurveyVue.Survey // surveyJS에서 Survey 컴포넌트만 따로 빼낸다

export default {
  name: 'MbtiTest',
  components: {
    Survey, // SurveyJS 컴포넌트를 사용한다
    Banner,
  },
  
  data: function(){
    return{
      results: null,
      mbti: "",
    }
  },
  methods:{
    calculate_mbti : function(results){
      let i_or_e = 0    
      let n_or_s = 0
      let t_or_f = 0
      let j_or_p = 0

      // console.log(i_or_e, n_or_s, t_or_f, j_or_p)
      // console.log(results);
      
      for (let i = 1; i< 100; i++){
        
          let tmp = results[i]

          // console.log(tmp);

          switch (tmp){
            case "i": 
              i_or_e += 1;
              break;
            case "e": 
              i_or_e -= 1;
              break;
            case "n":
              n_or_s += 1;
              break;
            case "s":
              n_or_s -= 1;
              break;
            case "t":
              t_or_f += 1;
              break;
            case "f":
              t_or_f -= 1;
              break;
            case "j":
              j_or_p +=1;
              break;
            case "p":
              j_or_p -=1;
              break;

            }
          }
        
          
      // console.log(i_or_e, n_or_s, t_or_f, j_or_p)
      if (i_or_e > 0){
        this.mbti += "i"
      }
      else{
        this.mbti += "e"
      }

      if (n_or_s > 0){
        this.mbti += "n"
      }
      else{
        this.mbti += "s"
      }

      if (t_or_f > 0){
        this.mbti += "t"
      }
      else{
        this.mbti += "f"
      }

      if (j_or_p > 0){
        this.mbti += "j"
      }
      else{
        this.mbti += "p"
      }
      // 로그인했으면, 여기에서 user mbti 도 바꿔주기!!!
      if (localStorage.getItem('jwt')){
        axios({
          method:'post',
          url:'http://15.165.76.174:80/accounts/mbti_change/',
          headers: {"Authorization":`JWT ${localStorage.getItem('jwt')}`},
          data: {"mbti":this.mbti.toUpperCase()}
        })
          .then((res)=>{
            console.log(res)
            
          })
          .catch(err=>{
            console.log(err)
          })
        }
    
      this.$router.push({name: 'MbtiTestResult', query: {data: JSON.stringify({mbti: this.mbti})}})
    },
    onCompleteHandler : function(result){
      this.results = JSON.stringify(result.data)
      this.calculate_mbti(this.results)
      
    }
  },

  computed: {
    surveyModel () { 
      let surveyModel = new SurveyVue.Model(surveyJSON)
      surveyModel.onComplete.add(this.onCompleteHandler)
      return surveyModel
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .test-logo {
    color: rgb(42, 90, 65);
    font-weight: 600;
    border: 2px dashed ;
    padding: 4px;
    position: fixed;
    top: 5rem;
    background-color: #eeeeee;
    z-index: 1000;
    border-radius: 5px;
  }
#surveyElement {
  /* max-width: 800px; */
  margin: 1rem;
  padding: 8%;
  border: 1px solid;
  color: white;
  background-color: rgb(42, 90, 65);
  border-radius: 10px;
  text-align: left;
  width: 70%;
}
div.sv_nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
input[type="button" i] {
  color: rgb(42, 90, 65);
  background-color: white;
  padding: 1% 3%;
  min-width: 90px;
  border: none;
  border-radius: 3px;
  margin-left: 4px;
  font-weight: 500;
}
input[type="radio" i] :checked{
  color: rgb(42, 90, 65);
}
#surveyElement > * h5 {
  margin: auto auto 2rem auto;
  padding-bottom: 10px;
  border-bottom: 1px solid white;
  font-size: 19px;
}
.sv_p_root {
  margin: 10%;
  padding: 0px;
}
.sv_qstn .sv-q-col-1 {
  color: rgb(42, 90, 65);
  transition: 0.2s all ease;
  background-color: white;
  border-radius: 5px;
  margin: 2% auto;
  padding: 2% 3%;
}
.sv_q_required_text {
  display: none;
}
.sv_qstn .sv-q-col-1:hover {
  background-color: #fde6bc;
  border-radius: 5px;
  margin: 2% auto;
  padding: 2% 3%;
  font-size: 17px;
}
</style>