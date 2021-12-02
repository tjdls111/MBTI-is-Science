<template>
  <div>
    <ul v-if="articleDetail.comment_set.length" class="ps-0">
      <!-- <h4>comments: {{articleDetail.comment_count}}</h4> -->
        <comment-list-item
          v-for = "comment in articleDetail.comment_set"
          :key = "comment.id"
          :comment = "comment"
          :comment_id = "comment.id"
          :article_id = "article_id"
          :profile_number="comment.author.poster_number"
        >
        </comment-list-item>
        <p class="at text-end">total: {{ articleDetail.comment_count }} </p>
    </ul>
    <div v-else>
      <p>There are no comments...</p>
    </div>
  </div>
</template>

<script>
import CommentListItem from './CommentListItem.vue'
import { mapState } from 'vuex'

export default {
  name: 'CommentList',
  components: {CommentListItem},
  data : function(){
    return {
      
    }
  },
  created: function(){ 
    this.$store.dispatch('LoadArticleDetail', this.article_id)
  },
  props:{
    article_id: Number, 
  }, 
  functions :{
    
  },
  computed: {
    ...mapState([
      'articleDetail'
    ])
  }
  

}
</script>

<style>

</style>