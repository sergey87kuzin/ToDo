<script setup>
</script>

<template>
  <div>
    <div v-if="auth"><TheNavigation/></div>
    <div v-if="!auth"><NotAuthNav/></div>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import TheNavigation from './components/Navigate.vue'
import NotAuthNav from './components/NotAuthNav.vue'

export default {
  components: {
    TheNavigation,
    NotAuthNav
  },
  computed: {
      auth() {
          if (sessionStorage.getItem('auth_token')) {
              return true
          }
      }
  },
  watch: {
    $route (to, from) {
      console.log(from)
      if ('path' in from) {
        if(from.path === '/signin/') {
          window.location.reload()
        }
      }
    }
  }
  // created() {
  //   if (localStorage.getItem('auth_token')) {
  //     $.ajaxSetup({
  //       headers: {'Authorization': 'Token' + sessionStorage.getItem('auth_token')}
  //     });
  //   }
  // }
}
</script>