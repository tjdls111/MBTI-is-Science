<template>
  <div>
    <banner></banner>
    <div class="container" style="margin: 4rem;">
      <h1 v-if="this.$route.query.data" class="mb-4">Review Update 🖊</h1>
      <h1 v-else class="mb-4">Review Create 🖊</h1>
      <b-form @submit="CreateArticle">
      <div class="create-form-border">
      <div class="create-form row d-flex align-center">
        <div class="category col-3">
          <p>Select rate</p>
        </div>
        <div class="col-9">
          <b-form-rating 
            id="rating-form"
            class="p-0 ms-auto d-inline align-right text-light "
            v-model="score"  
            value-max="10"
            variant="danger"
            show-value
            show-value-max
            icon-empty="heart"
            icon-half="heart-half"
            icon-full="heart-fill"
            size="sm"
            stars="10"
            aria-required="true"
          ></b-form-rating>
        </div>
        <div class="category col-3">
          <p><label for="title">Review title </label></p>
        </div>
        <div class=" col-9">
          <b-input v-model="title" type="text" name="title" class="review-title my-1"></b-input>
        </div>
        <div class="category col-3">
          <p><label for="movie">Movie title </label></p>
        </div>
        <div class=" col-9">
          <b-form-input v-model="movie" id="movie" list="my-list-id" class="my-1"></b-form-input>
          <datalist id="my-list-id">
            <option v-for="movie in movies" :key="movie.id">{{ movie.id }} : {{ movie.title }} </option>
          </datalist>
        </div>
        <div class="category col-3">
          <p><label for="content">Content </label></p>
        </div>
        <div class="col-9">
          <b-textarea v-model="content" type="text" name="content" class="my-1"> </b-textarea>
        </div>
      </div>
      </div>
        <b-button v-if="this.$route.query.data" type="submit" class="my-5 fw-bold" style="background-color: rgb(42, 90, 65);" >Update Review</b-button>
        <b-button v-else type="submit" class="my-5 fw-bold" style="background-color: rgb(42, 90, 65);" >Create Review</b-button>
      </b-form>
    </div>
  </div>
</template>

<script>
import Banner from '@/components/Banner'
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'ArticleCreate',
  data: function(){
    return {
        title:null,
        movieId: null,
        movie: null,
        score: null,
        content: null,
        article_pk: null,

    }
  },
  components: {
    Banner,
  },
  computed: {
    ...mapState(['movies'])

  },
  created: function(){
    if (this.$route.query.data){
      const origin_article_data = JSON.parse(this.$route.query.data)
      this.title = origin_article_data.title
      this.score = origin_article_data.score
      this.content = origin_article_data.content
      this.movieId = origin_article_data.movieId
      this.movieTitle = origin_article_data.movieTitle
      this.movie = `${this.movieId} : ${this.movieTitle}`
      this.article_pk = origin_article_data.article_pk
      // this.author = 
    }
    
  },
  watch: {
    // selectedMovie: function(){
      
    // }
    // newArticle: function(){
    //   this.$store.dispatch('LoadArticleList')
    // }

  },
  methods: {
    CreateArticle: function(event){
      event.preventDefault()



      // this.movieId = this.movie.splice()
      this.movieId = this.movie.split(':')[0]
      // console.log(this.movieId)

      const articleForm = {
        title:this.title,
        movie: this.movieId,
        content: this.content,
        score: this.score
      }

      if (this.$route.query.data){
        // article 수정
        axios({
          method:'put',
          url:`http://15.165.76.174:80/articles/${this.article_pk}/`,
          data: articleForm,
          headers: {"Authorization":`JWT ${localStorage.getItem('jwt')}`},
        })
          .then(()=>{
            // console.log(res)
            this.$router.push({name: 'ArticleDetail', query:{data: JSON.stringify({ articleId : this.article_pk})}})
          })
          .catch(err =>{
            console.log(err)
          })
      }
      else{
        // article 생성
        axios({
          method:'post',
          url:`http://15.165.76.174:80/articles/`,
          data: articleForm,
          headers: {"Authorization":`JWT ${localStorage.getItem('jwt')}`},
        })
          .then(()=>{       
            this.$router.push({name:'ArticleList'})
  
          })
          .catch(err =>{
            console.log(err)
          })
      }


    }
  }
}
</script>

<style >
.create-form-border{
  background-color: rgb(42, 90, 65);
  padding: 3% 4%;
  border-radius: 10px;
}
.create-form{
  color: white;
  background-color: rgb(42, 90, 65);
  border: 1px solid ;
  padding: 3% 3% 3% 0%;
  border-radius: 10px;
  min-width: 420px;
}
.category{
  border-right: 1px solid ;
  font-weight: 600;
  margin: 1rem 0 1rem 0;
}

</style>