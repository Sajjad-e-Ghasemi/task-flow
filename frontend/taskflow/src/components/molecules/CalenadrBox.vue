<template>
  <div>
    <div class="flex flex-row lg:gap-6 gap-2 justify-center">
        <DayText 
        :title="day.title" 
        :active="day.isCurrent" 
        v-for="day in weekDays"
        />
    </div>
  </div>
</template>

<script setup>
import { onMounted, reactive } from 'vue';
import DayText from '../atoms/DayText.vue';

const dayWeek = new Date();
let dayofWeek = dayWeek.getDay(); 

const weekDays = reactive([
  { dayID: 6, title: "شنبه", isCurrent: false },
  { dayID: 0, title: "یکشنبه", isCurrent: false },
  { dayID: 1, title: "دوشنبه", isCurrent: false },
  { dayID: 2, title: "سه شنبه", isCurrent: false },
  { dayID: 3, title: "چهارشنبه", isCurrent: false },
  { dayID: 4, title: "پنجشنبه", isCurrent: false },
  { dayID: 5, title: "جمعه", isCurrent: false },
]);

function isCurrentDay() {
  for (let day = 0; day < weekDays.length; day++) {
    const element = weekDays[day];
    if (element.dayID == dayofWeek) {
      element.isCurrent = true;
      break;
    }
  }
}

onMounted(() =>{
  isCurrentDay();
})

</script>

<style>

</style>