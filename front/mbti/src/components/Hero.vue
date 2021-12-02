<template>
  <div class="hero">
      <div class="info"></div>
      <b-carousel
        id="carousel-1"
        :interval="4000"
        fade
        controls
        indicators
        label-next
        label-prev
        background="#000000"
        style="text-shadow: 1px 1px 3px #333;"
      > 
        <b-carousel-slide
          class="test-page bg-none"
          img-src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbaSAT8%2FbtrmamVx9qo%2FeTuX7MAxA1L7cTP4ggJr41%2Fimg.png"
          text-color="rgb(42, 90, 65)"
        ><b-button :to="{name: 'MbtiTest'}" pill variant="danger" size="lg" id="test-page-btn">Test It Now</b-button>
        </b-carousel-slide>
        <b-carousel-slide
          caption="Christmas movie recommendation."
          text="Spend a fruitful Christmas alone."
          img-src="https://thumbs.gfycat.com/AdeptShrillHoneybee-size_restricted.gif"
          text-color="rgb(42, 90, 65)"
        ><b-button @click="search_christmas_movie" pill variant="outline-light" id="tr-btn"><b-icon icon="caret-right-fill"></b-icon> Watch Now</b-button>
        </b-carousel-slide>
        <b-carousel-slide
          caption="The Christmas chronicles: Part Two"
          text="2020 | All | 1h 55m | Comedies"
          img-src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcUmouM%2FbtrlgTOFJ18%2FXFQjG63RZ8tspDZNe3h76K%2Fimg.jpg"
        ><b-button pill v-b-modal.modal-1 variant="outline-light" id="tr-btn" >
            <b-icon icon="caret-right-fill"></b-icon> 
            Play Trailer</b-button>
            <b-modal id="modal-1" title="Trailer">
            <p class="mt-4">The Christmas chronicles: Part Two</p>
            <b-embed
              class=""
              type="iframe"
              allowfullscreen
              autoplay
              aspect="16by9"
              src="https://www.youtube.com/embed/HVzBwSOcBaI"
            ></b-embed>
            </b-modal>
        </b-carousel-slide>
        <b-carousel-slide
          caption="The Claus Family"
          text="2020 | All | 1h 37m | Family Movies"
          img-src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcraxQq%2FbtrlmnhhTYM%2FbX1MuI2VhYr3MSm2stXuhk%2Fimg.jpg"
        ><b-button pill v-b-modal.modal-2 variant="outline-light" id="tr-btn" >
            <b-icon icon="caret-right-fill"></b-icon> 
            Play Trailer</b-button>
            <b-modal id="modal-2" title="Trailer" class="align-center">
            <p class="mt-4">The Claus Family</p>
            <b-embed
              class=""
              type="iframe"
              allowfullscreen
              aspect="16by9"
              autoplay
              src="https://www.youtube.com/embed/mOgHcgm-riI"
            ></b-embed>
            </b-modal>
        </b-carousel-slide>
      </b-carousel>
    </div>

</template>

<script>
import axios from 'axios'

export default {
  name: 'Hero',
  methods:{
    search_christmas_movie: function(event){
      event.preventDefault()

      axios({
        method: 'get',
        url: `https://mbti.link/movies/christmas/search/`,

      })
        .then( (res) => {
          // console.log(res)
          this.$store.dispatch("searchMovies", res.data)
          this.$router.push({name:'MovieSearchList'})
          
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  font-family: 'Quicksand', 'Noto Sans KR', sans-serif;
  text-align: left;
}
body {
  font-family: 'Quicksand', 'Noto Sans KR', sans-serif;
}
/* ------------------------------------------------------------
/* Hero
/* ------------------------------------------------------------ */

.hero {
  /* position: relative; */
  overflow: hidden;
  /* display: flex; */
  width: 100%;
  height: 70%;
}

#hero-img {
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  text-align: center;
  position: relative;
  background-image: url('https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcUmouM%2FbtrlgTOFJ18%2FXFQjG63RZ8tspDZNe3h76K%2Fimg.jpg');
}

#tr-btn {
  font-size: 13px;
}
/* ------------------------------------------------------------
/* MBTI test
/* ------------------------------------------------------------ */
div.embed-responsive.embed-responsive-16by9 {
  text-align: center;
  margin: 20% 10%;
  /* padding-bottom: 30px; */
  color: white;
  /* background-color: #eeeeee; */
}
#modal-scrollable___BV_modal_header_{
  background-color: rgb(42, 90, 65);
}
.sv_container{
  overflow: scroll;
  padding-bottom: 10%;
}
#surveyElement {
  padding-bottom: 80px;
}
.sv_nav {
  margin-left: auto;
}
.test-page {
  position: relative;
}
button .close {
  display: none;
}
</style>