<template>
  <div>
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-lg font-bold">تسک‌های انجام شده ({{ tasks.length }})</h2>
      <span class="text-sm text-gray-500">برای بازگرداندن کلیک کنید</span>
    </div>
    
    <div class="space-y-3">
      <div 
        v-for="task in tasks" 
        :key="task.id" 
        class="flex items-center justify-between p-4 bg-yellow-500 border border-yellow-800 rounded-xl hover:bg-yellow-300 transition-colors"
      >
        <div class="flex-1">
          <h3 class="font-semibold text-gray-800">
            {{ task.task_title || 'بدون عنوان' }}
          </h3>
          <p class="text-sm text-gray-600 mt-1">
            {{ task.task_desc || 'بدون توضیح' }}
          </p>
        </div>
        
        <div class="flex items-center gap-3">
          <!-- دکمه تیک - تغییر وضعیت -->
          <button 
            @click="handleToggle(task.id)"
            class="w-8 h-8 flex items-center justify-center bg-green-100 text-green-600 rounded-full hover:bg-green-200"
            title="تغییر وضعیت"
          >
            ✓
          </button>
          
          <!-- دکمه بازگرداندن -->
          <button 
            @click="handleUndo(task.id)"
            class="px-3 py-1.5 text-xs bg-red-100 text-red-600 rounded-lg hover:bg-red-200 transition-colors"
          >
            بازگرداندن
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  tasks: {
    type: Array,
    default: () => []
  }
});

const emit = defineEmits(['toggleTask', 'undoTask']);

const handleToggle = (taskId) => {
  console.log('DidItBox: ارسال toggle برای تسک', taskId);
  emit('toggleTask', taskId);
};

const handleUndo = (taskId) => {
  console.log('DidItBox: ارسال undo برای تسک', taskId);
  emit('undoTask', taskId);
};
</script>