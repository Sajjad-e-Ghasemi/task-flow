<script setup>
import MyTasksPanel from './components/organisms/MyTasksPanel.vue';
import SideBar from './components/organisms/Sidebar.vue';
import UserPanel from './components/organisms/UserPanel.vue';

</script>

<template>
   <div class="flex flex-row justify-between">
    <UserPanel />
    <MyTasksPanel />
    <SideBar />
   </div>
</template>

<style scoped>
</style>
