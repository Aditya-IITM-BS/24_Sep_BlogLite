import { fetchWithAuth } from "../utils/fetchWithAuth.js"
import User from "../components/User.js"

export default {
    template : `<div class="p-4">
            <h1> Users </h1>
            <input placeholder="search" @input="search" v-model="searchQuery"/>
            <User v-for="user in users" :key="user.id" :email="user.email" :id="user.id" :followers="user.num_following" :posts="user.num_post" />
        </div>`,
    data(){
        return {
            users : [],
            searchQuery : null,
        }
    },
    methods : {
        async search(){
            const res = await fetchWithAuth('/api/users?query='+this.searchQuery)
            if (res.ok){
                this.users = await res.json()
            }else {
                console.warn('error fetching ')
            }
        }
    },

    async mounted(){
        console.log('mounted ran')
        const res = await fetchWithAuth('/api/users')
        this.users = await res.json()
    },

    components : {
        User,
    }

}