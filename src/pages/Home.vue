<template>
    <!-- <main> -->
      <section class="container">
        <h2>Dashboard</h2>
          <div>
            <v-card
              max-width="100%"
            >
              <v-card-text>
                <v-row>
                  <v-col>
                    <v-card
                      max-width="100%"
                    >
                      <v-card-text>
                        <div><h5>FORNO</h5></div>
                      </v-card-text>
                      <v-card-actions>
                        Lidos:
                        <v-spacer></v-spacer>
                        <h5>{{dataValues.forno}}</h5>
                      </v-card-actions>
                    </v-card>
                  </v-col>

                  <v-col>
                    <v-card
                      max-width="100%"
                    >
                      <v-card-text>
                        <div><h5>ESTEIRA</h5></div>
                      </v-card-text>
                      <v-card-actions>
                        Lidos:
                        <v-spacer></v-spacer>
                        <h5>{{dataValues.esteira}}</h5>
                      </v-card-actions>
                    </v-card>
                  </v-col>

                  <v-col>
                    <v-card
                      max-width="100%"
                    >
                      <v-card-text>
                        <div><h5>FLOWPACK</h5></div>
                      </v-card-text>
                      <v-card-actions>
                        Lidos:
                        <v-spacer></v-spacer>
                        <h5>{{dataValues.flowpack}}</h5>
                      </v-card-actions>
                    </v-card>
                  </v-col>
                </v-row>
              </v-card-text>

              <v-card-text>
                <v-row>
                  <v-col>
                    <v-card
                      max-width="100%"
                    >
                      <v-card-actions>
                        <div style="width:100%;">
                          <GChart
                            :settings="{packages: ['bar']}"
                            :data="chartData"
                            :options="chartOptions"
                            :createChart="(el, google) => new google.charts.Bar(el)"
                            @ready="onChartReady"
                          />
                        </div>
                      </v-card-actions>
                    </v-card>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </div>
      </section>
    <!-- </main> -->
</template>

<script>
import api from '@/services/api.js'
import { GChart } from 'vue-google-charts/legacy'

export default {
  name: 'cHome',
  components: {
    GChart
  },
  data: () => ({
    dataValues: {
      forno: 0,
      esteira: 0,
      flowpack: 0
    },
    chartsLib: null,
    chartData: [
      ['Equipamentos', 'Forno', 'Esteira', 'Flowpack'],
      ['Lidos', 94, 64, 89]
    ]
  }),
  computed: {
    chartOptions () {
      if (!this.chartsLib) return null
      return this.chartsLib.charts.Bar.convertOptions({
        chart: {
          title: 'Automação de forno na industria',
          subtitle: 'Leituras de fornos, esteiras e flowpack'
        },
        height: 252,
        bars: 'horizontal',
        colors: ['#1b9e77', '#d95f02', '#7570b3']
      })
    }
  },
  mounted () {
    this.Carregar('forno/c', 'forno')
    this.Carregar('esteira/c', 'esteira')
    this.Carregar('flowpack/c', 'flowpack')
  },
  methods: {
    onChartReady (chart, google) {
      this.chartsLib = google
    },
    Carregar (typeclick, key) {
      const url = `/${typeclick}`
      if (url !== '') {
        api.get(url)
          .then((response) => {
            if (key === 'forno') {
              this.dataValues.forno = response.data
            }
            if (key === 'esteira') {
              this.dataValues.esteira = response.data
            }
            if (key === 'flowpack') {
              this.dataValues.flowpack = response.data
            }
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
