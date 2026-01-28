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
              وظیفه تو اضافه کن!
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

    const task_title = ref('');
    const task_desc = ref('');
    const task_author = ref(null);
        
    const inputs = reactive([
      {label: 'عنوان وظیفه', type: 'text', placeholder: 'عنوان وظیفه رو وارد کن', model : task_title},
      {label: 'توضیحات', type: 'text', placeholder: 'توضیحات وظیفه خود را وارد کنید', model : task_desc},
      {label: 'نویسنده', type: 'number', model : task_author},
    ]);
    
    async function handeSumbit() {
      try {
        const response = await axios.post('api/tasks/', {
          task_title: task_title.value,
          task_desc: task_desc.value,
          task_author: Number(task_author.value),
        });

        window.location.reload();
      } catch (error) {
        console.error('failed:', error);
      }
      finally {
        task_title.value = '';
        task_desc.value = '';
        task_started_at.value = null;
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