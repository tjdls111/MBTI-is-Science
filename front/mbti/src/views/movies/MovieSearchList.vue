<template>
  <div>
    <banner></banner>
    <div class="container" style="min-heigth: 700px; margin-bottom: 100px;">
      <h1 class="title-text-margin my-4 fw-bold">Search Results</h1>
      <MovieSearchForm></MovieSearchForm>

    <div v-if="searchedMovies.length">
      <main id="movie-search-main" class="container px-4 " role="main" style="max-width:none; margin-bottom:80px;"> 
        <!-- <div class="gutter mid">
          <div><p>MBTI is Science</p></div>
        </div>  -->
        <ul 
          class="thumbgrid" 
          id="movie-list" 
        >
          <movie-list-item
            v-for="movie in moviesForList"
            :key="movie.id"
            :movie="movie"
          ></movie-list-item>
        </ul>
        <b-pagination
          class="pagination"
          aria-controls="movie-list"
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          first-number
          last-number
          align="center"
        ></b-pagination>
      </main>
    </div>
    <div v-else class="my-5">
      <p>There are no search results... We are sorry..
      Please search with another keyword.</p>
    </div>

    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MovieListItem from '@/components/MovieListItem'
import Banner from '@/components/Banner'
import MovieSearchForm from '@/components/MovieSearchForm'

export default {
  name : 'MovieSearchList',
  components:{
    MovieListItem,
    Banner,
    MovieSearchForm,
  },
  data: function(){
    return {
      perPage: 6,
      currentPage: 1,
    }
  },

  methods:{

  },
  computed: {
    ...mapState(['searchedMovies',]),
    rows() {
      return this.searchedMovies.length
    },
    moviesForList() {
      return this.searchedMovies.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage,
    )
  },
  }
}
</script>

<style>
@media (min-width: 700px) {
  #movie-search-main {
    margin-top: 40%;
  }
}

</style>