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
            ورود
        </h3>
        <ModalInput
        v-for="input in inputs"
        :type="input.type"
        :placeholder="input.placeholder"
        v-model="input.model"
        />
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
const toast = useToast();
const username = ref('');
const password = ref('');
const loggedin = ref(false)

const inputs = reactive([
  {label: 'نام کاربری یا ایمیل', type: 'text', placeholder: 'نام کاربری یا ایمیل خود را وارد کنید', model : username},
  {label: 'رمز عبور', type: 'password', placeholder: 'رمز عبور خود را وارد کنید', model : password}
]);

async function handeSumbit() {
  try {
    const response = await axios.post('/api/token/', {
      username: username.value,
      password: password.value
    });
    const token = response.data.token;
    localStorage.setItem('authToken', token);
    toast.success("با موفقیت وارد شدید");
    axios.defaults.headers.common['Authorization'] = `Token ${token}`;
    window.location.reload();
  } catch (error) {
    console.error('Login failed:', error);
  }
  finally {
    username.value = '';
    password.value = '';
    is_open.value = false;
    
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
  }
});
</script>

<style>

</style>