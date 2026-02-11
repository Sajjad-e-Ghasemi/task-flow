<template>
  <div class="flex flex-col gap-3">
    <div class="">
        <WelcomeText />
    </div>
    <div class="">
        <h1 class="text-2xl bold-irsans">
            وظایفی که باید انجام بدی
        </h1>
    </div>
    <div class="">
        <h1 class="text-2xl bold-irsans">
            {{ count }} تاست
        </h1>
    </div>
  </div>
</template>

<script setup>
import WelcomeText from '../atoms/WelcomeText.vue';

const props = defineProps(['count'])
</script>

<style>

</style>