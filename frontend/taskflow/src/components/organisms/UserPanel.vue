<template>
    <div
        class="mx-auto lg:grid lg:grid-cols-[500px_1fr_150px] 
               grid grid-cols-1 gap-4 w-full "
        id="user-panel"
    >

        <div class="flex flex-col lg:justify-between justify-center gap-9 mt-5 px-4">
            <UserProfile
            :modalStatus="modalStatus"
            :modalStatusReg="modalStatusReg"
            />

            <ModalLogin
            :is_open="is_open"
            :modelStatus="modalStatus"
            />
            
            <ModalRegister
            :is_open_login="is_open"
            :is_open="register_modalopen"
            :modelStatus="modalStatusReg"
            />

            <ModalAddTask
            :is_open="is_open_task"
            :modelStatus="showModalTask"
            />
             
            <div class="flex justify-center">
                <TaskTracker />
            </div>

            <DateBox
            :handleAddTask="modalStatusTask"
            :modelStatus="showModalTask"
            />


            <CalenadrBox /> 
            <div class="overflow-y-auto p-2 flex flex-col gap-2 md:max-h-[400px] max-h-[300px]">
                <DidItBox />
                <DidItBox />
                <DidItBox />
                <DidItBox />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useToast } from "vue-toastification";
import CalenadrBox from '../molecules/CalenadrBox.vue';
import DateBox from '../molecules/DateBox.vue';
import DidItBox from '../molecules/DidItBox.vue';
import TaskTracker from '../molecules/TaskTracker.vue';
import UserProfile from '../molecules/UserProfile.vue';

import ModalLogin from '../molecules/ModalLogin.vue';
import ModalRegister from '../molecules/ModalRegister.vue';
import ModalAddTask from '../molecules/ModalAddTask.vue';

const toast = useToast();
const is_open = ref(false);
const is_open_task = ref(false);

const register_modalopen = ref(false);

const modalStatus = () => {
    is_open.value = !is_open.value;
};

const modalStatusReg = () => {
    register_modalopen.value =  !register_modalopen.value;
}

const showModalTask = () => {
    is_open_task.value = !is_open_task.value
}

const modalStatusTask = () => {
    const loggedin = ref(false)
    if (localStorage.getItem('authToken')) {
        loggedin.value = true;
        is_open_task.value = !is_open_task.value;
    }
    else{
        toast.error("لطفا ابتدا وارد حساب کاربری خود شوید");
        loggedin.value = false;
    }
}

</script>

<style>
#user-panel {
    margin-right: 0; 
}
</style>
