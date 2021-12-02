<template>
  <li class="d-flex row ">
    <div class="comment row">
      <div class="col-3 d-flex flex-column justify-content-center align-items-center">
        <img v-if="profile_number" class="selected-img comment-profile-img" :src="require(`@/assets/profile_img${profile_number}.gif`)" alt="profile image">
        <img v-else class="selected-img comment-profile-img" src="@/assets/profile_img1.gif" alt="profile image">
        <router-link :to="{name: 'Profile', query:{data: JSON.stringify({user: comment.author.username})}}" style="text-decoration: none; font-size: 18px; font-weight: 700; color:rgb(42, 90, 65); ">
          <p class="user-link" >{{ comment.author.username }} </p>
        </router-link>
      </div>
      <div class="comment-content col-8">
        <p>{{comment.content}}</p>
        <div class="at">
          created at:  {{ comment.created_at.slice(5, 10) }} {{ comment.created_at.slice(11, 19) }}
        </div>
      </div>
      <div class="col-1" v-if="isAuthor">
        <b-button 
          class="text-decoration-none text-secondary"
          variant="link" 
          @click="comment_delete"
          size="sm"
        >X</b-button>
      </div>
    </div>
  </li>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'


export default {
  name: 'CommentListItem',
  props:{
    comment: Object,
    comment_id : Number,
    article_id: Number,
    profile_number:Number,
  },
  filters: {
    shorter: function(value) {
    return value.slice(0, 10);
    }
  },
  computed: {
    ...mapState(['username',]),

    isAuthor: function(){
      if (this.username === this.comment.author.username){
        return true
      }
      else{
        return false
      }
    }
  },

  methods :{
    comment_delete: function(){
      axios({
        method:'delete',
        url:`http://15.165.76.174:80/articles/comments/${this.comment_id}/`,
        headers: {"Authorization":`JWT ${localStorage.getItem('jwt')}`}
      })
        .then(res=>{
          this.$store.dispatch('LoadArticleDetail', this.article_id)
          console.log(res.data.reviews)
          
        })
        .catch(err=>{
          console.log(err);
        })
    }

  }
}
  
</script>

<style>
.comment {
  margin: 6px;  
  align-items: center;
  padding: 0 !important;
} 
.comment-content{
  /* color: white; */
  /* background-color: rgb(42, 90, 65); */
  color: rgba(0, 0, 0, 0.65);
  font-weight: 500;
  font-size: 15px;
  text-align: right;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}
.comment-content p{
  border-bottom: 1px solid rgb(42, 90, 65);
  text-align: left;
}
.comment p {
  margin: 0;
  padding: 3px;
  line-height: 1.5;
}

.comment-profile-img{
  width: 30%;
}

</style>