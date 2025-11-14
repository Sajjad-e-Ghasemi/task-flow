<script setup>
import MyTasksPanel from './components/organisms/MyTasksPanel.vue';
import NavBar from './components/organisms/NavBar.vue';
import UserPanel from './components/organisms/UserPanel.vue';

</script>

<template>
   <div class="flex flex-row container mx-auto">
    <UserPanel />
    <MyTasksPanel />
    <NavBar />
   </div>
</template>

<style scoped>
</style>
