<template>
    <div>
        <h1> Создание учетной записи </h1>
        <input v-model="login" type="text" placeholder="логин" />
        <input v-model="password" type="password" placeholder="пароль" />
        <button @click="createUser">создать</button>
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
        createUser() {
            $.ajax({
                url: `${baseUrl}/api/v1/users/`,
                type: "POST",
                data: {
                    username: this.login,
                    password: this.password
                },
                success: (response) => {
                    alert('пользователь создан)')
                    this.$router.push({name: 'Signin'})
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