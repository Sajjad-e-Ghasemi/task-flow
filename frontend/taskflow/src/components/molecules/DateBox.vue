<template>
  <div id="date-box" class="flex flex-row justify-between">
    <div id="date" class="flex flex-col gap-2">
        <DateText />
        <h3 class="font-bold text-2xl bold-irsans">امروز</h3>
    </div>
    <div id="task-btn">
        <AddTaskButton />
    </div>
  </div>
</template>

<script setup>
import AddTaskButton from '../atoms/AddTaskButton.vue';
import DateText from '../atoms/DateText.vue';


</script>

<style>

</style>