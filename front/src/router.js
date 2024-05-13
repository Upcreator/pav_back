import {createMemoryHistory, createRouter, createWebHistory} from 'vue-router'
import {useAuthStore} from "@/stores/authStore.js";


const routes = [
    {
        path: '/welcome',
        name: 'welcome',
        component: () => import('./views/Welcome.vue'),
    },
    {
        path: '/signup',
        name: 'signup',
        component: () => import('./views/SignUp.vue')
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('./views/Login.vue')
    },
    {
        path: '/',
        name: 'main',
        component: () => import('./views/Main.vue')
    },
]

const publicRoutes = [
    'welcome', 'login', 'signup'
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})


router.beforeEach((to, from, next) => {
    const authStore = useAuthStore()
    if (publicRoutes.includes(to.name)){
        if(to.name === 'login' || to.name === 'register'){
            authStore.getUser()
                .then(() => {
                    next({name: 'main'})
                })
                .catch(() => {
                    next()
                })
        }else{
            next()
        }

        return
    }
    if(!authStore.user){
        authStore.getUser()
            .then(() => {
                next()
            })
            .catch(() => {
                next({name: 'welcome'})
            })
    }else{
        next();
    }


})

export default router;

