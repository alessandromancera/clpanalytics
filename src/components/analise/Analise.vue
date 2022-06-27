<template>
  <div class="container text-center">
    <h6><b>Análise</b></h6>
    <div>
      <GChart
        :settings="{packages: ['bar']}"
        :data="chartData"
        :options="chartOptions"
        :createChart="(el, google) => new google.charts.Bar(el)"
        @ready="onChartReady"
      />
    </div>
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts/legacy'

export default {
  name: 'cAnalise',
  components: {
    GChart
  },

}
</script>

<style>

</style>
