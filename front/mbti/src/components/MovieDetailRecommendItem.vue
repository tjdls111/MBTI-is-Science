<template>
  <div>
  <li id="list">
    <a target="_blank" v-bind:href="`https://www.themoviedb.org/movie/${movie.id}`">
      <div>
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`">
        <p>{{ movie.title }}</p>
      </div>
    </a>
  </li>

  </div>
</template>

<script>
export default {
  name:"MovieDetailRecommendItem",
  props:{
    movie:Object,
    movieDetail: [],
  }
}
</script>

<style>

</style>