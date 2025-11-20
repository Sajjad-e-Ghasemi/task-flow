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
            <a href=""  
            v-for="day in days"
            @click="day.active==false"
            >
              <p
              :class="day.active ? 'text-amber-400':''"
              >
                {{ day.tabTitle }}
              </p>
            </a>
          </div>

        </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import AboutYou from '../molecules/AboutYou.vue';
import SearchBar from '../molecules/SearchBar.vue';

const days = reactive([
  {tabId : 1 ,tabTitle : "امروز", active: true},
  {tabId : 2 ,tabTitle : "فردا", active : false},
  {tabId : 3 ,tabTitle : "پس فردا", active : false},
])
</script>

<style>

</style>