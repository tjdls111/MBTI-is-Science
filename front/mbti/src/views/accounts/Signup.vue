<template>
  <div>
    <banner></banner>
    <h1 v-if="isUpdate" class="mt-4">Account Update</h1>
    <h1 v-else class="mt-4">Signup</h1>

    <div class="container mt-4" id="form" style="margin-bottom:100px;">
      <b-form @submit="onReset" v-if="show">
        <b-form-group
          v-if="isUpdate"
          id="input-group-1"
          label="Username:"
          label-for="input-1"
          description="Username is disabled."
        >
          <b-form-input
            disabled
            id="input-1"
            autofocus
            v-model="form.username"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          v-else
          id="input-group-1"
          label="Username:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            autofocus
            :state="name_validation"
            v-model="form.username"
            placeholder="Enter username"
            type="username"
            required
            validated="true"
          ></b-form-input>
          <b-form-invalid-feedback :state="name_validation">
            Your username must be 5-12 characters long.
          </b-form-invalid-feedback>
          <b-form-valid-feedback :state="name_validation">
            Looks Good.
          </b-form-valid-feedback>
        </b-form-group>

        <b-form-group id="input-group-4" label="MBTI:" label-for="input-4">
          <b-form-select
            id="input-4"
            v-model="form.mbti"
            :options="mbties"
            required
          ></b-form-select>
        </b-form-group>

        <b-form-group id="input-group-2" label="Password:" label-for="input-2">
          <b-form-input
            id="input-2"
            type="password"
            v-model="form.password"
            placeholder="Enter password"
            aria-describedby="password-help-block"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="Password Confirmation:" label-for="input-3">
          <b-form-input
            id="input-3"
            type="password"
            :state="pwd_validation"
            v-model="form.passwordConfirmation"
            placeholder="Enter password one more"
            aria-describedby="password-help-block"
            required
            @keyup.enter="signup"
          ></b-form-input>
          <b-form-invalid-feedback :state="pwd_validation">
            Your password and password confirmation do not match.
          </b-form-invalid-feedback>
          <b-form-valid-feedback :state="pwd_validation">
          </b-form-valid-feedback>
        </b-form-group>
        
        <b-button v-if="isUpdate" @click="signup" variant="success">Update</b-button>
        <b-button v-else @click="signup" variant="success">Signup</b-button>
      </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Banner from '@/components/Banner'

export default {
  name: 'Signup',
  components: {
    Banner,
  },
  data() {
    return {
      form: {
        username: '',
        password: '',
        passwordConfirmation:'',
        mbti: null,
        isLogin: false,
        isUpdate : true,
      },
      mbties: [{ text: 'Select One', value: null },'ENTJ','ENTP','ENFJ','ENFP','ESTJ','ESTP','ESFJ','ESFP','INTJ','INTP','INFJ','INFP','ISTJ','ISTP','ISFJ','ISFP',{ text: "I don't know", value: 'IDKW' },],
      show: true
    }
  },
  methods: {
    signup: function () {
      if (this.$route.query.data){
      

        // 정보 수정
        axios({
          method:'put',
          url:`https://mbti.link/accounts/`,
          data: this.form,
          headers: this.$store.state.config
        })
          .then((res)=>{
            console.log(res)
            
            this.$router.push({name:'MovieList'})
  
          })
          .catch(err =>{
            console.log(err)
          })
      }
      // 회원가입
      else {
      axios({
        method:'post',
        url:'https://mbti.link/accounts/',
        data: this.form
      })
        .then(()=>{
        

            axios({
              method:'post',
              url:'https://mbti.link/accounts/api-token-auth/',
              data: {
                username: this.form.username,
                password: this.form.password
              }
            })
              .then((res)=>{
                // console.log(res)
                localStorage.setItem('jwt', res.data.token)
                this.$emit('login')
                this.$store.dispatch("getUserName", this.form.username)
                this.$router.push({name:'MovieList'})
              })
              .catch(err=>{
                console.log(err)
                alert(err)
              })
          
          // console.log(res)
          // localStorage.setItem('jwt', res.data.token )
          // this.$emit('login')
          // this.$store.dispatch("getUserName", this.form.username)
          // this.$router.push({name:'Login'})
        })
        .catch(err=>{
          console.log(err)
          alert(err)
        })
      console.log(this.form)
    }
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.username = ''
      this.form.password = ''
      this.form.passwordConfirmation = ''
      this.form.mbti = null
    },
    logout: function() {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({name:'Login'})
    }
  },
  computed: {
    name_validation() {
      return this.form.username.length > 4 && this.form.username.length < 13 && this.form.username != Number
    },
    pwd_validation() {
      return this.form.password == this.form.passwordConfirmation 
    }
  },
  created: function(){
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
    if (this.$route.query.data){
      const origin_account_data = JSON.parse(this.$route.query.data)
      this.form.username = origin_account_data.username
      this.form.mbti = origin_account_data.mbti
      this.isUpdate = true
    }
  },
}
</script>

<style>
  #form {
    width: 40%;
    min-width: 300px;
    margin: 70px auto;
    padding: 20px;
    border: 2px solid rgb(42, 90, 65);
    border-radius: 10px;
    background-color: rgb(252, 239, 214);
  }
  #input-group-1, #input-group-2, #input-group-3, #input-group-4 {
    margin-bottom: 15px;
    font-weight: bold;
  }

</style>