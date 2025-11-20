import { createRouter, createWebHistory } from 'vue-router'

import DashboardPage from "@/components/pages/DashboardPage.vue"
import SettingPage from "@/components/pages/SettingPage.vue"

const routes = [
    {path:"/", name:"سایت مدیریت وظایف | taskflow",component: DashboardPage},
    {path:"/settings", name:"تنظیمات سایت", component: SettingPage},
    {path:"/docs", name:"اسناد", component: SettingPage},
  ]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
