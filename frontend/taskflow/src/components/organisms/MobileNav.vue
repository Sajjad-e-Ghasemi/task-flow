<template>
<div class="bg-black p-2 fixed bottom-2 w-full rounded-xl left-1/2 -translate-x-1/2 shadow-md shadow-black">      <nav>
        <ul class="flex flex-row space-x-4 text-white justify-around">
          <li 
          v-for="url in urls">
            <NavMobile 
            :text="url.title"
            :url_name="url.name"
            class="bold-irsans text-xs">
              <component :is="url.icon" class="w-6 h-6 mx-auto mb-1"/>
        </NavMobile>
          </li>
        </ul>
      </nav>
    </div>
  </template>
  
  <script setup>
    import { reactive } from 'vue';
import DashboardIcon from '../atoms/DashboardIcon.vue';
import DocsIcon from '../atoms/DocsIcon.vue';
import SettingIcon from '../atoms/SettingIcon.vue';
import NavMobile from '../molecules/NavMobile.vue';

  const urls = reactive([ 
    {title: 'اسناد', name: 'اسناد', icon:DocsIcon},
    {title:"داشبورد" ,name: 'سایت مدیریت وظایف | taskflow', icon:DashboardIcon},
    {title: 'تنظیمات',name: 'تنظیمات سایت', icon:SettingIcon},
  ])
  </script>
  
  <style>
  </style>
  