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
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import AboutYou from '../molecules/AboutYou.vue';
import SearchBar from '../molecules/SearchBar.vue';

const is_login = ref(false)

if (localStorage.getItem('authToken')) {
  is_login.value = true
}else{
  is_login.value = false
}
</script>

<style>

</style>