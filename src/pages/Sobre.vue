<template>
    <main>
      <section class="container">
        <h2>Sobre</h2>
          <div id="sobre">
            <v-row
              justify="center"
              align="center"
            >
            <v-card max-width="100%" >
              <v-card-text>
                <div>
                  <v-row>
                    <div
                      justify="center"
                      align="center"
                    >
                      <h4>CLP Analytics de automação de forno na indústria alimentícia</h4>
                    </div>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-card
                        max-width="100%"
                      >
                        <v-card-text>
                          <div
                            justify="center"
                            align="center"
                          ><h3>Utilizado neste projeto</h3></div>
                        </v-card-text>
                        <v-card-actions>
                          API - node.js - hospedado em https://www.heroku.com/<br />
                          Frontend - vue.js - hospedado em https://vercel.com/<br />
                          Banco de dados - MySql - hospedado em https://www.heroku.com/<br />
                          Análise e Gráficos - Python<br />
                          Versionamento Local - Git<br />
                          Versionamento Cloud - Github<br />
                        </v-card-actions>
                      </v-card>
                    </v-col>
                    <v-col>
                      <v-card
                        max-width="100%"
                      >
                        <v-card-text>
                          <div
                            justify="center"
                            align="center"
                          ><h3>Integrantes</h3></div>
                        </v-card-text>
                        <v-card-actions>
                          Alessandro Lima Mancera, 2008684<br />
                          Andre Luiz Felix Da Rosa, 2011349<br />
                          Carlos Alberto Guedes Golino, 1802881<br />
                          Durval Sproesser Neto, 2000799<br />
                          Edson Inácio De Lima, 2004603<br />
                          Maxuel Araujo Ferreira Da Silva, 2013257<br />
                          Rafael Montoro Da Silva, 2000952<br />
                          Rogerio Rodella, 2009359
                        </v-card-actions>
                      </v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-card max-width="100%" >
                        <v-card-text>
                          <div
                            justify="center"
                            align="center"
                          ><h6>
                            Projeto Integrador em Computação II - PJI240 - Turma 001<br />
                            Univesp - Universidade Virtual do Estado de São Paulo - Pólo Marília-SP<br />
                          </h6></div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                </div>
              </v-card-text>
            </v-card>
            </v-row>
          </div>
      </section>
    </main>
</template>

<script>

export default {
  name: 'cSobre',
  data () {
    return {
      about: ''
    }
  }
}
</script>

<style scoped>

main {
        align-items: center;
    }

.about {
  margin-bottom: 40px;
  display: flex;
}
</style>
