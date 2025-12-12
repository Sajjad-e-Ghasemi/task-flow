<template>
    <p class="text-xs text-red-500">
        {{ text }}
    </p>
</template>

<script setup>
defineProps({
    text: {
        type: String,
        default: '*خطایی رخ داده است'
    }
});
</script>