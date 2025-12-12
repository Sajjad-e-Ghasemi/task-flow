<script setup>
import MobileNav from '@/components/organisms/MobileNav.vue';
import MyTasksPanel from '@/components/organisms/MyTasksPanel.vue';
import SideBar from '@/components/organisms/Sidebar.vue';
import UserPanel from '@/components/organisms/UserPanel.vue';
</script>

<template>
   <div class="flex md:flex-row flex-col justify-between">
      <MobileNav
      class="sm:block lg:hidden"
      />
      <MyTasksPanel />
      <SideBar />
      <UserPanel />
   </div>
</template>

<style scoped>
</style>
