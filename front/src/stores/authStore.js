import { defineStore } from 'pinia'
import axios from "axios";
import {jwtDecode} from "jwt-decode";

// You can name the return value of `defineStore()` anything you want,
// but it's best to use the name of the store and surround it with `use`
// and `Store` (e.g. `useUserStore`, `useCartStore`, `useProductStore`)
// the first argument is a unique id of the store across your application
export const useAuthStore = defineStore('authStore', {
    state() {
        return {
            user: null
        }
    },
    actions: {
        async getUser(){
            const token = localStorage.getItem('access_token')
            if(token){
                this.user = jwtDecode(token)
                return;
            }
            throw DOMException("Unauth.")
        }
    }

})