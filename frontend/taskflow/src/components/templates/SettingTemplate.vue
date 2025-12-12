<script setup>
import MobileNav from '@/components/organisms/MobileNav.vue';
import SideBar from '@/components/organisms/Sidebar.vue';
import axios from '@/axios';
import { ref, onMounted } from 'vue';

const message = ref(null);
async function getMessage() {
    try {
        const response = await axios.get('/api/accounts/');
        message.value = response.data.message;
    } catch (error) {
        console.error('Error fetching message:', error);
    }
}

onMounted(() => {
  getMessage();
});
</script>

<template>   
   <div class="flex md:flex-row flex-col justify-between">
    <pre>{{ message }}</pre>
    <MobileNav class="sm:block lg:hidden" />
    <SideBar />

   </div>
</template>
