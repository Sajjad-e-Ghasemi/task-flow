<template>
  <div class="h-screen  flex flex-col items-center border-r border-gray-200 justify-between w-fit transition-all ease-in-out duration-200">
    <div :class="!is_expanded ? 'flex md:flex-col items-center gap-5 w-full ' : 'flex justify-between gap-5 flex-row-reverse w-full items-center'">
        <NavBrand>
            <img src="~@/assets/img/logo.png" alt="TaskFlow Logo" class="w-20 h-20"/>
        </NavBrand>
        <button class="cursor-pointer w-7" v-on:click="toggleNav">
            <img src="" alt="">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M11 5V19M6 8H8M6 11H8M6 14H8M6.2 19H17.8C18.9201 19 19.4802 19 19.908 18.782C20.2843 18.5903 20.5903 18.2843 20.782 17.908C21 17.4802 21 16.9201 21 15.8V8.2C21 7.0799 21 6.51984 20.782 6.09202C20.5903 5.71569 20.2843 5.40973 19.908 5.21799C19.4802 5 18.9201 5 17.8 5H6.2C5.0799 5 4.51984 5 4.09202 5.21799C3.71569 5.40973 3.40973 5.71569 3.21799 6.09202C3 6.51984 3 7.07989 3 8.2V15.8C3 16.9201 3 17.4802 3.21799 17.908C3.40973 18.2843 3.71569 18.5903 4.09202 18.782C4.51984 19 5.07989 19 6.2 19Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g>
          </svg>
          </img>
        </button>
    </div>
    <div class="">
        <UrlNavigation
        :is_expanded="is_expanded"
        />
    </div>
    <div class="">
      <UserAccounts
      :is_expanded="is_expanded"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import NavBrand from '../atoms/NavBrand.vue';
import UrlNavigation from '../molecules/UrlNavigation.vue';
import UserAccounts from '../molecules/UserAccounts.vue';

const is_expanded = ref(false); 
const toggleNav = () => {
  is_expanded.value = !is_expanded.value;
};

</script>

<style>

</style>