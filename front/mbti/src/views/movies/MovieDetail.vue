<template>
  <div>
    <banner></banner>
    <div class="container" style="margin: 6rem;">
      <div class="row">
        <div class="col-4">
          <img id="movie-img" :src="`https://image.tmdb.org/t/p/w500/${moviesDetail.poster_path}`">
        </div>
        <div class="col-8 d-flex flex-column me-auto">
          <h1 class="title fw-bold">{{ moviesDetail.title }}
          <span>({{ moviesDetail.release_date | shorter}})</span></h1>
          <div class="genre-list">
            <div class="genres" v-for="genre in setGenres" :key="genre.id"> {{ genre.name }} |</div>
          </div>
          <div class="heart h3">
            <span v-if ="is_pick === 'false'">
              <b-icon icon="heart" size="lg" class="text-danger" animation="cylon-vertical" @click="pick"></b-icon>
            </span>
            <span v-else>
              <b-icon icon="heart-fill" class="text-danger" animation="throb" @click="pick"></b-icon>
            </span>

            <span class="text-danger fs-6 fw-bold">  = {{ picks_cnt + moviesDetail.vote_count }}</span>
          </div>
          
          <b-form-rating 
            id="rating-form"
            v-model="moviesDetail.vote_average" 
            variant="danger" 
            value-max="10"
            readonly
            inline
            show-value
            show-value-max
            icon-empty="heart"
            icon-half="heart-half"
            icon-full="heart-fill"
            size="sm"
            stars="10"
            no-border
          ></b-form-rating>
          <div class="overview">
            {{ moviesDetail.overview}}
          </div>
        </div>
      </div>
      <hr>
      <div v-show="actors" class="row">
        <h3 class="title-text mb-3">Actors</h3>
        <ul class="recommends" style="height: 15rem; margin: 0;">
          <movie-actor-list
            v-for="actor in actors"
            :key="actor.id"
            :actor="actor"
          
          ></movie-actor-list>
        </ul>
      </div>
      <div v-show="reviews.length" class="row review-list">
        <hr>
        <h3 class="title-text mb-3">Reviews</h3>
        <div v-if="isLogin">
          <div id="create-btn" ><b-button class="mb-4" size="sm" variant="outline-danger" :to="{name: 'ArticleCreate'}" >I'll write a post, too. <b-icon class="fs-6 ms-1" icon="pencil-fill" ></b-icon></b-button></div>
        </div>
        <ul class="review-list">
          <movie-review-list
            v-for="review in reviews"
              :key="review.id"
              :review="review"
              :reviewAvatar="review.avatar_path.toString()"
          ></movie-review-list>
        </ul>
      </div>
      <div v-if = "reviews.length">
      </div>
      <div v-else>
        <hr>
        <h3 class="title-text mb-3">Reviews</h3>
        <p> There are no posts. </p>
        <div v-if="isLogin">  
          <div id="create-btn" ><b-button class="mb-4" size="sm" variant="outline-danger" :to="{name: 'ArticleCreate'}" >I'll write a first post!! <b-icon class="fs-6 ms-1" icon="pencil-fill" ></b-icon></b-button></div>
        </div>
      </div>

      <div>
        <MovieDetailRecommend 
        :movie_pk="movieId">
        </MovieDetailRecommend>
      </div>

    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios'
import Banner from '@/components/Banner'
import MovieActorList from '@/components/MovieActorList'
import MovieReviewList from '@/components/MovieReviewList'
import MovieDetailRecommend from '@/components/MovieDetailRecommend'

export default {
  name: 'MovieDtail',
  components: {
    Banner,
    MovieActorList,
    MovieReviewList,
    MovieDetailRecommend,
  },
  data: function(){
    return {
      is_pick: null,
      picks_cnt: null,
      genres : [],
      actors: [],
      reviews: [],
      movieId: null,
      isLogin: false,
      avatar_path : null,
    }
  },
  mounted() {
    // console.log(JSON.parse(this.$route.query.data).movieId)
    this.movieId = JSON.parse(this.$route.query.data).movieId
  },
  computed: {
    ...mapState(['moviesDetail', 'username']),
    // 장르 배열에 넣는 변수
    setGenres: function(){
      return this.moviesDetail.genres
    }
  },
  created: function () {
    // 로그인 여부 확인
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }

    // movieId 가져오기
    this.movieId = JSON.parse(this.$route.query.data).movieId
    // 디테일 요소 가져오기
    this.$store.dispatch('LoadMovieDetailList', this.movieId)
    // Pick 가져오기
    axios({
      method:'get',
      url:`https://mbti.link/movies/${this.movieId}/is_pick/`,
      headers: this.$store.state.config
    })
      .then(res=>{
        // console.log(res.data)
        this.is_pick = res.data.is_pick
        this.picks_cnt = res.data.picks_cnt
      })
      .catch(err=>{
        console.log(err);
      })

      // Actors 가져오기
    axios({
      method:'get',
      url:`https://mbti.link/movies/${this.movieId}/actors/`,
      // headers: this.$store.state.config
    })
      .then(res=>{
        // console.log(res.data.credits)
        this.actors = res.data.credits
      })
      .catch(err=>{
        console.log(err);
      })

    // reviews 가져오기
    axios({
      method:'get',
      url:`https://mbti.link/movies/${this.movieId}/reviews/`,
      // headers: {"Authorization":`JWT ${localStorage.getItem('jwt')}`}
    })
      .then(res=>{
        // console.log(res.data.reviews)
        this.reviews = res.data.reviews
      })
      .catch(err=>{
        console.log(err);
      })
  },
  methods:{
    pick: function(){
      this.$store.dispatch('SetToken')
      axios({
        method:'post',
        url:`https://mbti.link/movies/${this.movieId}/pick/`,
        headers: this.$store.state.config
      })
        .then(()=>{
          if (this.is_pick === 'false'){
            this.is_pick = 'true'
            this.picks_cnt = this.picks_cnt + 1
          }
          else {
            this.is_pick = 'false'
            this.picks_cnt = this.picks_cnt - 1
          }
        })
        .catch(err=>{
          console.log(err);
        })
    }
  },
  // 날짜 슬라이싱
  filters: {
    shorter: function(value) {
    return value.slice(0, 4);
    }
  },
}
</script>

<style>
.col-4 {
  display: inline;
}
#movie-img {
  width: 100%;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
  border-radius: 10px;

}
.title {
  display: inline;
  text-align: left;
  margin-left: 0;
}
.title span {
  font-size: 24px;
}
#rating-form {
  margin-left: auto;
  padding: 30px 10px;
  background-color: transparent;
}
.overview {
  text-align: left;
  padding: 0;
  font-weight: 500;
  font-size: 14px;
  line-height: 1.5;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 6;
  -webkit-box-orient: vertical;
}
.genre-list{
  margin-left: auto;
  margin-right: 10px;
}
.genres {
  color: #936c35;
  font-weight: 600;
  display: inline;
  font-size: 14px;
  
}
.heart {
  margin-left: auto;
  margin-right: 10px;
}
.review-list {
  display: flex;
  flex-direction: column;

}
</style>