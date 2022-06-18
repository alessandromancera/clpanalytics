<template>
  <header>
    <cMenu />
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
    align-items: center;
  }
</style>
