<template>
<div>
  <li>
    <div class="row d-flex align-items-center">
      <div class="col-4">
        <div>
          <span v-if="getAvatar === null" class="me-2"><b-avatar></b-avatar></span>
          <span v-else class="me-2">
            <b-avatar v-if="isTmdb === false" :src="require(`@/assets/profile_img${reviewAvatar}.gif`)"></b-avatar>
            <b-avatar v-else :src="reviewAvatar"></b-avatar>
          </span>
          <span class="review-author fs-6 text-success fw-bold"> {{ review.author }}</span>
        </div>
        <b-form-rating 
          v-if="review.rating !== null"
          id="rating-form"
          v-model="review.rating" 
          variant="danger" 
          value-max="10"
          readonly
          inline
          icon-empty="heart"
          icon-half="heart-half"
          icon-full="heart-fill"
          size="sm"
          stars="10"
          no-border
          class="p-0"
        ></b-form-rating>
      </div>
      <div class="col-8">
        <span class="review-content text-secondary"> {{ review.content }}</span>
      </div>
    </div>
  </li>
  <hr>
</div>
</template>

<script>
export default {
  name: 'MovieReviewList',
  props: {
    review: Object,
    reviewAvatar: String,
  },
  computed: {
    getAvatar: function(){
      if (this.reviewAvatar.match('/https://secure.gravatar.com/')){
        return null
      }
      else{
        return this.reviewAvatar
      }
    },
    isTmdb: function(){
      if (this.reviewAvatar.match('https://image.tmdb.org/t/p/w500/')){
        return true
      }
      else{
        // console.log(this.reviewAvatar)
        return false
      }
    }

  },
  created: function(){
    console.log(typeof(this.reviewAvatar));
  }
}
</script>

<style>
  .review-content {
    text-align: left;
    padding: 0 0 0 3%;
    font-weight: 500;
    font-size: 13px;
    line-height: 1.5;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;

  }
  #rating-form {
    background-color: none;
  }
</style>