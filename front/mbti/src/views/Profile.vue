.<template>
  <div>
    <banner></banner>
    <div class="container mt-4" style="margin-bottom:80px;">
      <h1 class="my-5 fw-bold">🔍 {{user}}'s Profile</h1>
      <!-- profile 파트 -->
      <div class="profile d-flex row align-items-center">
        <!-- avatar 파트 -->
        <div class="profile-img col-5 d-flex flex-column align-items-center">
          <img v-if="selected_avatar" class="selected-img" :src="require(`@/assets/profile_img${selected_avatar}.gif`)" alt="profile image">
          <img v-else class="selected-img" src="@/assets/profile_img1.gif" alt="profile image">

            <b-form @submit="changeProfile" inline v-if="username === user" class="">
              <label class="mr-sm-2 d-block my-1" >Selcet Avatar</label>
              <b-form-select v-model="selected_avatar" :options="img_options" size="sm" class="me-3 align-middle"></b-form-select>
              <b-button @click="changeProfile" variant="warning" size="sm">Save</b-button>
            </b-form>

        </div>
        
        <!-- Profile 기본 정보 -->
        <div class="profile-base col-7">
          <div class="fs-3">
            My username is <span class="fw-bold border-bottom">{{user}}</span>.
          </div>
          <h3 class="fs-4" v-if="mbti !== 'IDKW'">My MBTI is <span class="text-warning fw-bold">"{{mbti}}"</span>.</h3>
          <!-- 테스트 하러 가기 버튼 만들기 -->
          <h3 v-else>I don't know my mbti... </h3>
          <p class="fw-bold"> followings: <span class="text-warning">{{following_cnt}}</span> | followers: <span class="text-warning">{{follower_cnt}}</span> </p>
          <hr>
          <div v-if="username !== user">
            <span class="fw-bold" v-if ="is_followed === 'false'"><p class="mb-0"> Follow Me!</p><b-button 
                variant=warning
                @click="follow"
                size="md"
                class="mx-2 text-light fw-bold"
            > follow </b-button></span>
            <span class="fw-bold" v-else><p class="mb-0"> Don't Unfollow Me! T.T</p><b-button 
                variant=warning
                @click="follow"
                size="md"
                class="mx-2 text-light fw-bold"
            > unfollow </b-button></span>
          </div>
          
          <div v-else>
            <p class="fw-bold "> Account management</p>
            <span><b-button 
              class="mx-2"

              size="sm" 
              @click="account_delete"
              >Account Delete</b-button></span>
            <span><b-button 
              class="mx-2"

              size="sm" 
              @click="account_update"
              >Account Update</b-button></span>
          </div>
        </div>
      </div>
      
      <!-- articles 파트 -->
      <h1 class="my-5 text-center">📂 {{user}}'s Articles</h1>
      <div class="my-5">
        <div class="articles row" v-if="username === user">

          <div class="myPicks col-6 article-border-bottom">
            <h2 class="profile-article-title">{{user}}'s Picks</h2>
            <p class="at text-end">total: {{picks_count}}</p>
            <ul class="profile-article-ul">
              <li class="profile-article-li" v-for="(pick, pick_idx) in picks" :key = "pick.pk">
                <router-link :to="{name: 'MovieDetail', query:{data: JSON.stringify({ movieId : `${pick.pk}`})}}"><strong>{{ pick_idx + 1 }} | </strong> {{pick.title}} </router-link>  
                <hr class="m-0">
              </li>
            </ul>
            <div v-if="picks_count >= 7" class="text-center text-secondary">... + {{ picks_count - 8 }}</div>
          </div>
          <div class="myBooks col-6 article-border-left article-border-bottom">
            <h2 class="profile-article-title">{{user}}'s Bookmarks</h2>
            <p class="at text-end">total: {{bookmarks_count}}</p>
            <ul class="profile-article-ul">
              <li class="profile-article-li" v-for="(bookmark, bookmark_idx) in bookmarks" :key = "bookmark.pk">
                <router-link :to="{name: 'ArticleDetail', query:{data: JSON.stringify({ articleId:`${bookmark.pk}`})}}"><strong>{{ bookmark_idx + 1 }} | </strong> [{{bookmark.title}}] / with movie '{{bookmark.movie.title}}' </router-link>      
                <hr class="m-0">
              </li>
            </ul>
            <div v-if="bookmarks_count >= 7" class="text-center text-secondary">... + {{ bookmarks_count - 8 }}</div>
          </div>
        </div>
        <div class="articles row">
          <div class="col-6 ">
            <h2 class="profile-article-title">{{user}}'s Reviews</h2>
            <p class="at text-end">total: {{article_count}}</p>
            <ul class="profile-article-ul ">
              <li class="profile-article-li" v-for="(article, article_idx) in articles" :key = "article.pk">
                <router-link :to="{name: 'ArticleDetail', query:{data: JSON.stringify({article:`${article}`, articleId:`${article.pk}`})}}"><strong>{{ article_idx + 1 }} | </strong>  [{{article.title}}] / with movie '{{article.movie.title}}' </router-link>      
                <hr class="m-0">
              </li>
            </ul>
            <div v-if="article_count >= 7" class="text-center text-secondary">... + {{ article_count - 8 }}</div>
          </div>
          <div class="col-6 article-border-left">
            <h2 class="profile-article-title">{{user}}'s Comments</h2>
            <p class="at text-end">total: {{comment_count}}</p>
            <ul class="profile-article-ul">
              <li class="profile-article-li" v-for="(comment, comment_idx) in comments" :key = "comment.pk">
                <router-link :to="{name: 'ArticleDetail', query:{data: JSON.stringify({ article : `${comment.article}`, articleId:`${comment.article.id}`})}}"> 
                  <strong>{{ comment_idx + 1 }} | </strong>  [{{comment.content}}] / with article '{{comment.article.title}}'   
                </router-link> 
                <hr class="m-0">
              </li>
            </ul>
            <div v-if="comment_count >= 7" class="text-center text-secondary">... + {{ comment_count - 8 }}</div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import Banner from '@/components/Banner'
import axios from 'axios'

import {mapState} from 'vuex'

export default {
  name: 'Profile',
  components: {
    Banner,
  },

  data:function(){
    return {
      user: null,
      profile :null,
      mbti:null,
      articles:null,
      comments:null,
      bookmarks:null,
      picks:null,
      is_followed : null,
      follower_cnt : null,
      following_cnt: null,
      uploadedImg: null,
      selected_avatar: null,
      bookmarks_count: null,
      picks_count: null,
      comment_count: null,
      article_count: null,
      img_options: [{value: 0, text: 'Select..'}, {value: 1, text: 'cookie'}, {value: 2, text: 'rudolf'}, {value: 3, text: 'snowman'},{value: 4, text: 'rudolf boy'},{value: 5, text: 'santa'}, {value: 6, text: 'fairy'},{value: 7, text: 'santa girl'}],
    }
  },
  computed: {
    ...mapState([
      'username', 
      'userMbti'
    ]),
    },
  mounted() {
    this.user = JSON.parse(this.$route.query.data).user
  },  
  methods:{
    getProfile: function(){
      axios({
        method:'get',
        url:`https://mbti.link/accounts/${this.user}/`
      })
        .then(res=>{
          // console.log(res);
          const tmp = res.data
          this.profile = tmp
          this.mbti = tmp.mbti
          this.articles = tmp.article_set
          this.article_count = tmp.article_count
          this.comments = tmp.comment_set
          this.comment_count = tmp.comment_count
          this.bookmarks = tmp.bookmarked_articles
          this.bookmarks_count = tmp.bookmarked_articles_count
          this.picks = tmp.picked_movies
          this.picks_count = tmp.picked_movies_count
          this.selected_avatar= tmp.poster_number
        })
        .catch(err=>{
          console.log(err);
        })
    },
    account_delete: function(){
      axios({
        method:'delete',
        url:`https://mbti.link/accounts/`,
        headers: this.$store.state.config
      })
        .then((res)=>{
          // console.log(res)
          localStorage.removeItem('jwt', res.data.token)
          this.$router.push({name:'MovieList'})

        })
        .catch(err=>{
          console.log(err);
        })
    },
    account_update: function(){
      this.$router.push({name:'Signup', 
        query: {data: JSON.stringify({ 
          username : `${this.username}`,
          mbti : `${this.userMbti}`,     
        })}})
    },
    follow: function(){
      this.$store.dispatch('SetToken')

      axios({
        method:'post',
        url:`https://mbti.link/accounts/${this.user}/follow/`,
        headers: this.$store.state.config
      })
        .then(()=>{

          if (this.is_followed == 'false'){
            this.is_followed = 'true'
            this.follower_cnt = this.follower_cnt + 1
          }
          else {
            this.is_followed = 'false'
            this.follower_cnt = this.follower_cnt - 1
          }
        })
        .catch(err=>{
          console.log(err);
        })
    },

    changeProfile: function(){
      axios({
        method:'post',
        url:`https://mbti.link/accounts/pick_profile/`,
        headers: this.$store.state.config,
        data: {
          "poster_number": this.selected_avatar,
        }
      })
        .then(()=>{
          console.log(this.selected_avatar)
          this.$store.dispatch("getProfileNum", this.selected_avatar)
        })
        .catch(err=>{
          console.log(err);
        })

    }
  },

  created: function(){
    // console.log( JSON.parse(this.$route.query.data).user)
    this.user = JSON.parse(this.$route.query.data).user
    this.getProfile()

    // 이용자가 이 유저를 팔로우 했는지?
    axios({
      method:'get',
      url:`https://mbti.link/accounts/${this.user}/is_follow/`,
      headers: this.$store.state.config
    })
      .then(res=>{
        // console.log(res)
        this.is_followed = res.data.isFollow
        this.follower_cnt = res.data.follower_cnt
        this.following_cnt = res.data.following_cnt
      })
      .catch(err=>{
        console.log(err);
      })
  },

}
</script>

<style>
  h1 {
    margin: 20px;
  }
  .profile {
    color: white;
    background-color: rgb(42, 90, 65);
  }
  .profile-img{
    padding: 20px;
    background-color: #dc3545;
  }
  .selected-img{
    width: 90%;
    margin: 3px;
    /* border: 2px solid rgb(42, 90, 65); */
    clip-path: circle(50%);
  }
  .profile-base{
    display: flex;
    flex-direction: column;
    line-height: 2.5;
  }
  .article-border-left {
    border-left: 1px dashed rgb(42, 90, 65);
  }
  .article-border-bottom {
    border-bottom: 1px dashed rgb(42, 90, 65);
  }
  .articles{
    text-align: left;
  }
  .profile-article-title{
    padding: 2%;
    text-align: center;
    font-size: 23px;
    font-weight: 600;
    color: rgba(0, 0, 0, 0.65);
  }
  .profile-article-ul{
    padding: 2%;
    overflow: hidden;
    max-height: 243px;
  }
  .profile-article-li{
    overflow: hidden;
    line-height: 2;
    white-space: nowrap;
    text-overflow: ellipsis;
    font-size: 14px;
  }
  .profile-article-li a{
    text-decoration: none;
    color: grey;
    transition: 0.2s all ease;
    border-radius: 2px;
    padding: 2px;
  }
  .profile-article-li a:hover{
    color: white;
    background-color: #dc3545;
  }
</style>