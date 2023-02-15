<template>
    <div>
        <div>
            <h1> Изменение задачи </h1>
            <input v-model="task.header" type="text" placeholder="header"/>
            <input v-model="task.text" type="text" placeholder="text"/>
            <button @click="updateTask">сохранить</button>
        </div>
    </div>
</template>

<script>
import { baseUrl } from '../config'
export default {
    props: {
        id: {type: String, required: true}
    },
    data() {
        return {
            task: '',
        }
    },
    computed: {
        initialHeader() {
            return this.task.header
        }
    },
    created() {
        this.getTask()
    },
    methods: {
        getTask() {
            $.ajax({
                url: `${baseUrl}/api/v1/tasks/${this.id}/`,
                type: 'GET',
                headers: {
                    'Authorization': 'Token ' + sessionStorage.getItem('auth_token')
                },
                success: (response) => {
                    this.task = response
                },
                error: (response) => {
                    console.log(response)
                }
            })
        },
        updateTask() {
            $.ajax({
                url: `${baseUrl}/api/v1/tasks/${this.id}/`,
                type: 'PUT',
                headers: {
                    'Authorization': 'Token ' + sessionStorage.getItem('auth_token')
                },
                data: {
                    header: this.task.header,
                    text: this.task.text
                },
                success: (response) => {
                    alert('изменено')
                    this.$router.push({name: 'Home'})
                },
                error: (response) => {
                    alert('не удалось изменить')
                    console.log(response)
                }
            })
        }
    }
}
</script>