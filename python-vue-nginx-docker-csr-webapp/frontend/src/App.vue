<script>
    export default {
        computed: {
            routes() {
                // Get the routes from the router
                return this.$router.options.routes.filter(
                    (route) => route.path !== "/"
                );
            },
        },
    };
</script>

<template>
    <header>
        <nav>
            <ul>
                <!-- Hello Link -->
                <router-link to="/">
                    <li>Hello</li>
                </router-link>

                <!-- Other Links (Dynamic) -->
                <router-link
                    v-for="route in routes"
                    :key="route.path"
                    :to="route.path"
                >
                    <li>{{ route.name }}</li>
                </router-link>
            </ul>
        </nav>
    </header>

    <main>
        <img
            alt="Vue logo"
            class="logo"
            src="./assets/logo.svg"
            width="125"
            height="125"
        />

        <router-view></router-view>
    </main>
</template>

<style scoped>
    .logo {
        display: block;
        margin: 0 auto 2rem;
    }

    @media (min-width: 1024px) {
        .logo {
            margin: 0 2rem 0 0;
        }
    }
</style>
