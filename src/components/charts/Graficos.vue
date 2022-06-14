<template>
  <div class="chart">
    <!-- <Chart
      :chartData="chartData"
      :chartType="chartType"
    /> -->
    <div style="width: 800px; height: 600px;">
      <canvas id="revenue-chart"></canvas>
    </div>
  </div>
</template>

<script>
import Chart from '../Chart'
import api from '@/services/api.js'
const dataValues = []
const dataChart = {}

export default {
  name: 'GraficoEquipamentos',
  components: {
    // Chart
  },
  // data (dataValues) {
  //   return {
  //     chartType: 'pie',
  //     chartData: {
  //       labels: ['Forno', 'Esteira', 'Flowpack'],
  //       datasets: [
  //         {
  //           data: dataValues,
  //           backgroundColor: [
  //             'rgb(255, 99, 132)',
  //             'rgb(54, 162, 235)',
  //             'rgb(255, 205, 86)'
  //           ],
  //           hoverOffset: 4
  //         }
  //       ]
  //     }
  //   }
  // },
  mounted () {
    this.Carregar('forno/c')
    this.Carregar('esteira/c')
    this.Carregar('flowpack/c')

    const revenueChartData = {
      type: 'pie',
      data: {
        labels: ['Forno', 'Esteira', 'Flowpack'],
        data: dataValues,
        backgroundColor: [
          'rgb(255, 99, 132)',
          'rgb(54, 162, 235)',
          'rgb(255, 205, 86)'
        ],
        hoverOffset: 4
      }
    }
    const ctx = document.getElementById('revenue-chart')
    new Chart(ctx, this.revenueChartData)
  },
  methods: {
    Carregar (typeclick) {
      const url = `/${typeclick}`
      if (url !== '') {
        api.get(url)
          .then((response) => {
            dataValues.push(JSON.stringify(response.data))
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

<style>
</style>
