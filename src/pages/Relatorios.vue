<template>
  <main>
    <section class="container">
      <h1>Relatórios</h1>

      <div id="example-1">
        <button v-on:click="Carregar('esteira')">Esteira</button>
        <button v-on:click="Carregar('forno')">Forno</button>
        <button v-on:click="Carregar('flowpack')">Flowpack</button>
      </div>

      <div id="esteira">
        <v-data-table
            :headers="headers"
            :items="desserts"
            :items-per-page="20"
            show-expand
            class="elevation-1"
            loading
            loading-text="Selecione o Relatório..."
        >
          <template v-slot:expanded-item="{ item }">
            <v-data-table
                :headers="headersdetalhes"
                :items="item.detalhes"
                class="elevation-1"
            >
            </v-data-table>
          </template>
        </v-data-table>
      </div>
    </section>
  </main>
</template>

<script>
import api from '@/services/api.js'

export default {
  name: 'cReport',
  data () {
    return {
      headers: [
        { text: '#', value: 'id', sortable: false },
        { text: 'Velocidade Rolo', value: 'velocidade_rolo', sortable: false },
        { text: 'Velocidade Esteira', value: 'velocidade_esteira', sortable: false },
        { text: 'Data Hora', value: 'timestamp', sortable: false },
        { text: 'Detalhes', value: 'data-table-expand', sortable: false }
      ],
      headersdetalhes: [
        { text: '#', value: 'id', sortable: false },
        { text: 'Velocidade Rolo', value: 'velocidade_rolo', sortable: false },
        { text: 'Velocidade Esteira', value: 'velocidade_esteira', sortable: false },
        { text: 'Esteira', value: 'esteira_id', sortable: false }
      ],
      desserts: []
    }
  },
  mounted () {
    this.Carregar('esteira')
  },
  methods: {
    Carregar (typeclick) {
      const url = `/${typeclick}`
      if (url !== '') {
        api.get(url)
          .then((response) => {
            this.show_esteira = true
            this.desserts = response.data.rows
          })
          .catch((error) => {
            console.log('Error')
            console.log(error)
          })
          .finally(() => console.log('Finalizado'))
      }
    }
  }
}
</script>

<style scoped>
main {
  align-items: center;
}
</style>
