<template>
    <div id=nav>
      <router-link to='/'>Home</router-link> |
      <!-- <router-link :to="{name: 'Signup'}">Sign up</router-link> |
      <router-link :to="{name: 'Signin'}">Sign in</router-link> | -->
      <router-link :to="{name: 'CreateTask'}">Create Task</router-link>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Navigate',
  created() {
    $.ajaxSetup({
      headers: {
        'Authorization': 'Token' + sessionStorage.getItem('auth_token')
      }
    });
  }
}
</script>