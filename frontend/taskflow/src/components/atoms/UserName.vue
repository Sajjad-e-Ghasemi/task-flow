<template>
  <div>
    <h3 class="font-bold text-xs">
      {{ name }}
    </h3>
  </div>
</template>

<script setup>
defineProps({
  name: {
    type: String,
    required: true
  }
});
</script>

<style>

</style>