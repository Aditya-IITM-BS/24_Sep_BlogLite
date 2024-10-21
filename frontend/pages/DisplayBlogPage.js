export default {
    props : ['id'],
    template : `
    <div>
        <h1> {{blog.title}} </h1>
        <p> Published : {{formattedDate}} </p>
        <img width="150" v-bind:src="blog.image_url" />
        <p> {{blog.caption}} </p>
    </div>
    `,
    data(){
        return {
            blog : {},
        }
    },
    computed : {
        formattedDate(){
            return new Date(this.blog.timestamp).toLocaleString();
        }
    },
    async mounted(){
        const res = await fetch(`${location.origin}/api/blogs/${this.id}`, {
            headers : {
                'Authentication-Token' : this.$store.state.auth_token
            }
        })
        if (res.ok){
            this.blog = await res.json()
        }
    }
}