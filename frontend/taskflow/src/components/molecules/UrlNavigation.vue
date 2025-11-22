a<template>
    <div>
      <nav class="flex flex-col gap-10 w-fit items-start">
        <router-link 
          v-for="url in urls"
          :key="url.name"
          :to="{ name: url.name }"
          v-on:click="is_current_event(url.name)"
          :class="route.name == url.name ? 'bg-amber-300' : ''"
          class="flex flex-row justify-between duration-75 gap-50 p-3 rounded-xl items-center hover:bg-amber-200 w-fit"
          >
          <UrlText 
          v-show="is_expanded" 
          >
            {{ url.title }}
          </UrlText>
  
          <UrlIcon>
            <component 
            :is="url.icon" 
            /> 
          </UrlIcon>
        </router-link>
      </nav>
    </div>
  </template>
  
  <script setup>
  import { useRoute } from 'vue-router';
import UrlIcon from '../atoms/UrlIcon.vue';
  import UrlText from '../atoms/UrlText.vue';
  
  defineProps({
    is_expanded: Boolean,
    urls: Array,
  });
  const route = useRoute();
  </script>
  