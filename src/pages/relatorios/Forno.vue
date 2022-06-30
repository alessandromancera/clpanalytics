<template>
  <div id="app" app-data="true">
  <main>
    <section class="container">
      <h2>Relatório - Forno</h2>
      <div id="forno">

        <!-- Início detalhes -->
        <v-dialog v-model="modal.detalhes" transition="dialog-bottom-transition">
          <v-card>
            <v-toolbar color="#1e88e5" dark >
              <v-icon class="ml-2" >
                mdi mdi-stove
              </v-icon>
              <v-toolbar-title class="pl-4" >
                Detalhes do Forno {{this.modal.selecion}}
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
                        :loading="carregando"
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

        <v-card max-width="100%" >
          <v-data-table
            dense
            fixed-header
            height="63vh"
            :headers="headers"
            :items="desserts"
            :items-per-page="10"
            class="elevation-1"
            :loading="carregando"
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
        </v-card>
      </div>
    </section>
  </main>
</div>
</template>

<script>
import api from '@/services/api.js'
import moment from 'moment'

export default {
  name: 'cReportForno',
  data: () => ({
    modal: {
      detalhes: false,
      selecion: ''
    },
    itensdetalhes: [],
    headers: [
      { text: '#', value: 'id', sortable: false },
      { text: 'Temperatura Z1', value: 'temperatura_z1', sortable: false },
      { text: 'Temperatura Z2', value: 'temperatura_z2', sortable: false },
      { text: 'Temperatura Z3', value: 'temperatura_z3', sortable: false },
      { text: 'Temperatura Z4', value: 'temperatura_z4', sortable: false },
      { text: 'Temperatura Z5', value: 'temperatura_z5', sortable: false },
      { text: 'Velocidade Esteira', value: 'velocidade_esteira', sortable: false },
      { text: 'Data Hora', value: 'timestamp', sortable: false, formatter: (x) => (x ? moment(x).format('DD/MM/yyyy HH:mm:ss') : null) },
      { text: 'Detalhes', value: 'details', sortable: false }
    ],
    headersdetalhes: [
      { text: '#', value: 'id', sortable: false },
      { text: 'Temp. Z1', value: 'temperatura_z1', sortable: false },
      { text: 'Temp. Z2', value: 'temperatura_z2', sortable: false },
      { text: 'Temp. Z3', value: 'temperatura_z3', sortable: false },
      { text: 'Temp. Z4', value: 'temperatura_z4', sortable: false },
      { text: 'Temp. Z5', value: 'temperatura_z5', sortable: false },
      { text: 'Vel. Esteira', value: 'velocidade_esteira', sortable: false },
      { text: 'Pid Z1', value: 'pid_z1', sortable: false },
      { text: 'Pid Z2', value: 'pid_z2', sortable: false },
      { text: 'Pid Z3', value: 'pid_z3', sortable: false },
      { text: 'Pid Z4', value: 'pid_z4', sortable: false },
      { text: 'Pid Z5', value: 'pid_z5', sortable: false },
      { text: 'Corrente Motor', value: 'corrente_motor', sortable: false },
      { text: 'Data Hora', value: 'timestamp', sortable: false, formatter: (x) => (x ? moment(x).format('DD/MM/yyyy HH:mm:ss') : null) }
    ],
    desserts: [],
    carregando: false
  }),
  mounted () {
    document.body.setAttribute('data-app', true)
    this.Carregar('forno')
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
        this.carregando = true
        api.get(url)
          .then((response) => {
            this.desserts = response.data.rows
          })
          .catch((error) => {
            console.log('Error')
            console.log(error)
          })
          .finally(() => console.log('Finalizado'), this.carregando = false)
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
