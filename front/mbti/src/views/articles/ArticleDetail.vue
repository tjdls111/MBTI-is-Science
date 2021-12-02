<template>
  <div>
    <banner></banner>
    <div class="container" style="margin-bottom:80px;">
      <div class="d-flex flex-column">
        <div class="title">
          <router-link :to="{name: 'MovieDetail', query:{data: JSON.stringify({ movieId : articleDetail.movie.id})}}" style="text-decoration: none; font-size: 13px; font-weight: 500;">
            <p class="movie-title fs-5" >- {{ articleDetail.movie.title }}</p>
          </router-link>
          <div class="d-flex">
            <div class="article-detail-title fs-2 me-2">
              <span class="article-title-text">{{ articleDetail.title }}</span>
            </div>
            <div class="heart h3">
              <p class="count_show">{{likes_cnt}}</p>
              <span v-if ="is_like === 'false'">
                <b-iconstack size="lg" @click="like" >
                  <b-icon stacked icon="check" variant="danger" scale="0.75" shift-v="1"></b-icon>
                  <b-icon stacked icon="heart" variant="danger"></b-icon>
                </b-iconstack>
                <!-- <b-icon icon="heart" size="lg" class="text-danger" @click="like"></b-icon> -->
              </span>
              <span v-else>
                <b-iconstack size="lg" @click="like">
                  <b-icon stacked icon="heart-fill" variant="danger"></b-icon>
                  <b-icon stacked icon="check" variant="light" scale="0.75" shift-v="1"></b-icon>
                </b-iconstack>
                <!-- <b-icon icon="heart-fill" class="text-danger" @click="like"></b-icon> -->
              </span>
            </div>
            <div class="bookmark h3">
              <p class="count_show">{{bookmarks_cnt}}</p>
              <span v-if ="is_bookmark === 'false'">
                <b-icon icon="bookmark-check" size="lg" class="text-success" @click="bookmark"></b-icon>
              </span>
              <span v-else>
                <b-icon icon="bookmark-check-fill" class="text-success" @click="bookmark"></b-icon>
              </span>
            </div>
          </div>
        </div>
        <div class="d-flex align-items-center pt-4 mb-1">
          <div class="article-username">
            <router-link :to="{name: 'Profile', query:{data: JSON.stringify({user: articleDetail.author.username})}}" style="text-decoration: none; font-size: 13px; font-weight: 700; color:rgb(42, 90, 65); ">
            <p class="fs-5 mb-0" >{{ articleDetail.author.username }} </p>
          </router-link>
          </div>
          <div v-show="articleDetail.score" class="article-rating-form">
            <b-form-rating 
              id="rating-form"
              class="p-0"
              v-model="articleDetail.score" 
              variant="danger" 
              value-max="10"
              readonly
              show-value
              show-value-max
              icon-empty="heart"
              icon-half="heart-half"
              icon-full="heart-fill"
              size="sm"
              stars="10"
              no-border
            ></b-form-rating>
          </div>
        </div>
        <hr class="m-0">
      </div>
      <div class="article-content">
        <span class="article-content-text">{{ articleDetail.content }}</span>
      </div>
      <hr class="mb-1">
      <div class="d-flex align-items-center justify-content-between">
        <div class="at">
          created at:  {{ articleDetail.created_at.slice(5, 10) }} {{ articleDetail.created_at.slice(11, 19) }} / updated at: {{ articleDetail.updated_at.slice(5, 10) }} {{ articleDetail.updated_at.slice(11, 19) }}
        </div>

        <div v-if="isAuthor">
          <b-button @click="article_update" size="sm" variant="outline-secondary">Update</b-button>
          <b-button @click="article_delete" size="sm ms-1" variant="outline-secondary">Delete</b-button>
        </div>
        <b-button @click="goBack" size="sm" variant="outline-secondary">Back</b-button>
      </div>
      <div class="comment-list">
        <comment-list
          :comments="articleDetail.comment_set"
          :comment_count ="articleDetail.comment_count"
          :article_id="articleId"
        >
        </comment-list>
      </div>

      <div v-if="isLogin">
        <comment-form
          :article_id="articleId"
        ></comment-form>
      </div>
    </div>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList'
import CommentForm from '@/components/CommentForm'
import { mapState } from 'vuex'
import Banner from '@/components/Banner'
import axios from 'axios'

export default {
  name: 'ArticleDetail',
  components: {
    CommentList,
    CommentForm,
    Banner,
  },
  data: function(){
    return {
      isLogin: false,
      articleId: null,
      is_like: false,
      is_bookmark: false,
    }
  },
  mounted() {
    this.articleId = JSON.parse(this.$route.query.data).articleId
  },
  computed: {
    ...mapState([
      'articles',
      'articleDetail',
      'username',
    ]),
    isAuthor: function(){
      if (this.username === this.articleDetail.author.username)
        return true
      else
        return false
    }
  },
  methods: {
    like: function(){
      this.$store.dispatch('SetToken')
      axios({
        method:'post',
        url:`http://15.165.76.174:80/articles/${this.articleId}/likes/`,
        headers: this.$store.state.config
      })
        .then(()=>{
          if (this.is_like === 'false'){
            this.is_like = 'true'
            this.likes_cnt = this.likes_cnt + 1
          }
          else {
            this.is_like = 'false'
            this.likes_cnt = this.likes_cnt - 1
          }
        })
        .catch(err=>{
          console.log(err);
        })
    },
    bookmark: function(){
      this.$store.dispatch('SetToken')
      axios({
        method:'post',
        url:`http://15.165.76.174:80/articles/${this.articleId}/bookmark/`,
        headers: this.$store.state.config
      })
        .then(()=>{
          if (this.is_bookmark === 'false'){
            this.is_bookmark = 'true'
            this.bookmarks_cnt = this.bookmarks_cnt + 1
          }
          else {
            this.is_bookmark = 'false'
            this.bookmarks_cnt = this.bookmarks_cnt - 1
          }
        })
        .catch(err=>{
          console.log(err);
        })
    },

    article_delete : function(){
      this.$store.dispatch('SetToken')
      axios({
        method:'delete',
        url:`http://15.165.76.174:80/articles/${this.articleId}/`,
        headers: this.$store.state.config
      })
        .then(()=>{
          this.$router.push({name:'ArticleList'})
        })
        .catch(err=>{
          console.log(err);
        })
      
    },

    article_update: function(){
      this.$router.push({name:'ArticleCreate', 
        query: {data: JSON.stringify({ 
          title : `${this.articleDetail.title}`,
          score : `${this.articleDetail.score}`, 
          content : `${this.articleDetail.content}`,
          movieId : `${this.articleDetail.movie.id}`,
          movieTitle : `${this.articleDetail.movie.title}`,
          article_pk : `${this.articleId}`,
          
        })}})
    },
    goBack : function(){
      this.$router.go(-1)
    }
  },

  created: function(){
    console.log(JSON.parse(this.$route.query.data).articleId)
    this.articleId = JSON.parse(this.$route.query.data).articleId

    this.$store.dispatch('LoadArticleDetail', this.articleId)

    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }

    axios({
      method:'get',
      url:`http://15.165.76.174:80/articles/${this.articleId}/is_like/`,
      headers: this.$store.state.config
    })
      .then(res=>{
        // console.log(res.data)
        this.is_like = res.data.is_like
        this.likes_cnt = res.data.likes_cnt
      })
      .catch(err=>{
        console.log(err);
      })


    axios({
      method:'get',
      url:`http://15.165.76.174:80/articles/${this.articleId}/is_bookmark/`,
      headers: this.$store.state.config
    })
      .then(res=>{
        // console.log(res.data)
        this.is_bookmark = res.data.is_bookmark
        this.bookmarks_cnt = res.data.bookmarks_cnt
      })
      .catch(err=>{
        console.log(err);
      })
  }

}
</script>

<style>
.article-detail-title {
  font-weight: bold;
  color: #2e2e2e;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  
}
.article-rating-form {
  margin-left: auto;
}
.article-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  border: 1px solid rgb(0, 0, 0, 0.25);
  padding: 20px;
  margin: 20px 0;
  color: white;
  text-align: left;
  background-color:rgb(42, 90, 65);
  font-weight: 500;
  min-height: 150px;
  
}
.at {
  color: hsla(0, 0%, 0%, 0.45);
  font-size: 14px;
}

.comment-list {
  margin: 30px 0 30px 0;
}

.count_show{
  color: hsla(0, 0%, 0%, 0.45);
  font-size: 14px;
  position: relative;
  animation-name: move_quick;
  animation-duration: 4s;
  animation-iteration-count: infinite;
}

@keyframes move_quick{
    0%   {left:0px; top:0px;}
    25%  {left:10px; top:0px;}
    50%  {left:10px; top:10px;}
    75%  {left:0px; top:10px;}
    100% {left:0px; top:0px;}

}
</style>