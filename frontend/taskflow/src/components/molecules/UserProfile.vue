<template>
    <div id="profile">
        <div class="flex flex-row justify-between items-center" id="loggedin-tab" v-show="loggedin">
            <div class="flex flex-row gap-2" id="profile">
                <UserAvatar />
                <UserName />
            </div>
            <div id="logout" v-show="loggedin">
                <button class="flex md:flex-row gap-1 flex-col cursor-pointer items-center hover:text-amber-400 duration-75 "
                @click="logoutHandle"
                >
                    <h6 class="text-xs">خروج</h6>
                    <LogoutIcon />
                </button>
            </div>
        </div>
        <div id="unlogged" class="flex justify-between" v-show="!loggedin">
            <div id="login" class="flex flex-row items-center align-middle gap-2">
                <button class="flex flex-row gap-1 cursor-pointer items-center hover:text-amber-400 duration-75 "
                @click="modalStatus"
                >
                    <h6 class="text-xs">ورود</h6>
                    <LoginIcon />
                </button>
                <span class="relative min-w-px min-h-5 bg-neutral-200 transform"></span>
                <button class="flex flex-row gap-1 cursor-pointer items-center hover:text-amber-400 duration-75 "
                @click="modalStatusReg"
                >
                    <h6 class="text-xs">ثبت نام</h6>
                    <RegisterIcon />
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import UserAvatar from '../atoms/UserAvatar.vue';
import UserName from '../atoms/UserName.vue';
import LoginIcon from '../atoms/LoginIcon.vue';
import LogoutIcon from '../atoms/LogoutIcon.vue';
import RegisterIcon from '../atoms/RegisterIcon.vue';

const loggedin = ref(false)

if (localStorage.getItem('authToken')) {
  loggedin.value = true;
}
else{
  loggedin.value = false;
}
const logoutHandle = () => {
    localStorage.removeItem('authToken')
    window.location.reload();
}

defineProps(['modalStatus', 'modalStatusReg'])
</script>

<style>

</style>