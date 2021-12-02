import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    movies: [],
    moviesDetail: [],
    articles: [],
    articleDetail :[],
    username: null,
    config: null,
    userMbti: null,
    searchedMovies:[],
    searchedArticles: [],
    userProfileNum:0,
  },
  mutations: {
    LOAD_MOVIE_LIST : function(state, movies){
      state.movies = movies
    },
    LOAD_MOVIE_DETAIL_LIST : function(state, moviesDetail){
      // console.log(moviesDetail);
      state.moviesDetail = moviesDetail
    },
    LOAD_ARTICLE_DETAIL : function(state, articleDetail){
      state.articleDetail = articleDetail
    },
    LOAD_ARTICLE_LIST : function(state, articles){
      state.articles = articles
    }, 
    SET_TOKEN : function(state, config){
      state.config = config
    },

    GET_USER_NAME : function(state, username){
      state.username = username
    },
    
    GET_MBTI: function(state, mbti){
      state.userMbti = mbti
    },

    SEARCH_MOVIES: function(state, movies){
      state.searchedMovies = movies
    },
    SEARCH_ARTICLES: function(state, movies){
      state.searchedArticles = movies

    },
    GET_PROFILE_NUM: function(state, profileNum){
      state.userProfileNum = profileNum
    }    
  },
  actions: {
    LoadMovieList: function ({commit}) {
      axios({
        method: 'get',
        url: 'http://15.165.76.174:80/movies/'
      })
        .then((res)=>{
          // console.log(res);
          commit('LOAD_MOVIE_LIST', res.data)
        }) 
      
    },
    LoadMovieListBy: function ({commit}, sort_num) {
      axios({
        method: 'get',
        url: `http://15.165.76.174:80/movies/order_by/${sort_num}/`
      })
      .then((res)=>{
        console.log(res);
        commit('LOAD_MOVIE_LIST', res.data)
      })
  },
    LoadMovieDetailList: function ({ commit}, movieId) {
      axios({
        method: 'get',
        url: `http://15.165.76.174:80/movies/${movieId}/`
      })
        .then((res)=>{
          // console.log(res.data);
          commit('LOAD_MOVIE_DETAIL_LIST', res.data)
        })
      },
      LoadArticleList: function ({commit}) {
        axios({
          method: 'get',
          url: 'http://15.165.76.174:80/articles/'
        })
        .then((res)=>{
          // console.log(res);
          commit('LOAD_ARTICLE_LIST', res.data)
        })
    },
    LoadArticleListBy: function ({commit}, sort_num) {
      axios({
        method: 'get',
        url: `http://15.165.76.174:80/articles/sort/${sort_num}/`
      })
      .then((res)=>{
        console.log(res);
        commit('LOAD_ARTICLE_LIST', res.data)
      })
  },
    LoadArticleDetail: function ({commit}, articleId) {
      axios({
        method: 'get',
        url: `http://15.165.76.174:80/articles/${articleId}/`
      })
      .then((res)=>{
          console.log(res);
          commit('LOAD_ARTICLE_DETAIL', res.data)
        })
    },
    SetToken : function ({commit}){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      commit('SET_TOKEN', config)
    },

    getUserName : function({commit}, username){
      commit('GET_USER_NAME', username)
    },

    getMbti : function({commit}){

      axios({
        method: 'get',
        url: 'http://15.165.76.174:80/accounts/set_mbti/',
        headers: {"Authorization":`JWT ${localStorage.getItem('jwt')}`}
      })
        .then( (res) => {
          commit('GET_MBTI', res.data.mbti)
          
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    searchMovies: function({commit}, movies){
      commit('SEARCH_MOVIES', movies)
    },
    searchArticles: function({commit}, movies){
      commit('SEARCH_ARTICLES', movies)
    },
    getProfileNum: function({commit},profile_num){
      if (profile_num === 0){
        profile_num = 1
      }
      commit('GET_PROFILE_NUM', profile_num)
    }
  },
  modules: {
  }
})
