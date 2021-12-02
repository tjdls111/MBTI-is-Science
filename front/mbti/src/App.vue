<template>
  <div id="app">
    <!-- <iframe width="30%" height="auto" src="https://www.youtube.com/embed/YBkITBp_sJA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->
    <footer role="contentinfo" >
      <div class="d-flex px-3 justify-content-between align-items-center h-100">
        <div class="footer-part footer-icon">
          <a href="wwww.instagram.com" target="_blank"><b-icon icon="instagram"></b-icon></a>
          <a class="px-2" href="www.twitter.com" target="_blank"><b-icon icon="twitter" ></b-icon></a>
        </div>
        <div class="footer-part footer-logo">
          💡MBTI IS SCIENCE💡
        </div>
        <div class="footer-part footer-info">
          <a href="https://github.com/hoya0415" target="_blank">FRONT-END BY CHO_KAYE</a>  <br>
          <a href="https://github.com/tjdls111" target="_blank">BACK-END BY KIM_SEOIN</a> 
        </div>

      </div>
    </footer>
    <router-view @login="isLogin=true" />
  </div>
</template>

<script>
export default {
  name: 'App',
  components:{
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

/* ------------------------------------------------------------
/* General Declarations
/* ------------------------------------------------------------ */

* {
  box-sizing: border-box;
}

body {
  position: relative;
  margin: 0;
  padding: 0;
  margin-left: auto;
  margin-right: auto;
  background-color: #eeeeee !important;
  color: #212316;
  overflow-x: hidden !important;
  background-size: 100px 100px;
}

#app {
  font-family: 'Quicksand', 'Noto Sans KR', sans-serif;
  text-align: center;
  color: #2e2e2e;
  background-size: 100px 100px;
  position: absolute;
  width: 100%;
  /* height: calc(- 80px); */
}
.title-text {
  text-align: left;
  margin-bottom: 10px;
  margin-left: 0;
  font-weight: bold;
}

/* ------------------------------------------------------------
/* Footer
/* ------------------------------------------------------------ */
footer {
  /* line-height: 24px; */
  font-family: 'Quicksand', 'Noto Sans KR', sans-serif;
  border-top: 4px double rgb(42, 90, 65);
  color: rgb(42, 90, 65);
  /* background-color: rgba(42, 90, 65, 0.242); */
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 70px;
  /* z-index: 1000; */
  margin-top: 30px;
}
.footer-part{
  width: 20rem;
}
.footer-icon {
  text-align: left;
}
.footer-icon a{
  font-size: 13px;
  text-align: left;
  color: rgb(42, 90, 65);
}
.footer-icon a:hover {
  font-size: 17px;
  color: #936c35;
}
.footer-logo {
  font-weight: bold;
  font-size: 15px;
  
  }
.footer-info {
  text-align: right;
  font-size: 12px;
}
.footer-info a{
  font-weight: 500;
  color: rgb(42, 90, 65);
  font-size: 10px;
  text-decoration: none;
}
.footer-info a:hover{
  font-weight: 600;
  color: #936c35;
  font-size: 12px;
  text-decoration: none;
}

/*footer div {
  margin: 15px auto;
}

footer div.copyright {
  background: url("/assets/images/h-green.svg") 0 0.25rem no-repeat;
  background-size: 2.5rem 2.5rem;
  padding-left: 4rem;
}

body.project footer div.copyright {
  background-image: url("/assets/images/h.svg");
}

footer p {
  margin: 0;
  -webkit-font-smoothing: subpixel-antialiased;
  -moz-osx-font-smoothing: auto;
}

footer a {
  color: #212316;
  -webkit-font-smoothing: subpixel-antialiased;
  -moz-osx-font-smoothing: auto;
}

footer a:hover {
  color: #936c35;
}

@media (min-width: 800px) {
  footer {
    font-size: 14px;
  }

  footer > div {
    display: flex;
    align-items: baseline;
  }

  footer > div > div:first-child {
    width: 25%;
  }

  footer > div > div:last-child {
    width: 75%;
  }

  footer > div > div:nth-child(2) {
    display: flex;
    padding-right: 1rem;
  }

  h2 {
    font-size: 14px;
  }
}
@media (min-width: 1000px) {
  footer > div > div {
    width: 50% !important;
  }
} */
</style>
