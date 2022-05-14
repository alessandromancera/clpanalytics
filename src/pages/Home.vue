<template>
    <main>
        <div class="text-top">CLP Analytics</div>

        <a href="/" target="_blank">
            <img src="../assets/clp-Indus40.svg" alt="Projeto Integrador" id="subscrive">
        </a>
        <!-- <div class="text-bottom">projetointegrador.com.br</div> -->

    </main>
</template>

<script>
export default {
  name: 'cHome'
}
</script>

<style scoped>
    main {
        background-color: var(--color-background-home);
        justify-content: center;
        align-items: center;
    }

    .text-top {
        color: var(--color-text-light);
        font-size: 22px;
        margin-bottom: 20px;
    }

    #subscrive {
        width: 550px;
        height: 430px;
    }

    .text-bottom {
        color: var(--color-text-light);
        font-size: 18px;
        margin-top: 20px;
    }
</style>
