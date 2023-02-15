<template>
    <div>
        <h1>some task</h1>
        <h1>{{ task.header }}</h1>
        <h2>{{ task.text }}</h2>
        <button @click="deleteTask">удалить</button>
        <button @click="updateTask">изменить</button>
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
            task: ''
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
        deleteTask() {
            $.ajax({
                url: `${baseUrl}/api/v1/tasks/${this.id}/`,
                type: 'DELETE',
                headers: {
                    'Authorization': 'Token ' + sessionStorage.getItem('auth_token')
                },
                success: (response) => {
                    alert('удалено')
                    this.$router.push({name: 'Home'})
                },
                error: (response) => {
                    alert('не удалось удалить')
                    console.log(response)
                }
            })
        },
        updateTask() {
            this.$router.push({name: 'updateTask', params:{id:this.task.id}})
        }
    }
}
</script>