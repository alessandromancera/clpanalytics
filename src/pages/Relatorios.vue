<template>
    <main>
      <section class="container">
        <h1>Relatórios</h1>

        <div id="example-1">
          <button v-on:click="Carregar('esteira')">Esteira</button>
          <button v-on:click="Carregar('forno')">Forno</button>
          <button v-on:click="Carregar('flowpack')">Flowpack</button>
        </div>

      </section>

    </main>
</template>

<script>
import api from '@/services/api.js'

export default {
  name: 'cReport',
  data: () => ({
  }),
  mounted () {

  },
  methods: {
    Carregar (typeclick) {
      const url = `/${typeclick}`
      // alert(url)
      api.get(url)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log('Error')
          console.log(error)
        })
        .finally(() => console.log('Finalizado'))
    }
  }
}
</script>

<style scoped>

main {
      align-items: center;
    }
</style>
