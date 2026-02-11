<template>
  <div class="xl:flex flex-col gap-10 transition-all duration-200 hidden fixed left-60">
    <div class="">
        <AboutYou
        :count="count"
        />
    </div>
    <div class="">
        <SearchBar />
    </div>
    <div class="flex flex-col gap-5">
        <div class="">
          <h3 class="text-2xl bold-irsans">
            وظایف من
          </h3>
        </div>
        <div class=" text-gray-400" id="tabTasks">
          <div class="flex flex-row gap-15">
          </div>
        </div>
    </div>
    <div class="w-full text-center">
      <h3 v-show="!is_login" class="text-2xl text-gray-400">شما ثبت نام نکردید :(</h3>
      <div v-show="is_login">
        <!-- نمایش تسک‌های انجام نشده -->
        <div v-if="pendingTasks.length === 0 && !loading" class="text-center py-8 text-gray-500">
          ✅ همه تسک‌ها انجام شده‌اند!
        </div>
        
        <div v-for="task in pendingTasks" :key="task.id" 
          class="w-full h-20 rounded-xl flex justify-between p-4 items-center border border-gray-200 hover:border-yellow-300 transition-all bg-white hover:shadow-lg group mb-3">
  
          <div class="flex items-center space-x-3 rtl:space-x-reverse flex-1">
            <!-- دایره وضعیت -->
            <div class="w-8 h-8 rounded-full flex items-center justify-center"
                 :class="task.is_done 
                   ? 'bg-yellow-100 border-2 border-yellow-500' 
                   : 'bg-gray-100 border-2 border-gray-400'">
              <div class="w-3 h-3 rounded-full"
                   :class="task.is_done ? 'bg-yellow-500' : 'bg-gray-500'"></div>
            </div>
            
            <!-- اطلاعات -->
            <div class="flex-1">
              <h3 class="font-bold text-gray-800">{{ task.task_title }}</h3>
              <p class="text-xs text-gray-500 truncate max-w-md">{{ task.task_desc }}</p>
            </div>
          </div>
          
          <button 
            @click="toggleTaskStatus(task.id)"
            :disabled="updatingTaskId === task.id"
            :class="[
              'px-5 py-2.5 rounded-lg font-bold text-sm transition-all shadow',
              task.is_done 
                ? 'bg-gray-900 text-white hover:bg-black' 
                : 'bg-yellow-500 text-white hover:bg-yellow-600',
              updatingTaskId === task.id ? 'opacity-60' : ''
            ]"
          >
            {{ task.is_done ? 'بازگرداندن' : 'انجام شد' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import AboutYou from '../molecules/AboutYou.vue';
import SearchBar from '../molecules/SearchBar.vue';
import axios from '@/axios';

const is_login = ref(false)
const tasks = ref([])
const loading = ref(false)
const error = ref(null)
const updatingTaskId = ref(null)

onMounted(() => {
  const token = localStorage.getItem('authToken')
  is_login.value = Boolean(token)

  if (is_login.value) {
    getTasks()
  }
})


async function getTasks() {
  loading.value = true
  error.value = null

  try {
    const { data } = await axios.get('api/tasks/', {
      headers: {
        Authorization: `Token ${localStorage.getItem('authToken')}`,
      },
    })

    tasks.value = data
    console.log('✅ تسک‌ها دریافت شدند:', data.length)

  } catch (err) {
    console.error(err)
    error.value = 'خطا در دریافت تسک‌ها'

    if (err.response?.status === 401) {
      localStorage.removeItem('authToken')
      is_login.value = false
    }
  } finally {
    loading.value = false
  }
}

async function toggleTaskStatus(taskId) {
  if (updatingTaskId.value) return

  const task = tasks.value.find(t => t.id === taskId)
  if (!task) return

  updatingTaskId.value = taskId

  const previous = task.is_done
  task.is_done = !task.is_done // optimistic update

  try {
    await axios.patch(
      `api/tasks/${taskId}/`,
      { is_done: task.is_done },
      {
        headers: {
          Authorization: `Token ${localStorage.getItem('authToken')}`,
        },
      }
    )


  } catch (err) {
    console.log('❌ STATUS:', err.response.status)
    console.log('❌ DATA:', err.response.data)

    task.is_done = previous
    alert('خطا در تغییر وضعیت')
  }
  finally {
    updatingTaskId.value = null
  }
}

/* ===================== COMPUTED ===================== */

const pendingTasks = computed(() =>
  tasks.value.filter(task => task.is_done === false)
)

const completedTasks = computed(() =>
  tasks.value.filter(task => task.is_done === true)
)

const count = computed(() => pendingTasks.value.length)

/* ===================== HELPERS ===================== */

function refreshTasks() {
  if (is_login.value) getTasks()
}

</script>

<style>

</style>