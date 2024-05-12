<script setup>

import {computed} from "vue";

const getRouteMain = computed(() => {
  // Authorized user or not
  return 'main'
})
</script>

<template>
  <div class="flex bg-gray-900/90 p-2 items-center gap-10">
      <img width="70px" :src="'logo.png'" alt="123">
    <router-link class="text-white" :to="{name: getRouteMain}">Главная</router-link>
  </div>
</template>

<style scoped>

</style>