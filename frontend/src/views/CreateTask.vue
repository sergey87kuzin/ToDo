<template>
    <div>
        <h1> Создание задачи </h1>
        <input v-model="header" type="text" placeholder="заголовок" />
        <input v-model="text" type="text" placeholder="текст задачи" />
        <button @click="createUser">создать</button>
    </div>
</template>

<script>
import { baseUrl } from '../config'
export default {
    data() {
        return {
            header: '',
            text: ''
        }
    },
    methods: {
        createUser() {
            $.ajax({
                url: `${baseUrl}/api/v1/tasks/`,
                type: "POST",
                headers: {
                    'Authorization': 'Token ' + sessionStorage.getItem('auth_token')
                },
                data: {
                    header: this.header,
                    text: this.text
                },
                success: (response) => {
                    alert('задача создана)')
                    this.$router.push({name: 'Home'})
                },
                error: (response) => {
                    alert('что-то пошло не так')
                }
            })
        }
    }
}
</script>