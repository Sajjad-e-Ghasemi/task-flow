<template>
  <div class="flex flex-row justify-between items-center p-7 rounded-2xl w-full" id="task-tracker">
    <div class="">
        <RecorderBtn />
    </div>
    <div class="flex flex-col">
        <h3 class="font-bold text-md">مدیریت و ردیابی زمان</h3>
        <p class="text-gray-400">میتونی همین الان شروع کنی </p>
    </div>
  </div>
</template>

<script setup>
import RecorderBtn from '../atoms/RecorderBtn.vue';


</script>

<style>
  #task-tracker{
    box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.1);

  }
</style>