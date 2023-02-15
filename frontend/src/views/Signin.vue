<template>
    <div>
        <h1> Регистрация </h1>
        <input v-model="login" type="text" placeholder="логин"/>
        <input v-model="password" type="password" placeholder="пароль"/>
        <button @click="sendLogIn">Зарегистрироваться</button>
    </div>
</template>

<script>
import { baseUrl } from '../config'
export default {
    data() {
        return {
            login: '',
            password: ''
        }
    },
    methods: {
        sendLogIn() {
            $.ajax({
                url: `${baseUrl}/api-token-auth/`,
                type: "POST",
                data: {
                    username: this.login,
                    password: this.password
                },
                success: (response) => {
                    alert('вы вошли)')
                    sessionStorage.setItem('auth_token', response.token)
                    this.$router.push({name: 'Home'})
                },
                error: (response) => {
                    if (response.status === 400) {
                        alert('неправильно введены данные')
                    }
                }
            })
        }
    }
}
</script>