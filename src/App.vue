<template>
  <div id="app">
    <cHeader />
    <router-view path='$router.key' />
    <cFooter />
  </div>
</template>

<script>
import './styles/global.css'

import cHeader from './components/Header'
import cFooter from './components/Footer'

export default {
  name: 'App',
  components: {
    cHeader,
    cFooter
  }
}
</script>
