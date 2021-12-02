<template>
<div>
  <banner></banner>
  <div class="container h-100 p-5" style="margin: 6rem; min-height: 500px;">
    <div class="test-logo">Movie MBTI Test Result 🕵️‍♀️</div>
      <h1 class="mb-5">당신의 MBTI는 "{{ mbti | uppercase }}"</h1>
      <p>당신이 영화 캐릭터라면? </p>
      <p>{{results[mbti].character}}</p>
      <p>{{results[mbti].explanation}}</p>
      <p>영화 장르로 {{results[mbti].genre}}를(을) 추천해요~</p>
      
  </div>
</div>
</template>

<script>
import Banner from '@/components/Banner'

export default {
  name: 'MbtiTestResult',
  components: {
    Banner
  },
  data: function(){
    return{
      mbti: null,
      isLogin: false,
      results:{
        'istj' :{
          character :"마블의 가모라, 네뷸라. 킹스맨의 해리, 악마는 프라다를 입는다의 에밀리, 레옹의 레옹",
          explanation:"사실에 근거해서 생각하고, 진지한 모범생 같은 캐릭터예요~~ 주인공, 조력자를 맡는 경우가 많아요.",
          genre:"사극, 전쟁",
        
        },
        'isfj' :{
          character :"하울의 움직이는 성의 소피",
          explanation:"성실하고 온화해요. 협조를 잘해요~ 이 성격이 악역을 맡는 경우는 드물답니다.",
          genre:"사극, 다큐멘터리, 음악",
        
        },
        'infj' :{
          character :"해리포터의 덤블도어, 겨울왕국의 엘사, 나니아 연대기의 아슬란, 센과 치히로의 행방불명의 하쿠",
          explanation:"깊은 통찰력이나 특이한 능력을 가진 캐릭터. 주인공의 조력자 역할을 많이 해요. 주인공일 경우, 깊은 고민을 하기도 하죠.",
          genre:"드라마, 가족",
        
        },
        'intj' :{
          character :"해리포터의 볼드모트, 스네이프. 마블의 타노스, 닥터 스트레인지",
          explanation:"똑똑하고 철저한 계획을 세워요. 사연 있는 악역을 맡는 경우가 많아요.",
          genre:"미스테리, SF, 스릴러",
        
        },
        'istp' :{
          character :"007의 제임스 본드",
          explanation:"논리적이고 재주가 많답니다.",
          genre:"코미디, 사극, 범죄",
        
        },
        'isfp' :{
          character :"해리 포터의 해리 포터, 트와일라잇의 벨라, 레옹의 마틸다",
          explanation:"보통 성장물의 주인공 역할이 많답니다. 따듯하고 겸손해요.",
          genre:"어드벤처, 판타지, 애니메이션",
        
        },
        'infp':{
          character :"인사이드 아웃의 슬픔이, 센과 치히로의 행방불명의 치히로",
          explanation:"상냥해요. 이상적인 세상을 꿈꾸고 만들어가요~",
          genre:"판타지",
        
        },
        'intp' :{
          character :"스타워즈의 요다, 매트릭스의 네오",
          explanation:"새로운 지식을 추구하는 천재, 생각이 깊은 전략가랍니다.",
          genre:"SF 영화, 미스테리",
        
        },
        'estp' :{
          character :"짱구",
          explanation:"모험을 좋아하고, 활발해요. ",
          genre:"액션, 범죄",
        
        },
        'esfp' :{
          character :"헐크, 말레피센트",
          explanation:"자유로운 영혼이에요~ 에너지가 넘치죠. ",
          genre:"어드벤처, 뮤지컬",
        
        },
        'enfp' :{
          character :"알라딘의 지니, 찰리와 초콜릿 공장의 윌리 윌카, 겨울왕국의 안나",
          explanation:"열정이 넘쳐요. 명량하고 밝아요. 로맨틱 코미디의 주인공이 되보시는 건 어떤가요?",
          genre:"어드벤처, 액션",
        
        },
        'entp' :{
          character :"다크 나이트의 조커, 마블의 토니 스타크, 데드풀, 나홀로 집에의 케빈",
          explanation:"상상력이 넘쳐요. 새로운 것을 좋아하고 도전하죠.",
          genre:"코메디, 범죄, 다큐멘터리",
        
        },
        'estj' :{
          character :"해리포터의 헤르미온느",
          explanation:"현실적이고 실용적이에요. 뛰어난 실력이 있는 관리자형!",
          genre:"드라마, 어드벤처, 다큐멘터리 ",
        
        },
        'esfj' :{
          character :"토이 스토리의 우디",
          explanation:"친절하고 현실감각이 뛰어나요.",
          genre:"로맨틱, 뮤지컬",
        
        },
        'enfj' :{
          character :"모아나의 모아나, 인사이드 아웃의 기쁨이, 주토피아의 주디, 매트릭스의 모피어스",
          explanation:"명량하면서도 차분하게, 목표를 향해 나아가요.",
          genre:"로맨틱, 뮤지컬, 드라마",
        
        },
        'entj' :{
          character :"헝거 게임의 게일, 300의 레오니다스 왕",
          explanation:"활발하고 대담해요. 리더인 경우가 많아요. 강한 악역을 맡기도 한답니다.",
          genre:"스릴러, 공포, 범죄",
        
        },
        
      }

    }
  },
  computed: {

  },
  created: function(){
    this.mbti = JSON.parse(this.$route.query.data).mbti
    console.log(JSON.parse(this.$route.query.data))

    // const token = localStorage.getItem('jwt')
    // if (token) {
    //   this.isLogin = true
    // }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>