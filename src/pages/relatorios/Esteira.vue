<template>
  <main>
    <section class="container">
      <h2>Relatório - Esteira</h2>
      <div id="esteira">

        <!-- Início detalhes -->
        <v-dialog v-model="modal.detalhes" transition="dialog-bottom-transition">
          <v-card>
            <v-toolbar color="#1e88e5" dark >
              <v-icon class="ml-2" >
                mdi mdi-state-machine
              </v-icon>
              <v-toolbar-title class="pl-4" >
                Detalhes da Esteira {{this.modal.selecion}}
              </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-app-bar-nav-icon @click="modal.detalhes = false">
                <v-icon>mdi mdi-close-circle-outline</v-icon>
              </v-app-bar-nav-icon>
            </v-toolbar>
            <v-card-text>
                <v-col class="pt-6" >
                  <v-row>
                    <v-col cols="12" class="px-6">
                      <v-data-table
                          dense
                          fixed-header
                          height="65vh"
                          :headers="headersdetalhes"
                          :items="itensdetalhes"
                          :items-per-page="12"
                          class="elevation-1"
                          loading
                          loading-text="Aguarde, carregando detalhes..."
                          :footer-props="{
                            showFirstLastPage: true,
                            'items-per-page-all-text': 'Todos',
                            'items-per-page-options': [5, 10, 12, 15, -1],
                            'items-per-page-text':'Total por página: '
                          }"
                      >
                        <!--  -->
                        <template
                          v-for="header in headersdetalhes.filter((header) =>
                            header.hasOwnProperty('formatter')
                          )"
                          v-slot:[`item.${header.value}`]="{ value }"
                          >
                          {{ header.formatter(value) }}
                        </template>
                      </v-data-table>
                    </v-col>
                  </v-row>
                </v-col>
            </v-card-text>
          </v-card>
        </v-dialog>
        <!-- Fim Detalhes -->

        <!-- Inicio Principal -->
        <v-data-table
          dense
          fixed-header
          height="63vh"
          :headers="headers"
          :items="desserts"
          :items-per-page="10"
          class="elevation-1"
          loading
          loading-text="Aguarde, carregando relatório..."
          :footer-props="{
            showFirstLastPage: true,
            'items-per-page-all-text': 'Todos',
            'items-per-page-options': [5, 10, 12, 15, -1],
            'items-per-page-text':'Total por página: '
          }"
        >
            <template #[`item.details`]="{ item }">
              <v-app-bar-nav-icon @click="Detalhes(item)">
                <v-icon>mdi mdi-archive-eye</v-icon>
              </v-app-bar-nav-icon>
            </template>
            <!--  -->
            <template
              v-for="header in headers.filter((header) =>
                header.hasOwnProperty('formatter')
              )"
              v-slot:[`item.${header.value}`]="{ value }"
              >
              {{ header.formatter(value) }}
            </template>
        </v-data-table>
        <!-- Fim Principal -->
      </div>
    </section>
  </main>
</template>

<script>
import api from '@/services/api.js'
import moment from 'moment'

export default {
  name: 'cReportEsteira',
  data () {
    return {
      headers: [
        { text: '#', value: 'id', sortable: false },
        { text: 'Velocidade Rolo', value: 'velocidade_rolo', sortable: false },
        { text: 'Velocidade Esteira', value: 'velocidade_esteira', sortable: false },
        { text: 'Data Hora', value: 'timestamp', sortable: false, formatter: (x) => (x ? moment(x).format('DD/MM/yyyy HH:mm:ss') : null) },
        { text: 'Detalhes', value: 'details', sortable: false }
      ],
      headersdetalhes: [
        { text: '#', value: 'id', sortable: false },
        { text: 'Velocidade Rolo', value: 'velocidade_rolo', sortable: false },
        { text: 'Velocidade Esteira', value: 'velocidade_esteira', sortable: false },
        { text: 'Data Hora', value: 'timestamp', sortable: false, formatter: (x) => (x ? moment(x).format('DD/MM/yyyy HH:mm:ss') : null) }
      ],
      modal: {
        detalhes: false,
        selecion: ''
      },
      desserts: []
    }
  },
  mounted () {
    document.body.setAttribute('data-app', true)
    this.Carregar('esteira')
  },
  methods: {
    Detalhes (item) {
      this.modal.detalhes = true
      this.modal.selecion = item.id
      this.itensdetalhes = item.detalhes
    },
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
