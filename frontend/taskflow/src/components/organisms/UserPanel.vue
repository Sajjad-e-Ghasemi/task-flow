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
      
      
      <!-- تسک‌های انجام شده -->
      <div class="bg-gray-100 p-4 rounded-xl">
        <div class="overflow-y-auto p-2 flex flex-col gap-2 md:max-h-[300px] max-h-[250px]">
          <DidItBox 
            v-if="completedTasks.length > 0"
            :tasks="completedTasks"
            @toggleTask="toggleTaskStatus"
            @undoTask="undoTask"
          />
          <div v-else class="text-center py-8 text-gray-500">
            📝 هنوز تسکی انجام نداده‌اید
          </div>
        </div>
        <div class="mt-2 text-sm text-yellow-600">
          {{ completedTasks.length }} تسک انجام شده
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useToast } from "vue-toastification";
import CalenadrBox from '../molecules/CalenadrBox.vue';
import DateBox from '../molecules/DateBox.vue';
import DidItBox from '../molecules/DidItBox.vue';
import TaskTracker from '../molecules/TaskTracker.vue';
import UserProfile from '../molecules/UserProfile.vue';

import axios from '@/axios';

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

// وضعیت‌ها
const is_login = ref(false);
const tasks = ref([]);
const loading = ref(false);
const error = ref(null);
const updatingTaskId = ref(null);

// وضعیت اولیه
onMounted(() => {
  const token = localStorage.getItem('authToken');
  is_login.value = !!token;

  if (is_login.value) {
    getTasks();
  }
});

// دریافت تسک‌ها
async function getTasks() {
  loading.value = true;
  error.value = null;

  try {
    const response = await axios.get('api/tasks/', {
      headers: {
        'Authorization': `Token ${localStorage.getItem('authToken')}`
      }
    });
    
    tasks.value = response.data;
    console.log('✅ تسک‌ها دریافت شدند:', tasks.value);
    
    // بررسی دقیق ساختار داده
    if (tasks.value.length > 0) {
      console.log('🔍 ساختار تسک اول:', tasks.value[0]);
      console.log('🔍 فیلدهای موجود:', Object.keys(tasks.value[0]));
    }
    
  } catch (err) {
    console.error('❌ خطا در دریافت تسک‌ها:', err);
    error.value = err.response?.data?.message || 'خطا در دریافت داده‌ها';
    
    if (err.response?.status === 401) {
      localStorage.removeItem('authToken');
      is_login.value = false;
    }
  } finally {
    loading.value = false;
  }
}

// تغییر وضعیت تسک (toggle)
async function toggleTaskStatus(taskId) {
  console.log('🔄 تغییر وضعیت تسک:', taskId);

  const taskIndex = tasks.value.findIndex(t => t.id === taskId);
  if (taskIndex === -1) {
    console.error('❌ تسک یافت نشد:', taskId);
    return;
  }

  const currentTask = tasks.value[taskIndex];
  
  // تشخیص فیلد وضعیت - بهبود یافته
  let statusField = null;
  if (currentTask.is_done !== undefined) statusField = 'is_done';
  else if (currentTask.is_active !== undefined) statusField = 'is_active';
  else if (currentTask.completed !== undefined) statusField = 'completed';
  else if (currentTask.status !== undefined) statusField = 'status';
  else if (currentTask.done !== undefined) statusField = 'done';
  
  if (!statusField) {
    console.error('❌ فیلد وضعیت یافت نشد برای تسک:', currentTask);
    toast.error('خطا: فیلد وضعیت یافت نشد');
    return;
  }
  
  console.log(`🔍 فیلد وضعیت تشخیص داده شد: ${statusField}`);
  
  let newStatus;
  const currentStatus = currentTask[statusField];
  
  // منطق تغییر وضعیت
  if (typeof currentStatus === 'boolean') {
    newStatus = !currentStatus;
  } else if (currentStatus === 'true' || currentStatus === 'done' || currentStatus === 'completed') {
    newStatus = false;
  } else {
    newStatus = true;
  }
  
  console.log(`🔄 تغییر از ${currentStatus} به ${newStatus}`);

  // به‌روزرسانی محلی
  tasks.value[taskIndex][statusField] = newStatus;
  updatingTaskId.value = taskId;

  try {
    // ارسال به سرور
    await axios.patch(
      `api/tasks/${taskId}/`,
      { [statusField]: newStatus },
      {
        headers: {
          'Authorization': `Token ${localStorage.getItem('authToken')}`,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log('✅ وضعیت تسک تغییر کرد:', taskId);
    
    // پیام موفقیت
    if (newStatus) {
      toast.success('تسک به لیست انجام‌شده‌ها اضافه شد');
    } else {
      toast.success('تسک به لیست انجام‌نشده‌ها بازگردانده شد');
    }
    
  } catch (err) {
    console.error('❌ خطا در تغییر وضعیت:', err);
    // بازگرداندن وضعیت قبلی در صورت خطا
    tasks.value[taskIndex][statusField] = currentStatus;
    
    let errorMessage = 'خطا در تغییر وضعیت';
    if (err.response?.status === 404) errorMessage = 'تسک یافت نشد';
    if (err.response?.status === 405) errorMessage = 'متد پشتیبانی نمی‌شود';
    
    toast.error(errorMessage);
  } finally {
    updatingTaskId.value = null;
  }
}

// تابع بازگرداندن تسک (undo)
async function undoTask(taskId) {
  console.log('↩️ بازگرداندن تسک:', taskId);
  toggleTaskStatus(taskId); // از همان تابع استفاده می‌کنیم
}

// computed برای تسک‌های انجام شده
const completedTasks = computed(() => {
  console.log('📊 محاسبه completedTasks...');

  const completed = tasks.value.filter(task => {
    if (!task) return false;
    
    // بررسی همه فیلدهای ممکن برای وضعیت "انجام شده"
    const isCompleted = 
      task.is_done === true || 
      task.is_done === 'true' ||
      task.is_active === true ||
      task.is_active === 'true' ||
      task.completed === true ||
      task.completed === 'true' ||
      task.done === true ||
      task.done === 'true' ||
      task.status === 'completed' ||
      task.status === 'done' ||
      task.status === 'true';
    
    return isCompleted;
  });

  console.log('✅ تعداد تسک‌های انجام شده:', completed.length);
  return completed;
});

// computed برای تسک‌های در انتظار (انجام نشده)
const pendingTasks = computed(() => {
  console.log('📊 محاسبه pendingTasks...');

  const pending = tasks.value.filter(task => {
    if (!task) return false;
    
    // بررسی همه فیلدهای ممکن برای وضعیت "انجام نشده"
    const isPending = 
      task.is_done === false || 
      task.is_done === 'false' ||
      task.is_active === false ||
      task.is_active === 'false' ||
      task.completed === false ||
      task.completed === 'false' ||
      task.done === false ||
      task.done === 'false' ||
      task.status === 'pending' ||
      task.status === 'incomplete' ||
      task.status === 'false' ||
      task.status === 'todo' ||
      // اگر هیچ کدام از فیلدهای بالا true نبود، آن را pending در نظر بگیر
      !(task.is_done === true || 
        task.is_done === 'true' ||
        task.is_active === true ||
        task.is_active === 'true' ||
        task.completed === true ||
        task.completed === 'true' ||
        task.done === true ||
        task.done === 'true' ||
        task.status === 'completed' ||
        task.status === 'done' ||
        task.status === 'true');
    
    return isPending;
  });

  console.log('✅ تعداد تسک‌های انجام نشده:', pending.length);
  return pending;
});

// تابع تست برای بررسی داده‌ها
function debugTasks() {
  console.log('=== دیباگ داده تسک‌ها ===');
  console.log('کل تسک‌ها:', tasks.value.length);
  console.log('انجام شده:', completedTasks.value.length);
  console.log('انجام نشده:', pendingTasks.value.length);

  if (tasks.value.length > 0) {
    console.log('📋 لیست تمام تسک‌ها:');
    tasks.value.forEach((task, index) => {
      console.log(`\nتسک ${index + 1} (ID: ${task.id}):`);
      console.log('  عنوان:', task.title);
      console.log('  توضیح:', task.description);
      console.log('  is_done:', task.is_done);
      console.log('  is_active:', task.is_active);
      console.log('  completed:', task.completed);
      console.log('  status:', task.status);
      console.log('  done:', task.done);
    });
  }
}

// فراخوانی دیباگ پس از دریافت داده
onMounted(() => {
  setTimeout(debugTasks, 2000);
});
</script>

<style>
#user-panel {
  margin-right: 0; 
}
</style>