<template>
    <div>
        <h1>home page</h1>
        <section v-if="tasks">
        <router-link 
            v-for="task in tasks"
            :key="task.id"
            :to="{name: 'Task', params:{id:task.id}}"
        > <h2>{{task.header}}</h2></router-link>
        </section>
    </div>
</template>

<script>
import { baseUrl } from '../config'
export default{
    name: 'Home',
    data() {
        return {
            tasks: ''
        }
    },
    created() {
        this.loadTasks()
    },
    methods: {
        loadTasks() {
            $.ajax({
                url: `${baseUrl}/api/v1/tasks/`,
                type: 'GET',
                headers: {
                    'Authorization': 'Token ' + sessionStorage.getItem('auth_token')
                },
                success: (response) => {
                    this.tasks = response
                },
                error: (response) => {
                    console.log(response)
                }
            })
        }
    }
}
</script>
