<script setup>

import Button from "../components/Button.vue";
import router from "@/router.js";
import {ref} from "vue";
import axios from "axios";

const email = ref(null)
const username = ref(null)
const password = ref(null)

const signup = () => {
  axios.post('api/users/', {email: email.value, username: username.value, password: password.value})
      .then((d) => {
        router.push({name: 'login'})
      })
      .catch((e) => {
        console.log(e);
      })
}
</script>

<template>
  <div class="grid md:grid-cols-2 h-screen">
    <div class="hidden md:flex gap-10 flex-col items-center justify-center bg-gray-900/60 shadow-xl">
      <img :src="`logo.png`">
      <p class="text-5xl font-extrabold text-white">PavApp</p>
    </div>
    <div class="w-full relative text-white flex flex-col justify-center items-center">
      <div class="absolute right-10 top-10">
        <p class="cursor-pointer" @click="router.push({name: 'login'})">Войти</p>
      </div>
      <img class="block md:hidden mb-5" :src="`logo.png`">
      <p class="text-3xl font-extrabold">Создайте аккаунт</p>
      <div class="w-full lg:px-40 p-2 mt-10">
        <input
            v-model="email"
            type="email"
            id="email"
            class="bg-gray-50 mt-2 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Введите свою почту"
            required/>

        <input
            v-model="username"
            type="username"
            id="username"
            class="bg-gray-50 mt-2 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Введите свой логин"
            required/>
        <input
            v-model="password"
            type="password"
            id="password"
            class="bg-gray-50 mt-2 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Введите пароль"
            required/>
        <Button @click="signup"class="mt-2 text-sm">
          Создать
        </Button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.text {
  width: 6ch;
  color: white;
  font-family: monospace;
  font-size: 90px;
  white-space: nowrap; /* не переносить текст на другую строку */
  overflow: hidden; /* скрываем переполнение контентом */
  border-right: 3px solid #fff;
  animation: printed_text 5s infinite;
}

@keyframes cursor {
  0% {
    border-color: white;
  }

  50% {
    border-color: transparent;
  }

  100% {
    border-color: white;
  }
}

@keyframes printed_text {
  0% {
    width: 0;
  }
  50% {
    width: 100%;
  }
  100% {
    width: 0;
  }

}

</style>