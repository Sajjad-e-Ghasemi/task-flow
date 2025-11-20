<template>
    <div
        class="mx-auto lg:grid lg:grid-cols-[500px_1fr_150px] 
               grid grid-cols-1 gap-4 w-full "
        id="user-panel"
    >
        <div class="flex flex-col lg:justify-between justify-center gap-10 mt-10 px-4">
            <UserProfile />

            <div class="flex justify-center">
                <TaskTracker />
            </div>

            <DateBox />

            <CalenadrBox />

            <div class="overflow-y-auto p-2 flex flex-col gap-2 max-h-[400px]">
                <DidItBox />
                <DidItBox />
                <DidItBox />
                <DidItBox />
            </div>
        </div>
    </div>
</template>

<script setup>
import CalenadrBox from '../molecules/CalenadrBox.vue';
import DateBox from '../molecules/DateBox.vue';
import DidItBox from '../molecules/DidItBox.vue';
import TaskTracker from '../molecules/TaskTracker.vue';
import UserProfile from '../molecules/UserProfile.vue';
</script>

<style>
#user-panel {
    margin-right: 0; 
}
</style>
