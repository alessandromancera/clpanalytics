<template>
  <v-app v-bind:style="styleObject">
    <div id="app"
      :class="`${switchLabel}`"
      v-bind:style="styleObject"
    >
      <!-- :style="styleObject" -->
      <cHeader />
      <router-view path='$router.key' />
      <cFooter />
    </div>
  </v-app>
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
  },
  data () {
    return {
      styleObject: {
        fontSize: '1.25rem'
      }
    }
  },
  mounted () {
    this.styleObject.fontSize = this.$vuetify.theme.fontSize + 'rem'
  },
  computed: {
    switchLabel: function () {
      return this.$vuetify.theme.dark ? 'dark' : 'light'
    },
    toggleFontSize: function () {
      return this.$vuetify.theme.fontSize
    }
  }
}
</script>
