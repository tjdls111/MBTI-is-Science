<template>
  <li id="list">
    <div >
      <p class="actor-character fs-6 text-danger" style="width: 6em;">{{ actor.character }}</p>
      <a target="_blank" v-bind:href="`https://www.themoviedb.org/person/${actor.id}`">
        <img v-if="actor.profile_path !== null" :src="`https://image.tmdb.org/t/p/w500/${actor.profile_path}`" style="width: 6em;">
      </a>
      <!-- <img v-else src="../assets/logo.png"> -->
      <span class="actor-name">{{ actor.name }}</span>
    </div>
  </li>
</template>

<script>
export default {
  name: 'MovieActorList',
  props: {
    actor: Object,
  }
}
</script>

<style>
.actor-character {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.actor-name {
  display: block;
  color: gray;
  font-size: 13px; 
  font-weight: 500;
  margin-top: 10px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style>