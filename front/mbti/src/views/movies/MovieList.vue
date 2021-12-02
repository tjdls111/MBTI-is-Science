<template>
  <div class="movie-list-main">
    <hero></hero>
    <banner></banner>

    <!-- <section role="movie-list">
      <div id="create-btn" ><b-button size="sm" variant="outline-warning" :to="{name: 'MbtiTest'}" >Go to the MBTI test<b-icon class="fs-6" icon="file-earmark-text-fill" ></b-icon></b-button></div>
    </section> -->
    <MovieSearchForm></MovieSearchForm>
    
    <section v-show="isLogin && userMbti!=='IDKW'" role="movie-list">
      <movie-mbti-recommend
      ></movie-mbti-recommend>
    </section>
    <!-- <section v-show="isLogin && userMbti==='IDKW'" role="movie-list"> -->


    <section role="movie-list">
      <movie-weather-recommend
      ></movie-weather-recommend>
    </section>

    <h1 class="title-text title-text-margin mt-5">🔔 Movies</h1>
    <div class="d-flex flex-row-reverse px-5">
      <b-dropdown text="Sort" variant="*" id="movie-dropdown-btn">
          <b-dropdown-item @click="sortMovie(0)">score highest</b-dropdown-item>
          <b-dropdown-item @click="sortMovie(1)">score lowest</b-dropdown-item>
          <b-dropdown-item @click="sortMovie(2)">latest</b-dropdown-item>
          <b-dropdown-item @click="sortMovie(3)">oldest</b-dropdown-item>
          <b-dropdown-item @click="sortMovie(4)">pick highest</b-dropdown-item>
      </b-dropdown>
    </div>
    <main class="container px-4 mt-1" role="main" style="max-width: none; margin-bottom: 80px;">
      <div class="gutter mid">
        <div><p>MBTI is Science</p></div>
      </div>
        <ul 
          class="thumbgrid" 
          id="movie-list" 
        >
          <movie-list-item
            v-for="(movie, idx) in moviesForList"
            :key="movie.id"
            :movie="movie"
            :idx="idx"
          ></movie-list-item>
        </ul>
      <div >
        <b-pagination
          class="pagination"
          aria-controls="movie-list"
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          first-text="«"
          last-text="»"
          pills
          align="center"
        ></b-pagination>
      </div>
    </main>

  </div>
</template>

<script>
import MovieMbtiRecommend from '@/components/MovieMbtiRecommend'
import MovieWeatherRecommend from '@/components/MovieWeatherRecommend'
import MovieListItem from '@/components/MovieListItem'
import Hero from '@/components/Hero'
import Banner from '@/components/Banner'
import MovieSearchForm from '@/components/MovieSearchForm'
import {mapState} from 'vuex'

export default {
  name: 'MovieList',
  components: {
    MovieMbtiRecommend,
    MovieWeatherRecommend,
    MovieListItem,
    Hero,
    Banner,
    MovieSearchForm,
  },
  methods:{
    sortMovie: function(sort_num){
      this.$store.dispatch("LoadMovieListBy",sort_num)
    }
  },
  created: function () {
    this.$store.dispatch('LoadMovieList')
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  },
  computed : {
    ...mapState(['movies','userMbti']),
    rows() {
      return this.movies.length
    },
    moviesForList() {
      return this.movies.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage,
    )
    }
  },
  data: function(){
    return {
      isLogin: false,
      perPage: 10,
      currentPage: 1,
    }
  },
}
</script>

<style>
.title-text-margin {
  margin: 35px auto 0 6%;
}

/* ============================================================
/* LAYOUT
/* ============================================================ */

.movie-list-main {
  height: 100%;
}

main {
  display: block;
  position: relative;
}


/* ------------------------------------------------------------
/* The Gutter
/* ------------------------------------------------------------ */
div.gutter {
  display: none;
}

div.gutter.mid {
  display: block;
  margin: 0 auto;
  padding: 4rem 0 4rem 0;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 14px;
  font-weight: 600;
  color: #936c35;
  -webkit-font-smoothing: subpixel-antialiased;
  -moz-osx-font-smoothing: auto;
  width: 100%;
  height: 15rem;
  background: url("https://blog.kakaocdn.net/dn/6Ol7o/btrl5wcHsqU/cYaT4YKWBJsFkUkyVxjYvk/img.gif") no-repeat 50% 50%;
  background-size: calc(30vh - 7rem);
  text-align: center;
  display: flex;
  align-items: center;
}

div.gutter.mid div {
  max-width: 20em;
  margin: 0 auto;
  margin-bottom: 8rem;
}

@media (min-width: 700px) {
  
  div.gutter,
  div.gutter.mid {
    display: block;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-size: 14px;
    -webkit-font-smoothing: subpixel-antialiased;
    -moz-osx-font-smoothing: auto;
    position: sticky;
    position: -webkit-sticky;
    width: 30vw;
    height: 30vw;
    left: calc(50% - 15vw);
    /* top: calc(50% - 15vw - 2rem); */
    top: calc(50% - 100px);
    background: url("https://blog.kakaocdn.net/dn/6Ol7o/btrl5wcHsqU/cYaT4YKWBJsFkUkyVxjYvk/img.gif") no-repeat 50% 50%;
    background-size: calc(40vh - 7rem);
    text-align: center;
    display: flex;
    align-items: center;
    margin-bottom: 2rem;
  }

  /* Accommodate the vertical space occupied by middle column */
  ul.thumbgrid {
    margin-top: -28vw !important;
  }

  div.gutter div {
    /* transform: rotate(90deg); */
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    text-align: center;
  }

  div.gutter div p {
    text-align: center;
    width: 100%;
    margin-bottom: 25%;
    font-weight: 600;
    color: #936c35;
  }
}
/* Hide all gutter contents if window is short */
@media (max-height: 300px) {
  div.gutter {
    display: none;
  }
}
/* Hide caption if window is not tall enough for rotated text */
@media (max-height: 500px) {

}
/* Limit H in background and caption if window is very wide */
@media (min-height: 600px), (min-width: 1400px) {
  div.gutter,
  div.gutter.mid {
    background-size: 175px;
    
  }
}
@media (min-width: 1400px) {
  ul.thumbgrid {
    margin-top: -330px !important;
  }

  div.gutter,
  div.gutter.mid {
    width: 300px;
    height: 300px;
    margin-bottom: 9em;
    font-weight: 600;
    left: calc(50% - 150px);
    top: calc(50% - 150px + 2rem);
  }
}
/* ------------------------------------------------------------
/* Thumbnail Grid (for staff list, projects, etc.)
/* ------------------------------------------------------------ */
ul.thumbgrid {
  list-style: none;
  padding: 0;
  margin: 0;
}

ul.thumbgrid a {
  text-decoration: none;
  color: rgb(42, 90, 65);
  transition: 0.2s all ease;
  -webkit-transform: translateZ(0);
  -moz-transform: translateZ(0);
  -ms-transform: translateZ(0);
  -o-transform: translateZ(0);
  transform: translateZ(0);
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -ms-backface-visibility: hidden;
  backface-visibility: hidden;
}

ul.thumbgrid a img {
  transition: 0.2s all ease;
  -webkit-transform: translateZ(0);
  -moz-transform: translateZ(0);
  -ms-transform: translateZ(0);
  -o-transform: translateZ(0);
  transform: translateZ(0);
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -ms-backface-visibility: hidden;
  backface-visibility: hidden;
  box-shadow: 3px 1px 12px 1px rgba(0, 0, 0, 0.5);
  border-radius: 15px;
}

ul.thumbgrid a:hover {
  color: #936c35;
}

ul.thumbgrid a:hover img {
  filter: brightness(0.4);
}

ul.thumbgrid img {
  display: block;
  width: 100%;
  margin-bottom: 1rem;
}

ul.thumbgrid strong {
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 12px;
  display: block;
}

ul.thumbgrid li {
  width: 60%;
  margin-bottom: 4rem;
}

ul.thumbgrid li:nth-child(even) {
  margin-left: 40%;
}

ul.thumbgrid div.portraitimg {
  position: relative;
}

ul.thumbgrid div.portraitimg div.text {
  position: absolute;
  margin: 0;
  padding-left: 0 !important;
  text-align: center;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  opacity: 0;
  transition: opacity 0.3s ease;
  -webkit-transform: translateZ(0);
  -moz-transform: translateZ(0);
  -ms-transform: translateZ(0);
  -o-transform: translateZ(0);
  transform: translateZ(0);
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -ms-backface-visibility: hidden;
  backface-visibility: hidden;
  color: #fbfaf6;
  text-shadow: 0 0 5px #000;
  display: flex;
  align-items: center;
}

ul.thumbgrid div.portraitimg div.text strong {
  width: 100%;
}

ul.thumbgrid div.portraitimg div.text:after {
  content: "";
  border: 3px double #936c35;
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 12px;
  top: 12px;
}

ul.thumbgrid a:hover div.portraitimg div.text {
  opacity: 1;
}


@media (min-width: 700px) {
  ul.thumbgrid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  ul.thumbgrid li {
    margin-bottom: 3rem;
  }

  ul.thumbgrid li:nth-child(odd),
  ul.thumbgrid li:nth-child(even) {
    width: 35%;
    padding: 0;
    margin-left: 0;
    margin-right: 0;
    /* align-self: flex-start; */
  }

  /* ul.thumbgrid li:nth-child(2n - 1),
  ul.thumbgrid li:nth-child(2n) {
    align-self: baseline;
  } */

  /* ul.thumbgrid:not(.staff) li:nth-child(4n - 1),
  ul.thumbgrid:not(.staff) li:nth-child(4n) {
    margin-top: -10vw;
  } */

  ul.thumbgrid strong {
    font-size: 14px;
  }
}
@media (min-width: 1440px) {
  ul.thumbgrid {
    max-width: 1400px;
    margin: 0 auto;
  }

  ul.thumbgrid li:nth-child(odd) a > strong {
    padding-left: 0;
  }

  /* ul.thumbgrid:not(.staff) li:nth-child(4n - 1),
  ul.thumbgrid:not(.staff) li:nth-child(4n) {
    margin-top: -9rem;
  } */
}

.pagination{
  padding: 1rem;
}
.page-link{
  color: rgb(42, 90, 65) !important;
}
.page-item.active .page-link {
  z-index: 3;
  color: #fff !important;
  background-color: rgb(42, 90, 65) !important;
  border-color: rgb(42, 90, 65) !important;
}
#movie-dropdown-btn__BV_toggle_ {
  color: #919191;

}

</style>