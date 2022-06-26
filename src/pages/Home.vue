<template>
    <main>
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
                        <Analise/>
                      </v-card-actions>
                    </v-card>
                  </v-col>
                </v-row>
              </v-card-text>

              <!-- <v-card-text>
                <v-row>
                  <v-col>
                    <v-card
                      max-width="100%"
                    >
                      <v-card-actions>
                        <div class="container text-center">
                          <GoogleChart/>
                        </div>
                      </v-card-actions>
                    </v-card>
                  </v-col>
                </v-row>
              </v-card-text> -->

            </v-card>

          </div>
      </section>
    </main>
</template>

<script>
import api from '@/services/api.js'
import Analise from '@/components/analise/Analise.vue'

export default {
  name: 'cHome',
  components: {
    Analise
  },
  data: () => ({
    reveal: false,
    dataValues: {
      forno: 0,
      esteira: 0,
      flowpack: 0
    }
  }),
  mounted () {
    this.Carregar('forno/c', 'forno')
    this.Carregar('esteira/c', 'esteira')
    this.Carregar('flowpack/c', 'flowpack')
  },
  methods: {
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

.v-card--reveal {
      bottom: 0;
      opacity: 1 !important;
      position: absolute;
      width: 100%;
    }
</style>
