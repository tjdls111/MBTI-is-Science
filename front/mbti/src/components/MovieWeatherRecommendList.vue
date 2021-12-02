<template>
<div class="recommend-list">
  <!-- <ul class="recommends"> -->
    <movie-weather-recommend-item
      v-for="movie in movies.data"
        :key="movie.id"
        :movie="movie"
    ></movie-weather-recommend-item>
  <!-- </ul> -->
</div>
</template>

<script>
// import axios from 'axios'
import MovieWeatherRecommendItem from '@/components/MovieWeatherRecommendItem'

export default {
  name: 'MovieWeatherRecommendList',
  components: {
    MovieWeatherRecommendItem
  },
  props:{
    movies: Object,
  },
  data: function () {
    return {
      weather: this.movies.id
    }
  }
  
}
</script>

<style>
.recommend-list {
  display: flex;
}
</style>