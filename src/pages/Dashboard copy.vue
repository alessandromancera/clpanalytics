<template>
    <main>
      <section class="container">
        <h1>Dashboard</h1>
        <div class="d-flex">
          <Graficos/>
      </div>
      </section>
    </main>
</template>

<script>
import Graficos from '@/components/charts/Graficos.vue'

export default {
  name: 'cDashboard',
  components: {
    Graficos
  }
}
</script>

<style scoped>

main {
      align-items: center;
    }
</style>
