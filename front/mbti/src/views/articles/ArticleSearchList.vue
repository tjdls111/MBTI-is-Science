<template>
  <div>
    <banner></banner>
    <div class="container mt-5" style="min-height: 500px; margin-bottom:100px;">

      <h1 class="review-title mb-5">Search Results</h1>
      <ArticleSearchForm></ArticleSearchForm>

      <div v-if="searchedArticles.length">
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
        <div class="article-pagination">
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
      <div v-else class="py-5">
        <p>There are no search results... We are sorry..
        Please search with another keyword.</p>
      </div>
    </div>


    </div>
</template>

<script>
import { mapState } from 'vuex'
import ArticleListItem from '@/components/ArticleListItem'
import Banner from '@/components/Banner'
import ArticleSearchForm from '@/components/ArticleSearchForm'

export default {
  name : 'ArticleSearchList',
  components:{
    ArticleListItem,
    Banner,
    ArticleSearchForm
  },
  data: function(){
    return {
      perPage: 5,
      currentPage: 1,

    }
  },

  methods:{

  },
  computed: {
    ...mapState(['searchedArticles',]),
    rows() {
      return this.searchedArticles.length
    },
    articlesForList() {
      return this.searchedArticles.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage,
      )
    },
  }

}
</script>

<style>
/* .article-pagination {

} */
</style>