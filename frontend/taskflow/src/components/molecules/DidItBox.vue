<template>
  <div class="flex flex-row justify-between items-center p-12 rounded-2xl bg-yellow-300" id="task-tracker">
      <div class="flex flex-col gap-2">
          <h3 class="font-bold text-md bold-irsans">ملاقات</h3>
          <p class="text-xs">گفت با دوستان درباره برخی از وظایف هفته های آتی    </p>
        </div>
        <div class="">
            <CheckBtn />
        </div>
  </div>
</template>

<script setup>
import CheckBtn from '../atoms/CheckBtn.vue';


</script>

<style>

</style>