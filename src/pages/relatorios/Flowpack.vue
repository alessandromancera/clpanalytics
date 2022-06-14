<template>
  <main>
    <section class="container">
      <h2>Relatório - Flowpack</h2>
      <div id="flowpack">
        <v-card max-width="100%" >
          <v-data-table
              dense
              fixed-header
              height="63vh"
              :headers="headers"
              :items="desserts"
              :items-per-page="12"
              class="elevation-1"
              loading
              loading-text="Aguarde, carregando relatório..."
          >
          </v-data-table>
        </v-card>
      </div>
    </section>
  </main>
</template>

<script>
import api from '@/services/api.js'

export default {
  name: 'cReportFlowpack',
  data () {
    return {
      headers: [
        { text: '#', value: 'id', sortable: false },
        { text: 'Velocidade Maquina', value: 'velocidade_maquina', sortable: false },
        { text: 'Qde Produtos Embalados', value: 'quantidade_produtos_embalados', sortable: false },
        { text: 'Qquantidade Embalagens', value: 'quantidade_embalagens', sortable: false },
        { text: 'Posicao Figura', value: 'posicao_figura', sortable: false },
        { text: 'Data Hora', value: 'timestamp', sortable: false }
      ],
      desserts: []
    }
  },
  mounted () {
    document.body.setAttribute('data-app', true)
    this.Carregar('flowpack')
  },
  methods: {
    Carregar (typeclick) {
      const url = `/${typeclick}`
      if (url !== '') {
        api.get(url)
          .then((response) => {
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
