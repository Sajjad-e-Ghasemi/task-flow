<template>
  <div class="flex flex-row justify-between items-center border border-gray-300 px-3 p-2 rounded-xl mb-5 gap-10">
      <UserName 
        :name="username" 
        v-show="is_expanded"
      />
    <img src="~@/assets/img/myPic.jpeg" class="rounded-full w-8 h-8" alt="">
  </div>
</template>

<script setup>
import { ref } from 'vue';
import UserName from '../atoms/UserName.vue';

const username = ref("Sajjad Ghasemi");
defineProps(['is_expanded']);
</script>

<style>

</style>