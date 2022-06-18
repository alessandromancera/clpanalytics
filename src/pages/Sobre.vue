<template>
    <main>
      <section class="container">
        <h2>Sobre</h2>
          <div id="esteira">
            <v-card
              max-width="100%"
            >
              <v-card-text>
                <div>
                  <p>CLP Analytics de automação de forno na indústria alimentícia</p>
                  Através de consulta na API coletando os dados para análise e tomada de<br/>
                  decisões a partir do FrontEnd.<br/>
                  <br/>
                  Projeto Integrador em Computação II - PJI240 - Turma 001<br/>
                  Univesp - Universidade Virtual do Estado de São Paulo - Pólo Marília-SP<br/>
                  <br/>
                  Integrantes:-<br/>
                  Alessandro Lima Mancera, 2008684<br/>
                  Andre Luiz Felix Da Rosa, 2011349<br/>
                  Carlos Alberto Guedes Golino, 1802881<br/>
                  Durval Sproesser Neto, 2000799<br/>
                  Edson Inácio De Lima, 2004603<br/>
                  Maxuel Araujo Ferreira Da Silva, 2013257<br/>
                  Rafael Montoro Da Silva, 2000952<br/>
                  Rogerio Rodella, 2009359<br/>
                </div>
              </v-card-text>
            </v-card>
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
