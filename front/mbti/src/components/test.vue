<template>
  <div class="hello">
    <div id='surveyElement'>
      <survey :survey="surveyModel"/> <!-- surveyJS 컴포넌트에 surveyModel을 넣는다 -->
    </div>
  </div>
</template>

<script>
import * as SurveyVue from 'survey-vue' // surveyJS를 import한다
import surveyJSON from '@/assets/survey.json' // 설문조사 JSON 문항을 불러온다

let Survey = SurveyVue.Survey // surveyJS에서 Survey 컴포넌트만 따로 빼낸다

export default {
  name: 'Test',
  components: {
    Survey // SurveyJS 컴포넌트를 사용한다
  },
  methods:{
    calculate_mbti : function(results){
      let i_or_e = 0    
      let n_or_s = 0
      let t_or_f = 0
      let j_or_p = 0

      console.log(i_or_e, n_or_s, t_or_f, j_or_p)
      
      for (let i = 1; i< 13; i++){
        let tmp = results[i]
        
        switch (tmp){
          case "i": 
            i_or_e += 1;
            break;
          case "e": 
            i_or_e --;
            break;
          case "n":
            n_or_s ++
            break
          case "s":
            n_or_s --
            break
          case "t":
            t_or_f ++
            break
          case "f":
            t_or_f --
            break
          case "j":
            j_or_p ++
            break
          case "p":
            j_or_p --
            break
          default:
            console.log(`#{tmp}는 mbti 유형 요소가 아닙니다.`)
          }
        }
        
      console.log(i_or_e, n_or_s, t_or_f, j_or_p)
      let mbti = ""
      if (i_or_e > 0){
        mbti = mbti + "i"
      }
      else{
        mbti = mbti + "e"
      }

      if (n_or_s > 0){
        mbti = mbti + "n"
      }
      else{
        mbti = mbti + "s"
      }

      if (t_or_f > 0){
        mbti = mbti + "t"
      }
      else{
        mbti = mbti + "f"
      }

      if (j_or_p > 0){
        mbti = mbti + "j"
      }
      else{
        mbti = mbti + "p"
      }
      console.log(mbti)      
    }
  },
  computed: {
    surveyModel () { 
      let surveyModel = new SurveyVue.Model(surveyJSON) // 설문조사 JSON 문항을 model로 넣는다
      surveyModel.onComplete.add(function (result) { // Complete 버튼을 누르면 실행할 콜백 함수를 넣는다
        // alert(`result: ${JSON.stringify(result.data)}`)
        const results = JSON.stringify(result.data)
        console.log(results) 
        this.calculate_mbti(results)
      })
      return surveyModel
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>