import Vue from 'vue'
import VueRouter from 'vue-router'
import cHome from '@/pages/Home'
import cSobre from '@/pages/Sobre'
import cReportEsteira from '@/pages/relatorios/Esteira'
import cReportForno from '@/pages/relatorios/Forno'
import cReportFlowpack from '@/pages/relatorios/Flowpack'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: cHome
  },
  {
    path: '/report-esteira',
    name: 'report-esteira',
    component: cReportEsteira
  },
  {
    path: '/report-forno',
    name: 'report-forno',
    component: cReportForno
  },
  {
    path: '/report-flowpack',
    name: 'report-flowpack',
    component: cReportFlowpack
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
