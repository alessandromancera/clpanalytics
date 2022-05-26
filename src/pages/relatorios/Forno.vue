<template>
  <main>
    <section class="container">
      <h1>Relatório - Forno</h1>
      <div id="forno">
        <v-data-table
            :headers="headers"
            :items="desserts"
            :items-per-page="20"
            show-expand
            class="elevation-1"
            loading
            loading-text="Aguarde, carregando relatório..."
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
  name: 'cReportForno',
  data () {
    return {
      headers: [
        { text: '#', value: 'id', sortable: false },
        { text: 'Temperatura Z1', value: 'temperatura_z1', sortable: false },
        { text: 'Temperatura Z2', value: 'temperatura_z2', sortable: false },
        { text: 'Temperatura Z3', value: 'temperatura_z3', sortable: false },
        { text: 'Temperatura Z4', value: 'temperatura_z4', sortable: false },
        { text: 'Temperatura Z5', value: 'temperatura_z5', sortable: false },
        { text: 'Velocidade Esteira', value: 'velocidade_esteira', sortable: false },
        { text: 'Data Hora', value: 'timestamp', sortable: false },
        { text: 'Detalhes', value: 'data-table-expand', sortable: false }
      ],
      headersdetalhes: [
        { text: '#', value: 'id', sortable: false },
        { text: 'Temperatura Z1', value: 'temperatura_z1', sortable: false },
        { text: 'Temperatura Z2', value: 'temperatura_z2', sortable: false },
        { text: 'Temperatura Z3', value: 'temperatura_z3', sortable: false },
        { text: 'Temperatura Z4', value: 'temperatura_z4', sortable: false },
        { text: 'Temperatura Z5', value: 'temperatura_z5', sortable: false },
        { text: 'Velocidade Esteira', value: 'velocidade_esteira', sortable: false },
        { text: 'Pid Z1', value: 'pid_z1', sortable: false },
        { text: 'Pid Z2', value: 'pid_z2', sortable: false },
        { text: 'Pid Z3', value: 'pid_z3', sortable: false },
        { text: 'Pid Z4', value: 'pid_z4', sortable: false },
        { text: 'Pid Z5', value: 'pid_z5', sortable: false },
        { text: 'Corrente Motor', value: 'corrente_motor', sortable: false },
        { text: 'Data Hora', value: 'timestamp', sortable: false },
        { text: 'Forno', value: 'forno_id', sortable: false }
      ],
      desserts: []
    }
  },
  mounted () {
    this.Carregar('forno')
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
