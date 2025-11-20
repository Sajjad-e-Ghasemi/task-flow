import { createRouter, createWebHistory } from "vue-router"
import DashboardPage from "@/components/pages/DashboardPage.vue"
import SettingPage from "@/components/pages/SettingPage.vue"

const routes = [
    {path:"/", component: DashboardPage},
    {path:"/settings", component: SettingPage},
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router