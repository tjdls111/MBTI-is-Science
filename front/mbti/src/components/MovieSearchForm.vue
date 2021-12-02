<template>
  <div class="search-form d-flex justify-content-end m-4 py-4">
    <form @submit="search_movie">
      <b-input 
        style="width: 22rem;"
        class ="search_input d-inline"
        type="search" 
        v-model="search"
        placeholder = "Enter the movie keyword you want to find."
        @keyup.enter="search_movie"></b-input>
    </form>
      <b-button size="sm" class="search-btn ms-2" style="background-color: rgb(42, 90, 65); min-width: 82.41px;">Search <b-icon class="fs-6" icon="briefcase-fill" ></b-icon></b-button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MovieSearchForm',

  data: function(){
    return {
      search: null,

    }
  },

  methods:{
    search_movie: function(event){
      event.preventDefault()

      axios({
        method: 'get',
        url: `https://mbti.link/movies/${this.search.trim()}/search/`,

      })
        .then( (res) => {
          console.log(res)
          this.$store.dispatch("searchMovies", res.data)
          this.$router.push({name:'MovieSearchList'})
          
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>