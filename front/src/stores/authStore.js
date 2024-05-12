import { defineStore } from 'pinia'

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
            console.log(123)
            const data = await axios.get('api/users/1')
            console.log(data);
        }
    }

})