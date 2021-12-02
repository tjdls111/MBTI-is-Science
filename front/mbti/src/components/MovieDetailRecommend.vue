<template>
  <div>
    <h3 class="title-text mb-3">Movies similar to this movie.</h3>
    <div v-if="recommendedMovies.length">
      <ul class="recommends">
        <MovieDetailRecommendItem
        v-for="movie in recommendedMovies"
        :key="movie.id"
        :movie="movie"
        >
        </MovieDetailRecommendItem>
      </ul>
    </div>
    <div v-else>
      <div class="pb-5">We are so sorry. There is no movie recommendation for this movie.</div>
    </div>
  </div>
</template>

<script>
import MovieDetailRecommendItem from '@/components/MovieDetailRecommendItem'

import axios from 'axios'
export default {
  name:"MovieDetailRecommend",
  components:{
    MovieDetailRecommendItem

  },
  data:function(){
    return{
      recommendedMovies: [],
    }
  },
  props:{
    movie_pk:String,
  },
  methods:{
    getRecommendList: function(){
      axios({
        method: 'get',
        url: `http://15.165.76.174:80/movies/${this.movie_pk}/movie_recommend/`,
      })
        .then( (res) => {
          // console.log(res.data)
          this.recommendedMovies = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
      
    }
  },
  created: function(){
    this.getRecommendList()
  }

}
</script>
<style>

</style>