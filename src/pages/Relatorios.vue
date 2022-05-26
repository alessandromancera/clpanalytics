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
        <v-client-table
          :data="usersCollection"
          :options="tableOptions"
          :columns="tableColumns">
        </v-client-table>

        <vuetable ref="vuetable"
          :api-mode="false"
          :data="data"
          :fields="tableColumns"
          data-path="rows"
          pagination-path=""
        ></vuetable>
      </div>

    </section>
  </main>
</template>

<script>
import api from '@/services/api.js'
import Vuetable from 'vuetable-2'

export default {
  name: 'cReport',
  components: {
    Vuetable
  },
  data () {
    return {
      tableColumns: ['id', 'velocidade_rolo', 'velocidade_esteira', 'timestamp'],
      usersCollection: [],
      data: [],
      tableOptions: {
        headings: {
          id: 'ID',
          velocidade_rolo: 'Velocidade Rolo',
          velocidade_esteira: 'Velocidade Esteira',
          timestamp: 'Data Hora'
        }
        // sortable: ['id', 'timestamp'],
        // filterable: ['id', 'timestamp']
      }
    }
  },
  mounted () {},
  methods: {
    Carregar (typeclick) {
      const url = `/${typeclick}`
      if (url !== '') {
        api.get(url)
          .then((response) => {
            this.show_esteira = true
            this.data = JSON.stringify(response.data)
            this.usersCollection = JSON.stringify(response.data)
            console.log('usersCollection')
            console.log(this.usersCollection)
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
