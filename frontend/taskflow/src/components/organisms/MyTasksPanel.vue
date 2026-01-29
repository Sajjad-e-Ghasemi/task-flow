<template>
  <div class="xl:flex flex-col gap-10 transition-all duration-200 hidden fixed left-60">
    <div class="">
        <AboutYou />
    </div>
    <div class="">
        <SearchBar />
    </div>
    <div class="flex flex-col gap-5">
        <div class="">
          <h3 class="text-2xl bold-irsans">
            وظایف من
          </h3>
        </div>
        <div class=" text-gray-400" id="tabTasks">
          <div class="flex flex-row gap-15">
          </div>

        </div>
    </div>
    <div class="w-full text-center">
      <h3 v-show="!is_login" class="text-2xl text-gray-400">:(شما ثبت نام نکردید</h3>
      <div v-show="is_login" v-for="task in tasks" class="w-full h-20 shadow-xl rounded-2xl flex justify-between p-5 align-middle items-center border border-gray-200">
        <h3 class="text-xl bold-irsans text-gray-400">
          {{ task.task_title }}
        </h3>
        <p class="text-xs text-gray-400">
          {{ task.task_desc }}
        </p>

      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import AboutYou from '../molecules/AboutYou.vue';
import SearchBar from '../molecules/SearchBar.vue';
import axios from '@/axios';

const is_login = ref(false)

if (localStorage.getItem('authToken')) {
  is_login.value = true
}else{
  is_login.value = false
}

const tasks = ref([])

async function getTasks() {
      try {
        const response = await axios.get('api/tasks/', {
         headers: {
          'Authorization': `Token ${localStorage.getItem('authToken')}`
          }
        },
      );
      tasks.value = response.data

      } catch (error) {
        console.error('failed:', error);
      }
     }

getTasks()

</script>

<style>

</style>