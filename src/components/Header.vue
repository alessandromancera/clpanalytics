<template>
  <header>
    <nav class="container">
      <a href="/" title="HOME - CLP Analytics" >CLP Analytics</a>
      <cMenu />
    </nav>

  </header>
</template>

<script>
import cMenu from './MenuApp.vue'

export default {
  name: 'cHeader',
  components: {
    cMenu
  },
  data () {
    return {
      menuActive: false,
      listOne: false,
      listTwo: false,
      listThree: false,
      listFour: false
    }
  },
  methods: {
    openMenu: function () {
      this.menuActive = true
    },
    closeMenu: function () {
      this.menuActive = false
    }
  }
}
</script>

<style scoped>
header {
  background-color: var(--color-background-nav);
  width: 100%;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
}

nav {
  display: flex;
  justify-content: space-between;
  height: 60px;
  align-items: center;
  color: var(--color-text-light);
}
a {
  color: var(--color-text-light);
}
</style>
