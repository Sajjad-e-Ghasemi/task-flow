<template>
  <div>
    <h3 class="text-gray-400">{{ currentDate }}</h3>
  </div>
</template>

<script setup>
  const date = new Date();
  const currentDate = new Intl.DateTimeFormat('fa-IR', {
    year : 'numeric',
    month : 'long',
    day : 'numeric'
    }).format(date)
</script>

<style>

</style>