<template>
<div>
  <banner></banner>
  <div class="container" style="margin-bottom:80px;">
    <h1 class="review-title">🎞 Movie Review</h1>
    <div id="create-btn" v-show="isLogin"><b-button style="padding: 0.46rem 0.53rem" size="sm" variant="danger" :to="{name: 'ArticleCreate'}" > Create <b-icon class="fs-6" icon="pencil-fill" ></b-icon></b-button></div>
    <div class="d-flex justify-content-between">
      
      <b-dropdown text="Sort" variant="*" id="dropdown-btn">
        <b-dropdown-item @click="find_by(0)">oldest</b-dropdown-item>
        <b-dropdown-item @click="find_by(1)">latest</b-dropdown-item>
        <b-dropdown-item @click="find_by(3)">score highest</b-dropdown-item>
        <b-dropdown-item @click="find_by(2)">score lowest</b-dropdown-item>
        <b-dropdown-item @click="find_by(5)">bookmark highest</b-dropdown-item>
        <b-dropdown-item @click="find_by(6)">like highest</b-dropdown-item>
      </b-dropdown>
      <ArticleSearchForm></ArticleSearchForm>
    </div>
    <div>
      <ul style="padding-left: 0;">
        <article-list-item
          v-for="article in articlesForList"
          :key="article.pk"
          :article="article"
          :movie="article.movie"
        ></article-list-item>
      </ul>
    </div>
  <b-pagination 
    class="text-success" 
    align="center" 
    v-model="currentPage" 
    pills 
    :total-rows="rows"
    :per-page="perPage"
    first-number
    last-number
    ></b-pagination>
  </div>
</div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'
import { mapState } from 'vuex'
import Banner from '@/components/Banner'
import ArticleSearchForm from '@/components/ArticleSearchForm'


export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
    Banner,
    ArticleSearchForm
  },
  created: function () {
    this.$store.dispatch('LoadArticleList')
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
    
  },
  data: function(){
    return {
      perPage: 10,
      currentPage: 1,
      isLogin: false,
    }
  },
  computed: {
    ...mapState(['articles']),
    rows() {
      return this.articles.length
    },
    articlesForList() {
      return this.articles.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage,
      )
    },
  },
  methods: {
    find_by:function(sort_num){
      this.$store.dispatch("LoadArticleListBy", sort_num)
    },


  },
  
}
</script>

<style>
.container {
  margin: 60px auto;
}
#create-btn {
  text-align: right;
  margin-right: 0;
  display: block;
}
h1 {
  color: rgb(42, 90, 65);
}

.review-title {
  text-align: left;
  margin-bottom: 10px;
  margin-left: 0;
  font-weight: bold;
}
#dropdown-btn__BV_toggle_ {
  color: #919191;
}
</style>