<template>
  <footer>
      <div class="text-bottom">projetointegrador.com.br</div>
  </footer>
</template>

<script>
import api from '@/services/api.js'

export default {
  name: 'cFooter',
  data () {
    return {
      socialLinks: []
    }
  },
  mounted () {
    api.get('/social-links.json').then((response) => {
      this.socialLinks = response.data
    })
  }
}
</script>

<style scoped>
footer {
  background-color: var(--color-background-nav);
  width: 100%;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.text-bottom {
    color: var(--color-text-light);
    font-size: 18px;
    margin-top: 20px;
}

.socialLink {
  border: 1px solid var(--color-text-light);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  margin: 0 10px;
}
.socialLink img {
  width: 20px;
}
</style>
