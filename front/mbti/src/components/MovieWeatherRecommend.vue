<template>
  <div>
    <div class="d-flex justify-content-between align-items-center mt-5">
      <h1 class="fw-bold" style="margin-left: 6%; font-weight:500;">🌦 Today's Movie</h1>
      <b-dropdown text="Regions" variant="*" id="movie-dropdown-btn" class="me-5">
          <b-dropdown-item @click="getRecommendListBy(2)">Gumi</b-dropdown-item>
          <b-dropdown-item @click="getRecommendListBy(0)">Seoul</b-dropdown-item>
          <b-dropdown-item @click="getRecommendListBy(1)">Buolkyung</b-dropdown-item>
          <b-dropdown-item @click="getRecommendListBy(3)">Gwangju</b-dropdown-item>
          <b-dropdown-item @click="getRecommendListBy(4)">Daejeon</b-dropdown-item>
      </b-dropdown>
    </div>
    <h5 class="sub-title">
      {{weather_messages[weathers[0]]}}
      <br>
      {{weather_messages[weathers[1]]}}
    </h5>

    <ul class="recommends">
        <movie-weather-recommend-list
          v-for="movies in recommendedMovies"
            :key="movies.id" 
            :movies="movies"
        >
        </movie-weather-recommend-list>
    </ul>
    <hr class="mx-4">
  </div>
</template>

<script>
import MovieWeatherRecommendList from '@/components/MovieWeatherRecommendList'
import axios from 'axios'

export default {
  name: 'MovieWeatherRecommend',
  components: {
    MovieWeatherRecommendList
  },
  data: function(){
    return {
      recommendedMovies: [],
      weathers: [],
      weather_messages : {
        'rain':"☂️ A 'Scary movie' on a dark and rainy day.",
        'snowy':"☃️ A 'Cozy movie' under a blanket on a snowy day.",
        'sunny':"☀️ Let's go on an 'Adventure' on a sunny day!",
        'cold':"🌬 A warm movie with your 'family movie' on a cold day.",
        'warm':"🌸 How about an 'Drama' on a warm day?",
        'hot':"🔥On a hot day, let's chase away the heat by watching a 'Chilling movie'.",
      }
    }
  },
  methods: {
    getRecommendList: function(){
      axios({
        method: 'get',
        url: `https://mbti.link/movies/today_recommend/`,
      })
        .then( (res) => {
          // console.log(res.data)
          const tmp  = res.data
          this.recommendedMovies = tmp
          
          for (let i = 0; i < 2; i++) {
            this.weathers.push(tmp[i].weather)   
          }

        })
        .catch((err)=>{
          console.log(err)
        })
    },
    getRecommendListBy: function(area_num){
      axios({
        method: 'get',
        url: `https://mbti.link/movies/${area_num}/today_recommend/`,
      })
        .then( (res) => {
          // console.log(res.data)
          const tmp  = res.data
          this.recommendedMovies = tmp
          
          for (let i = 0; i < 2; i++) {
            this.weathers.push(tmp[i].weather)   
          }

        })
        .catch((err)=>{
          console.log(err)
        })
    },
  },
  created: function () {
    this.getRecommendList()
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


</style>