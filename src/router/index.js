import Vue from 'vue'
import VueRouter from 'vue-router'
import cHome from '@/pages/Home'
import cSobre from '@/pages/Sobre'
import cReport from '@/pages/Relatorios'
import cDashboard from '@/pages/Dashboard'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: cHome
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: cDashboard
  },
  {
    path: '/report',
    name: 'report',
    component: cReport
  },
  {
    path: '/about',
    name: 'about',
    component: cSobre
  }
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
