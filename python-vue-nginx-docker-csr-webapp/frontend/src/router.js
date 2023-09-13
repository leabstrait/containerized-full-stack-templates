import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: "/",
        name: "Hello",
        component: () => import("./views/Hello.vue"),
    },
    {
        path: "/identify",
        name: "Identify",
        component: () => import("./views/Identify.vue"),
    },
    {
        path: "/app1",
        name: "App1",
        component: () => import("./views/App1.vue"),
    },
    {
        path: "/app2",
        name: "App2",
        component: () => import("./views/App2.vue"),
    },
    {
        path: "/admin",
        name: "Admin",
        component: () => import("./views/Admin.vue"),
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
