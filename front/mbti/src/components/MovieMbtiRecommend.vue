<template>
  <div>
    <h1 class="title-text title-text-margin mt-5">🎁 Movie For "{{ userMbti }}"</h1>
    <h5 class="sub-title">{{recommendedMoviesExplain[userMbti]}}</h5>
    <div>
      <ul class="recommends">
        <movie-mbti-recommend-item
          v-for="movie in recommendedMovies"
            :key="movie.id"
            :movie="movie"
        >
        </movie-mbti-recommend-item>
      </ul>
    </div>
    <hr class="mx-4">
  </div>
</template>

<script>
import MovieMbtiRecommendItem from '@/components/MovieMbtiRecommendItem'
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'MovieMbtiRecommend',
  components: {
    MovieMbtiRecommendItem,
  },
  computed: {
    ...mapState(['username', 'userMbti'])
  },
  data: function(){
    return {
      recommendedMovies: [],
      recommendedMoviesExplain:{
        'ENTJ':"I recommend thriller and horror movies for you, the leader type, ENTJ!",
        'ENTP':"For ENTP, the debater type, I recommend black comedy and documentary that capture reality.",
        'ENFJ':"I recommend a romantic comedy for you who value warm and relationships.",
        'ENFP':"You are a creative and passionate free soul. I recommend adventure movies for you.",
        'ESTJ':"You are realistic and have leadership. I recommend a court drama to you.",
        'ESTP':"You enjoy adventures. What do you think about action movies?",
        'ESFJ':"You are Sociable and kind. What do you think of a romance movie?",
        'ESFP':"You're sociable and energetic. What do you think about the musical movie?",
        'INTJ':"You're logical and have a lot of thoughts. I recommend a mystery and documentary movie to you.",
        'INTP':"You, the idea bank. I recommend science movies for you!",
        'INFJ':"You are insightful and like to imagine. I recommend dramas and fantasy to you.",
        'INFP':"You are full of passion and sensitivity. I recommend a fantasy movie to you. Let's go to the world of dreams and adventures.",
        'ISTJ':"You're logical and responsible. What do you think about historical movies?",
        'ISTP':"You're cool-headed and curious. What do you think about social satire movies?",
        'ISFJ':"You are brave and altruistic. I recommend animations, adventure and fantasy movies for you!",
        'ISFP':"You are curious and artistic. I recommend animation, family and adventure movie for you.",
        'IDKW':"Try the Mbti test and get a movie recommendation that suits you!",
      },
      // userMbti: null,
    }
  },
  methods: {
    getRecommendList: function(){
      axios({
        method: 'get',
        url: `https://mbti.link/movies/${this.userMbti}/mbti_recommend/`,
      })
        .then( (res) => {
          // console.log(res.data)
          this.recommendedMovies = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    get_mbti: function (){
      this.$store.dispatch('getMbti')
      
      this.getRecommendList()
    }
  },

  created: function () {
    this.get_mbti()
    
  },
  
}
</script>

<style>

.recommends {
  display: flex;
  justify-content: flex-start;
  white-space: nowrap;
  overflow: scroll;
  height: 20rem;
  align-items: center;
}
.sub-title {
  color: gray;
  margin-left: 7%;
  margin-bottom: 30px;
  text-align: left;
}

</style>