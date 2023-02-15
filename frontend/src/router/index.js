import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {path: '/', name: 'Home', component: Home},
  {path: 
    '/signup/',
    name: 'Signup', 
    component: ()=>import('../views/Signup.vue')
  },
  {path: 
    '/signin/', 
    name: 'Signin', 
    component: ()=>import('../views/Signin.vue')
  },
  {path: 
    '/create_task/', 
    name: 'CreateTask', 
    component: ()=>import('../views/CreateTask.vue')
  },
  {path: 
      '/tasks/:id', 
      name: 'Task', 
      component: ()=>import('../views/Task.vue'),
      props: true
  },
  {path: 
    '/updatetasks/:id', 
    name: 'updateTask', 
    component: ()=>import('../views/Update.vue'),
    props: true
}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
