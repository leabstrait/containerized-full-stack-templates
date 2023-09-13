<script setup>
    import { ref, onMounted } from "vue";

    const apiResponse = ref(null);

    const apiUrl = "/api/app2";

    // Function to make the API call
    const fetchData = async () => {
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            const data = await response.json();
            apiResponse.value = data;
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };

    // Use the onMounted hook to make the API call when the component is mounted
    onMounted(() => {
        fetchData();
    });
</script>

<template>
    <!-- Display the API response data -->
    <div v-if="apiResponse">
        <h2>API Response:</h2>
        <pre>{{ JSON.stringify(apiResponse, null, 2) }}</pre>
    </div>
</template>

<style scoped>
    h2 {
        font-weight: 500;
        font-size: 2.6rem;
        position: relative;
        top: -10px;
    }
</style>
