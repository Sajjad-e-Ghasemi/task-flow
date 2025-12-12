<template>
    <input class="border border-gray-200 rounded px-3 py-2 w-xs outline-0 text-xs"  
    :type="type"
    :placeholder="placeholder"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
    />
</template>

<script setup>
defineProps({
  type: String,
  placeholder: String,
  modelValue: String
});

defineEmits(['update:modelValue'])
</script>

<style>

</style>