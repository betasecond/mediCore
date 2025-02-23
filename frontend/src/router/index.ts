import {createRouter, createWebHistory, RouteRecordRaw} from 'vue-router'
import LoginPageView from '../components/LoginPageView.vue'
import TestPageView from '../components/TestLoginPageView.vue'

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/login'
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPageView
    },
    {
        path: '/test',
        name: 'test',
        component: TestPageView
    },
    {
        path: '/:pathMatch(.*)*',
        redirect: '/login'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router