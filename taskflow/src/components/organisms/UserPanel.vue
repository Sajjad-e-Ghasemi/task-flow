<template>
    <div class="grid grid-cols-[400px_1fr_150px] h-screen my-auto" id="user-panel">
        <div class="flex flex-col gap-15 mt-10">
            <div>
                <UserProfile />
            </div>
            <div class="">
                <TaskTracker />
            </div>
            <div class="">
                <DateBox />
            </div>
            <div class="">
                <CalenadrBox />
            </div>
            <div class="overflow-y-scroll p-2 flex flex-col gap-2 max-h-[300px]">
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
    #user-panel{
        margin-right: 40px;

    }
</style>