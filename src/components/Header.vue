<template>
  <header>
    <nav class="container">
      <a href="/" title="HOME - CLP Analytics" >CLP Analytics</a>
      <!-- <img
        v-on:click="openMenu"
        id="menu-button"
        src="../assets/menu.svg"
        alt="Abrir Menu"
      /> -->

      <!-- <div v-on:click="closeMenu" id="menu-overlay" v-if="menuActive"></div> -->
      <!-- <div id="menu-items" :class="{ active: menuActive }">
        <a><img id="menu-logo" src="" alt="logo" /></a>

        <ul class="menu">
          <li @mouseover="listTwo = true" @mouseleave="listTwo = false">
            <a href="/dashboard">Dashboard</a>
          </li>
          <li @mouseover="listThree = true" @mouseleave="listThree = false">
            <a href="#">Relatorios</a>
            <transition name="fade">
              <ul v-if="listThree" @click="listThree = false">
                <li><a href="/report-esteira">Esteira</a></li>
                <li><a href="/report-forno">Forno</a></li>
                <li><a href="/report-flowpack">Flowpack</a></li>
              </ul>
            </transition>
          </li>
          <li @mouseover="listFour = true" @mouseleave="listFour = false">
            <a href="/about">Sobre</a>
          </li>
        </ul>
      </div> -->
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
}

#logo {
  width: 130px;
}

#menu-button {
  width: 30px;
}

#menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 40%;
  height: 100vh;
  background-color: #000000;
  opacity: 0.8;
}

#menu-logo {
  widows: 110px;
  margin-top: 30px;
  margin-bottom: 10px;
}

#menu-items {
  position: fixed;
  top: 0;
  right: 0;
  width: 40%;
  height: 100vh;
  background-color: var(--color-background-nav);
  display: none;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

#menu-items.active {
  display: flex;
}

#items-menu {
  display: flex;
}

ul {
  list-style: none;
  text-align: center;
}

ul li {
  margin: 20px 0px;
}

ul li a {
  color: var(--color-text-light);
}

a {
  color: var(--color-text-light);
}

.menu {
  /* font: 14px/1.5 'Open Sans', sans-serif;
  font-weight: 600;
  margin: 0;
  padding: 0;
  list-style: none; */
}

.menu a {
  display: flex;
  padding: 20px;
  color: #fff;
  text-decoration: none;
}

.menu li {
  display:flexbox;
  float: left;
  position: relative;
  /* background: #222; */
  color: #fff;
  /* min-width: 180px; */
}

.menu li ul {
  display: block;
  position: absolute;
  border:1px solid #c0c0c0;
  width: 150px;
  height: 180px;
  margin: 0 10px;
  padding: 20;
  background: grey;
}

.menu li ul li {
/* background: beige; */
  transition: background .2s;
}

.menu li ul li:hover {
  /* background-color: #fff; */
  text-align: center;
  text-decoration-color: #000000;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .2s;
}
.fade-enter, .fade-leave-active {
  opacity: 0;
}

@media (min-width: 700px) {
  #menu-button,
  #menu-logo,
  #menu-overlay {
    display: none;
  }

  #menu-items {
    display: flex;
    position: static;
    height: 60px;
    width: auto;
  }

  ul {
    display: flex;
    height: 60px;
    align-items: center;
  }

  ul li {
    margin: 0px;
    margin-left: 20px;
  }
}
</style>
