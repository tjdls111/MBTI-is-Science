import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieList from '../views/movies/MovieList.vue'
import Login from '../views/accounts/Login.vue'
import Signup from '../views/accounts/Signup.vue'
import Profile from '../views/Profile.vue'
import MbtiTest from '../views/MbtiTest.vue'
import MbtiTestResult from '../views/MbtiTestResult.vue'
import ArticleList from '../views/articles/ArticleList.vue'
import ArticleCreate from '../views/articles/ArticleCreate.vue'
import ArticleDetail from '../views/articles/ArticleDetail.vue'
import ArticleSearchList from '../views/articles/ArticleSearchList.vue'
import MovieDetail from '../views/movies/MovieDetail.vue'
import MovieSearchList from '../views/movies/MovieSearchList.vue'
import Test from '@/components/test.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/mbti-test',
    name: 'MbtiTest',
    component: MbtiTest
  },
  {
    path: '/mbti-test-result',
    name: 'MbtiTestResult',
    component: MbtiTestResult,
    props: true,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    props: true
  },
  {
    path: '/articles/article-list',
    name: 'ArticleList',
    component: ArticleList
  },
  {
    path: '/articles/create',
    name: 'ArticleCreate',
    component: ArticleCreate
  },
  {
    path: '/articles/detail',
    name: 'ArticleDetail',
    component: ArticleDetail,
    props: true
  },
  {
    path: '/articles/search',
    name: 'ArticleSearchList',
    component: ArticleSearchList
  },
  {
    path: '/movies/detail',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true
  },
  {
    path:'/movies/search',
    name:'MovieSearchList',
    component: MovieSearchList,
    
  },
  {
    path:'/test',
    name: 'Test',
    component: Test,
  }

]

const router = new VueRouter({
  mode: 'history',
  // 스크롤 복구 함수
  scrollBehavior() {
    return { x: 0, y: 0 } 
  },
  base: process.env.BASE_URL,
  routes
})

export default router
