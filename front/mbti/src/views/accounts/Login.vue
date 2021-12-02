<template>
  <div style=" min-height:600px;">
    <banner></banner>
      <h1 class="mt-5">Login</h1>
    <div class="container mt-4" id="form" style="margin-bottom:80px;">
      <b-form @reset="onReset" v-if="show">
        <b-form-group
          id="input-group-1"
          label="Username:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            autofocus="true"
            v-model="form.username"
            placeholder="Enter username"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Password:" label-for="input-2">
          <b-form-input 
            @keyup.enter = "login"
            id="input-2"
            v-model="form.password"
            type="password"
            placeholder="Enter password"
            aria-describedby="password-help-block"
            required
          ></b-form-input>
        </b-form-group>

        <b-button @click="login" variant="success">Login</b-button>
        
      </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Banner from '@/components/Banner'

export default {
  name: 'Login',
  components: {
    Banner,
  },
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      show: true
    }
  },
  methods: {
    login: function() {
      axios({
        method:'post',
        url:'http://15.165.76.174:80/accounts/api-token-auth/',
        data: this.form
      })
        .then((res)=>{
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$store.dispatch("getUserName", this.form.username)

          axios({
            method:'get',
            url:`http://15.165.76.174:80/accounts/${this.form.username}/`
          })
            .then(res=>{
              this.$store.dispatch("getProfileNum", res.data.poster_number)
            })
            .catch(err=>{
              console.log(err);
            })
          
          
          
          this.$router.push({name:'MovieList'})
          
        })
        .catch(err=>{
          console.log(err)
          alert(err)
        })
      // console.log(this.form)
    },
    
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.username = ''
      this.form.password = ''
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
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
  #input-group-1, #input-group-2, #input-group-3 {
    margin-bottom: 15px;
    font-weight: bold;
  }

</style>