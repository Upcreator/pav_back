<script setup>

import Header from "../components/Header.vue";
import {ChartBarIcon, ClockIcon, WrenchScrewdriverIcon} from "@heroicons/vue/24/solid/index.js";
import Button from "../components/Button.vue";
import router from "@/router.js";


</script>

<template>
  <div class="">
    <Header></Header>
    <div class="max-w-5xl p-1 m-auto my-5">
      <div class="flex justify-center">
        <p class="text-center font-extrabold text">PavApp</p>
      </div>
      <Button @click="router.push({name: 'signup'})" class="mt-10">Создать первую заявку</Button>
      <!--      <p class="text-center text-7xl text-white font-bold tracking-wide mt-5">PavApp</p>-->
      <div
          class="bg-gray-900/70 mt-5 gap-5 grid md:grid-cols-3 border border-gray-700/90 shadow-xl text-white p-5 rounded-2xl">
        <div class="shadow border border-gray-900 p-2 flex flex-col rounded-2xl">
          <div class="flex items-center">
            <WrenchScrewdriverIcon class="h-20"/>
            <p>Создание надёжного сервиса</p>
          </div>
          <p class="m-2">Наш сервис позволит сделать тех.поддержку вашей организации</p>
        </div>
        <div class="shadow border border-gray-900 p-2 flex flex-col rounded-2xl">
          <div class="flex items-center">
            <ClockIcon class="h-20"/>
            <p>Экономия времени</p>
          </div>
          <p class="m-2">Эффективная и быстрая поддержка залог рационального использования времени</p>
        </div>
        <div class="shadow border border-gray-900 p-2 flex flex-col rounded-2xl">
          <div class="flex items-center">
            <ChartBarIcon class="h-20"/>
            <p>Удобная аналитики</p>
          </div>
          <p class="m-2">
            Мы предоставляем инструменты аналитики с целью оптимизации процесса тех. поддержки
          </p>
        </div>
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
  animation: cursor 0.75s step-end infinite, printed_text 1s steps(6);
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
  from {
    width: 0;
  }
}

</style>