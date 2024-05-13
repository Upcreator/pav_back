<script setup>

import Header from "@/components/Header.vue";
import {ArrowDownTrayIcon, ChartBarIcon, ClockIcon, WrenchScrewdriverIcon} from "@heroicons/vue/24/solid/index.js";
import Button from "@/components/Button.vue";
import {useAuthStore} from "@/stores/authStore.js";
import {ref} from "vue";
const authStore = useAuthStore()
const licenseName = ref(null)

const createLicense = () => {
  const user = authStore.user

  axios.post('api/licenses/', {
    "name": licenseName.value,
    "is_Activated": false,
    "user": user.user_id,
  }, {
    headers:{
      "Authorization": `Bearer ${localStorage.getItem('access_token')}`
    }
  })
      .then(() => {
        licenseName.value = null;
      })
      .catch(e => {
        console.log(e);
      })
}



</script>

<template>
  <Header></Header>
  <div class="max-w-7xl p-1 m-auto my-10">
    <div class="grid md:grid-cols-2 gap-5">
      <div
          class="bg-gray-900/70 h-fit border border-gray-700/90 shadow-xl text-white p-5 rounded-2xl">
        <p class="mb-5">Скачать наше приложение</p>
        <a href="app.exe" target="_blank" class="w-full
        flex items-center justify-center gap-5
         text-xl bg-gray-900/70  hover:bg-gray-900/40 transition rounded-lg p-2 text-white">
          Скачать <ArrowDownTrayIcon class="h-5"/>
        </a>
      </div>
      <div
          class="bg-gray-900/70 border border-gray-700/90 shadow-xl text-white p-5 rounded-2xl">
        <p class="mb-5">Введите название вашей лицензии</p>
        <input
            v-model="licenseName"
            type="text"
            id="title"
            class="bg-gray-50 my-2 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Название"
            required/>
        <Button @click="createLicense" class="flex items-center justify-center gap-5">Создать</Button>
      </div>

    </div>


  </div>
</template>

<style scoped>

</style>