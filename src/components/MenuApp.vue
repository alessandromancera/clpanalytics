<template>
<div class="container" v-bind:style="styleObject">
  <nav class="navbar navbar-expand-lg">
    <a class="navbar-brand" href="/">CLP Analytics</a>
    <div>
      <v-btn depressed color="primary" icon @click="toggleDarkMode">
        <v-icon>mdi-theme-light-dark</v-icon>
      </v-btn>
    </div>
    <!-- <div>
      <v-switch
        @change="toggleDarkMode"
        :label="`${switchLabel}`"
        v-model="darkMode"
        inset
        input-value="true"
        :value="darkMode"
      ></v-switch>
    </div> -->
    <div>
      <v-btn depressed color="primary" icon @click="toggleFontUp" @change="toggleFontUp">
        <v-icon>mdi-format-font-size-increase</v-icon>
      </v-btn>
      <v-btn depressed color="primary" icon @click="toggleFontDown">
        <v-icon>mdi-format-font-size-decrease</v-icon>
      </v-btn>
    </div>

    <button class="navbar-toggler " type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Alterna navegação">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Relatórios
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            <a class="dropdown-item" href="/report-esteira">Esteira</a>
            <a class="dropdown-item" href="/report-forno">Forno</a>
            <a class="dropdown-item" href="/report-flowpack">Flowpack</a>
          </div>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/about">Sobre</a>
        </li>
      </ul>
    </div>
  </nav>
</div>
</template>

<script>

export default {
  name: 'cMenuApp',
  data () {
    return {
      dropdown: false,
      styleObject: {
        fontSize: '1.25rem'
      }
    }
  },
  methods: {
    toggleDarkMode: function () {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
    },
    toggleFontUp: function () {
      this.$vuetify.theme.fontSize = this.$vuetify.theme.fontSize + 0.25
      this.styleObject.fontSize = this.$vuetify.theme.fontSize + 'rem'
    },
    toggleFontDown: function () {
      if (this.$vuetify.theme.fontSize > 1.5) {
        this.$vuetify.theme.fontSize = this.$vuetify.theme.fontSize - 0.25
      } else {
        this.$vuetify.theme.fontSize = 1.25
      }
      this.styleObject.fontSize = this.$vuetify.theme.fontSize + 'rem'
    }
  },
  mounted () {
    // this.toggleDarkMode()
  },
  computed: {
    switchLabel: function () {
      return this.$vuetify.theme.dark ? 'Claro' : 'Escuro'
    },
    modeDark: function () {
      return this.$vuetify.theme.dark ? 'dark' : 'light'
    },
    darkMode: function () {
      return this.$vuetify.theme.dark
    },
    toggleFontSize: function () {
      return this.$vuetify.theme.fontSize
    }
  }
}
</script>

<style scoped>
nav {
    display: flex;
    justify-content: space-between;
    height: 60px;
    color: var(--color-text-light);
  }

  a {
    background-color: var(--color-background-nav);
    color: #fff;
  }

  .dropdown-menu {
    background-color: var(--color-background-nav);
    z-index: 999;
    position: relative;
  }

  .navbar-toggler-icon {
    background-color: #fff;
  }
</style>
