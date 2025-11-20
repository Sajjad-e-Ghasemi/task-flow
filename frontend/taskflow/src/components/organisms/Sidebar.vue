<template>
  <div 
  class="h-screen hidden lg:flex flex-col items-center border-r border-gray-200 bg-white justify-between w-fit transition-all duration-300 ease-in-out absolute left-0 "
  :class="is_expanded ? 'w-64 p-5' : 'w-20 p-3'"
  >
        <div class="sm:hidden flex flex-row" id="profile">
            <UserAvatar />
            <UserName />
        </div>
    <div 
        :class="!is_expanded ? 'flex md:flex-col items-center gap-5 w-full' 
        : 'flex justify-between gap-5 flex-row-reverse w-full items-center' "
        >
        <NavBrand>
            <img src="~@/assets/img/logo.png" alt="TaskFlow Logo" class="w-20 h-20"/>
        </NavBrand>
        <ToggleButton 
        :toggleNav="toggleNav" 
        />
    </div>
    <div class="">
        <UrlNavigation
        :is_expanded="is_expanded"
        :urls="urls"
        />
    </div>
    <div class="">
      <UserAccounts
      :is_expanded="is_expanded"
      />
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import NavBrand from '../atoms/NavBrand.vue';
import UrlNavigation from '../molecules/UrlNavigation.vue';
import UserAccounts from '../molecules/UserAccounts.vue';
import UserAvatar from '../atoms/UserAvatar.vue';
import UserName from '../atoms/UserName.vue';
import ToggleButton from '../atoms/ToggleButton.vue';
import DashboardIcon from '../atoms/DashboardIcon.vue';
import SettingIcon from '../atoms/SettingIcon.vue';
import DocsIcon from '../atoms/DocsIcon.vue';

const urls = reactive([ 
  {title:"داشبورد" ,name: 'سایت مدیریت وظایف | taskflow', icon:DashboardIcon},
  {title: 'اسناد', name: 'اسناد', icon:DocsIcon},
  {title: 'تنظیمات',name: 'تنظیمات سایت', icon:SettingIcon},
])


const is_expanded = ref(false); 
const toggleNav = () => {
  is_expanded.value = !is_expanded.value;
};


</script>

<style>

</style>