import Vue from 'vue'
import Router from 'vue-router'
import SearchApp from '@/components/SearchApp.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SearchApp',
      component: SearchApp
    }
  ]
})
