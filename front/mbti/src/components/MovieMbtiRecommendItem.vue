<template>

  <li id="list">
    <router-link  :to="{name: 'MovieDetail', query:{data: JSON.stringify({ movieId : `${movie.id}`})}}">
      <div>
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`">
        <p class="pt-1">{{ movie.title }}</p>
      </div>
    </router-link>
  </li>

</template>

<script>
// import axios from 'axios'

export default {
  name: 'MovieMbtiRecommendItem',
  props:{
    movie:Object,
    movieDetail: [],

  },
  
}
</script>

<style>
#list img {
  /* margin: 30px 0; */
  width: 10em;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
  border-radius: 10px;
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


#list img:hover {
  filter: brightness(0.4);
}
#list {
  max-width: 200px;
  padding: 0 10px;
  display: block;
}
#list a{
  text-decoration: none;
}
#list p:hover {
  color: #936c35;
}
#list p {
  color: rgb(42, 90, 65);
  font-weight: bold;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style>