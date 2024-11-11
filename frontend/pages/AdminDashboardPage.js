export default {
    template : `
        <div>
            <h1> this is admin dashboard </h1>
            <button @click="create_csv"> Get Blog Data </button>
        </div>
    `, 
    methods : {
        async create_csv(){
            const res = await fetch(location.origin + '/create-csv', {
                headers : {
                    'Authentication-Token' : this.$store.state.auth_token
                }
            })
            const task_id = (await res.json()).task_id

            const interval = setInterval(async() => {
                const res = await fetch(`${location.origin}/get-csv/${task_id}` )
                if (res.ok){
                    console.log('data is ready')
                    window.open(`${location.origin}/get-csv/${task_id}`)
                    clearInterval(interval)
                }

            }, 100)
            
        },
    },
}