<template>
  <div>
    <form class="content-textarea" @submit = "CreateComment">
      <b-form-textarea
        v-model="content"
        placeholder="Enter comment..."
        autofocus
      ></b-form-textarea>
      <b-button class="ms-2" variant="outline-success" type="submit"> Write </b-button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CommentForm',
  data: function(){
    return {
      content: null,

    }
  },
  props:{
    article_id:Number,
  },
  methods :{
    CreateComment: function(event){
      
      event.preventDefault()
      this.content = event.target[0].value
      console.log(event.target[0].value)


      axios({
        method: 'post',
        url: `https://mbti.link/articles/${this.article_id}/comments/`,
        headers: {"Authorization":`JWT ${localStorage.getItem('jwt')}`},
        data : {"content" : this.content}
      })
        .then( () => {
          // console.log(res)
          
          this.$store.dispatch('LoadArticleDetail', this.article_id)
          this.content = ""
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  },
  

}

</script>

<style>
.content-textarea{
  display: flex;
  padding: 20px;
}
</style>