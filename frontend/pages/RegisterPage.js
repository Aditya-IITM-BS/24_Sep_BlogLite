export default {
    template : `
    <div>
        <input placeholder="email"  v-model="email"/>  
        <input placeholder="password"  v-model="password"/>  
        <input placeholder="role"  v-model="role"/>  
        <button @click="submitLogin"> Register </button>
    </div>
    `,
    data(){
        return {
            email : null,
            password : null,
            role : null,
        } 
    },
    methods : {
        async submitLogin(){
            const res = await fetch(location.origin+'/register', 
                {method : 'POST', 
                    headers: {'Content-Type' : 'application/json'}, 
                    body : JSON.stringify({'email': this.email,'password': this.password, 'role' : this.role})
                })
            if (res.ok){
                console.log('we are register')
            }
        }
    }
}