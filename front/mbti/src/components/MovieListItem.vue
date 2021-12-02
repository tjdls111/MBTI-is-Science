<template>
  <li>

    <!-- <div v-if="idx === 4" class="odd odd-left">
      <img src="https://blog.kakaocdn.net/dn/9gRI0/btrmaMMHPYC/hKki1SSxr0Lk0OsG2fGV60/img.gif" alt="">
    </div> -->
    <!-- <div v-if="idx === 6" class="odd odd-left">
      <img src="https://blog.kakaocdn.net/dn/SHiYc/btrl57EPosM/rhpcBZDjHye2Uc7CwPlGg0/img.gif" alt="">
    </div> -->
    <router-link :to="{name: 'MovieDetail', query:{data: JSON.stringify({ movieId : `${movie.id}`})}}">
      <div class="portraitimg">
          <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`">
          <div class="text align-center" >
            <strong> <b-icon icon="caret-down-fill" style="width: 15%; height: 15%;"></b-icon> <br> "{{ movie.title }}" </strong>
          </div>
      </div>
          <strong>: {{ movie.title }} :</strong>
    </router-link>
    <!-- <div v-if="idx === 5" class="odd odd-right">
      <img src="https://blog.kakaocdn.net/dn/YFo7a/btrl8nUHPoI/mRpaXruge5t6sIcsDIurn1/img.gif" alt="">
    </div> -->
    <!-- <div v-if="idx === 7" class="odd odd-right">
      <img src="https://blog.kakaocdn.net/dn/6Ol7o/btrl5wcHsqU/cYaT4YKWBJsFkUkyVxjYvk/img.gif" alt="">
    </div> -->
  </li>

</template>

<script>
// import axios from 'axios'

export default {
  name: 'MovieMbtiRecommendItem',
  props:{
    movie:Object,
    movieDetail: [],
    idx: Number,
  },
  
}
</script>

<style>
.portraitimg {
  margin: 30px 0;
  
}
ul.thumbgrid {
  margin: auto;
}
.odd {
  display: none;
}

@media (min-width: 700px) {
  .odd {
    opacity: 90%;
    display: list-item;
    align-self: baseline;
    width: 90%;
    padding: 0;
    margin-left: 0;
    margin-right: 0;
  }
  .odd-left {
    align-self: flex-start;
    padding-left: 10%;
    margin-bottom: 6rem;
  }
  .odd-right {
    align-self: baseline;
    margin-bottom: 0;
  }
  .odd img{
    display: block;
    width: 90%;
    margin: 1rem;
  }
}
</style>