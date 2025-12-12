<template>
    <div>
      <dialog open v-show="is_open" class="border border-gray-200 mx-auto p-10 rounded-xl bg-white absolute">
        <button 
        class="cursor-pointer absolute top-2 right-2 text-xl"
        @click="modelStatus">
          <CloseIcon />
        </button>
        <form method="post" class="flex flex-col gap-4 w-80 ease-in-out duration-200" @submit.prevent="handeSumbit">
          <img src="@/assets/img/logo.png" alt="Login Icon" class="mx-auto mt-6 h-30 w-30" />
          <h3 class="text-center mt-4 text-lg font-semibold">
              ثبت نام
          </h3>
          <ModalInput
          v-for="input in inputs"
          :type="input.type"
          :placeholder="input.placeholder"
          :class="isnt_match ? 'border-red-500' : ''"
          v-model="input.model"
          />
          <ErrorTxt 
          v-if="isnt_match" 
          text="*رمزهای عبور مطابقت ندارند" />
          <ModalBtn />
        </form>
      </dialog>
    </div>
  </template>
  
  <script setup>
  import { reactive, ref } from 'vue';
  import ModalInput from '../atoms/ModalInput.vue';
  import ModalBtn from '../atoms/ModalBtn.vue';
  import CloseIcon from '../atoms/CloseIcon.vue';
  import axios from '@/axios';
  import { useToast } from "vue-toastification";
  import ErrorTxt from '../atoms/ErrorTxt.vue';

  const username = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  const isnt_match = ref(false);

  const inputs = reactive([
    {label: 'نام کاربری یا ایمیل', type: 'text', placeholder: 'نام کاربری یا ایمیل خود را وارد کنید', model : username},
    {label: 'رمز عبور', type: 'password', placeholder: 'رمز عبور خود را وارد کنید', model : password},
    {label: 'تایید رمز عبور', type: 'password', placeholder: 'رمز عبور خود را مجددا وارد کنید', model : confirmPassword},
  ]);
  
  async function handeSumbit() {
    try {
        if (password.value == confirmPassword.value) {
            isnt_match.value = false;
            const response = await axios.post('/api/accounts/', {
                username: username.value,
                password: password.value
            });
            is_open_login.value = true
            is_open.value =false
        } else {
            isnt_match.value = true;
        }
    }
    catch (error) {
      console.error('Login failed:', error);
    }
    finally {
      username.value = '';
      password.value = '';
      confirmPassword.value = '';
      
    }
  }
  
  defineProps({
    is_open: {
      type: Boolean,
      default: false
    },
    modelStatus: {
      type: Function,
      required: true
    },
    is_open_login: {
        type: Boolean,
        default: false
    }
  });
  </script>
  
  <style>
  
  </style>