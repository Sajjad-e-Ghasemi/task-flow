<!-- NavMobileTxt.vue (button variant) -->
<template>
  <a
    class="inline-block px-4 py-2 rounded-4xl text-white "
    @click="$emit('click')"
  >
    {{ text }}
</a>
</template>

<script setup>
defineProps({
  text: { type: String, required: true }
});
</script>
