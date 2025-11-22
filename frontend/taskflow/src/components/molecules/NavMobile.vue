<template>
    <router-link 
    :to="{name : url_name}">
        <div class="flex flex-col items-center text-xs">
            <slot>

            </slot>
            <NavMobileTxt 
            :text="text"
            />
        </div>
    </router-link>
</template>

<script setup>

import NavMobileTxt from '@/components/atoms/NavMobileTxt.vue';

defineProps({
  text: {
    type: String,
    required: true
  },
  url_name:{
    type: String,
    required: false
  }
});

</script>

<style>

</style>