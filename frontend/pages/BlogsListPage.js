import BlogCard from "../components/BlogCard.js"

export default {
    template :`
    <div class="p-4">
        <h1> Blogs List 👌</h1>
        <BlogCard v-for="blog in blogs" :title="blog.title" :date="blog.timestamp" :author_id="blog.user_id" :blog_id="blog.id">
    </div>
    `,
    data(){
        return {
            blogs : []
        }
    },
    methods : {

    },
    async mounted(){
        const res = await fetch(location.origin + '/api/blogs', {
            headers : {
                'Authentication-Token' : this.$store.state.auth_token
            }
        })

        this.blogs = await res.json()
    },
    components : {
        BlogCard,
    }

}