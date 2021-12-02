<template>
  <div class="search-form d-flex justify-content-end my-2">
    <form @submit="search_movie">
      <b-input
        style="width: 23rem;"
        class ="search_input d-inline"
        type="text"
        placeholder="Enter the article keyword you want to find." 
        v-model="search" @keyup.enter="search_movie"></b-input>
    </form>
    <b-button class="search-btn ms-2" size="sm" style="background-color: rgb(42, 90, 65);">Search <b-icon class="fs-6" icon="search" ></b-icon></b-button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ArticleSearchForm',

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
        url: `http://15.165.76.174:80/articles/${this.search.trim()}/search/`,

      })
        .then( (res) => {
          // console.log(res)
          this.$store.dispatch("searchArticles", res.data)
          this.$router.push({name:'ArticleSearchList'})
          
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  }
}
</script>

<style>

  .search_input{
    border: 2px solid rgb(42, 90, 65);
    border-radius: 4px;
    transition: width 0.4s ease-in-out;
    
  }
  .search_input:focus{
    background-color: rgb(253, 230, 188);
  }
  .search-btn {
    background-color: rgb(42, 90, 65);
  }
</style>