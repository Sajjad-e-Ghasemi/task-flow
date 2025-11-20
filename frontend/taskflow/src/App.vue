<script setup>
import MobileNav from './components/organisms/MobileNav.vue';
import MyTasksPanel from './components/organisms/MyTasksPanel.vue';
import SideBar from './components/organisms/Sidebar.vue';
import UserPanel from './components/organisms/UserPanel.vue';
import DashboardPage from './components/pages/DashboardPage.vue';

</script>

<template>
   <DashboardPage />

   <router-view />
</template>

<style scoped>
</style>
