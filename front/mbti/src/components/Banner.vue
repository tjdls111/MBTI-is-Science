<template>
  <header role="banner">
      <nav class="navigation column" role="navigation">
        <div>
          <router-link to="/" class="logo" rel="move-list">💡MBTI is Science💡</router-link> 
          <router-link to="/" >
            <span class="effect">Movie</span>
          </router-link> 
          <router-link :to="{name:'ArticleList'}">
            <span class="effect">Review</span>
          </router-link> 
          <router-link v-if="isLogin" @click.native="logout" to="#">
            <span class="effect">Logout</span>
          </router-link>
          <router-link v-else :to="{name:'Login'}">
            <span class="effect">Login</span>
          </router-link> 
          <router-link v-if="isLogin" :to="{name:'Profile', query:{data: JSON.stringify({user: username})}}" >
          <b-avatar v-if="userProfileNum" badge-top :src="require(`@/assets/profile_img${userProfileNum}.gif`)" size="2rem" >
            <template #badge><b-icon icon="star-fill" variant="warning" animation="spin-reverse"></b-icon></template>
          </b-avatar></router-link>
          <router-link v-else :to="{name:'Signup'}">
            <span class="effect">Signup</span>
          </router-link> 
        </div>
      </nav>
    </header>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'Banner',
  data: function(){
    return {
      isLogin: false,
      profile_number:null,
    }
  },
  computed: {
    ...mapState(['username','userProfileNum']),
    getAvatar: function(){
      if (this.reviewAvatar.match('/https://secure.gravatar.com/'))
        return null
      else
        return this.reviewAvatar
    },

  },
  created: function(){
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  },
  methods: {
    logout: function() {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({name:'Login'})
    }
  },
}
</script>

<style>
/* ------------------------------------------------------------
/* Navigation
/* ------------------------------------------------------------ */

header {
  display: block;
  
}
header[role="banner"] {
    position: sticky;
    position: -webkit-sticky;
    top: 0;
    z-index: 999;
}

nav {
  background-image: url('../assets/nav_back.jpg');
  background-size: cover;
  background-size: 70%;
  padding: 0.5rem;
  text-align: center;
  min-width: none;
  
}
nav a.logo {
    text-transform: uppercase;
    font-size: 18px;
    width: 100%;
    
    display: inline-block;
}

nav a {
  font-weight: 700;
  font-size: 15px;
  color: rgb(253, 230, 188);
  text-decoration: none;
  display: inline-block;
  margin: auto 0;
  padding: 0;
  text-align: center;
  width: 23.5%;
  min-width: 63px;
  text-shadow:1px 1px 1px #936c35;
}

nav a:hover{
  color: #936c35;
}

nav a.router-link-exact-active .effect{
  font-size: 17px;
  padding-bottom: 3px;
  border-bottom: 2px dotted rgba(255, 255, 255, 0.35);
}

@media (min-width: 500px) {
  nav {
    padding: 1rem 1.5rem calc(1rem - 2px) 1.5rem;
  }

  nav div {
    margin: auto;
    display: flex;
    justify-content: center;
    max-width: 60rem;
  }

  nav a {
    font-size: 15px;

  }

  nav a:nth-child(1) {
    font-size: 20px;
    width: 40%;
    min-width: 200px;
    margin: auto;
    order: 3;
  }

  nav a:nth-child(2) {
    order: 1;
  }

  nav a:nth-child(3) {
    order: 2;
  }
  nav a:nth-child(4) {
    order: 4;
  }

  nav a:nth-child(5) {
    order: 5;
  }
}

</style>