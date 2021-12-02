<template>
<div>
  <li class="article-list">
    <hr>
    <div class="row justify-content-center align-items-center">
      <div class="col-2 created-at">
        {{article.created_at | shorter }}
      </div>
      <div class="col-5 title" >
        <router-link :to="{name: 'MovieDetail', query:{data: JSON.stringify({ movieId : movie.id})}}" style="text-decoration: none; font-size: 13px; font-weight: 500;">
          <p class="movie-title" >{{ article.movie.title }} </p>
        </router-link>
        <router-link :to="{name: 'ArticleDetail', query:{data: JSON.stringify({ articleId : article.id})}}" style="text-decoration: none;">
          <p class="article-title">{{ article.title }} <span class="text-secondary fw-normal" style="font-size:13px;">[{{ article.comment_count }}]</span></p>
        </router-link>
      </div>
      <div class="col-1">
        <router-link :to="{name: 'Profile', query:{data: JSON.stringify({user: article.author.username})}}" style="text-decoration: none; font-size: 13px; font-weight: 700; color:rgb(42, 90, 65); ">
        <img v-if="article.author.poster_number" class="selected-img" :src="require(`@/assets/profile_img${article.author.poster_number}.gif`)" alt="profile image">
        <img v-else class="selected-img" src="@/assets/profile_img1.gif" alt="profile image">
          <p class="user-link mb-0" >{{ article.author.username }} </p>
        </router-link>
      </div>
      <div class="col-4 mt-1">
        <b-form-rating 
          id="article-list-rating-form"
          v-model="article.score" 
          variant="danger" 
          value-max="10"
          readonly
          icon-empty="heart"
          icon-half="heart-half"
          icon-full="heart-fill"
          size="sm"
          stars="10"
          no-border
        ></b-form-rating>
      </div>
      <!-- <b-button @click="clickParams">detail</b-button> -->
    </div>
    
  </li>
</div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'ArticleListItem',
  props:{
    article: Object,
    movie: Object
  },
  data: function(){
    return {}
  },
  filters: {
    shorter: function(value) {
    return value.slice(0, 10);
    }
  },
  computed: {
    ...mapState(['username'])
  },
  methods: {
    setToken: function (){
      
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    deleteArticleListItem: function (article) {
      axios({
        method: 'delete',
        url: `https://mbti.link/articles/${article.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          // localStorage.removeItem(res.data)
          this.getArticleList()
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateArticleListItem: function (article) {
      const articleItem = {
        ...article,
      }

      axios({
        method: 'put',
        url: `https://mbti.link/articles/${article.id}/`,
        data: articleItem,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
        })

        .catch(err => {
          console.log(err)
        })
    },
  }

}
</script>

<style>
li {
  list-style: none;
}
.article-list p:hover {
  color: #936c35;
}
.created-at {
  font-size: 13px;
  color: rgb(145, 145, 145);
  line-height: 2;
}
.title {
  display: block;
}
.movie-title {
  color: rgb(145, 145, 145);
  /* margin-right: auto; */
  text-align: left;
  line-height: 1;
  padding-bottom: 5px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  margin-bottom: 0;
}
.article-title {
  margin-bottom: auto;
  text-align: left;
  font-size: 16px;
  font-weight: 600;
  line-height: 1.5;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  text-decoration: none;
  cursor: pointer;
  color: #2e2e2e;
}
.article-title:hover {
  color: #936c35;
}
#article-list-rating-form {
  background: none;
  padding: 0;
}
</style>