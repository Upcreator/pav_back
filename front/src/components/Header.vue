<script setup>

import {computed} from "vue";
import {useAuthStore} from "@/stores/authStore.js";
import Button from "@/components/Button.vue";
import router from "@/router.js";

const authStore = useAuthStore()

const getRouteMain = computed(() => {
  // Authorized user or not
  if(authStore.user){
    return 'main'
  }
  return 'welcome';
})

const logout = () => {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  router.push({name: 'login'})
}
</script>

<template>
  <div class="flex bg-gray-900/90 p-2 items-center justify-between gap-10">
    <div class="flex items-center gap-10">
      <img width="70px" :src="'logo.png'" alt="123">
      <router-link class="text-white" :to="{name: getRouteMain}">Главная</router-link>
    </div>

    <button v-if="authStore.user" class="text-white" @click="logout">Выйти</button>
  </div>
</template>

<style scoped>

</style>