<template>
    <main>
        <section class="container">
            <div class="main">
                <!-- <v-card
                    max-width="100%"
                >
                    <v-card-text>
                        <v-row
                            align="center"
                            justify="center"
                        >
                            <v-img
                                src="../assets/indus40.svg"
                                max-width="50%"
                                max-height="50%"
                                position="center"
                            >
                            </v-img>
                        </v-row>
                    </v-card-text>
                </v-card> -->
            </div>
        </section>
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

    .main {
        background-color: var(--color-background-home);
        justify-content: center;
        align-items: center;
    }

    .text-top {
        color: var(--color-text-light);
        font-size: 22px;
        margin-bottom: 20px;
        justify-content: center;
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
