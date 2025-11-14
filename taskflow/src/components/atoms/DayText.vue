<template>
    <p 
    :class="active ? 'text-yellow-500 text-xs' : 'text-xs'"
    >
        {{ title }}
    </p>
</template>

<script setup>
    defineProps(['title','active'])
</script>

<style>

</style>