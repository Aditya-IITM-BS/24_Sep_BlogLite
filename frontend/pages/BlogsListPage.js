import BlogCard from "../components/BlogCard.js"

export default {
    template :`
    <div class="p-4">
        <h1> Blogs Feed 👌</h1>
        <div v-if="blogs">
        <BlogCard v-for="blog in blogs" :key="blog.id" :title="blog.title" :date="blog.timestamp" :author_email="blog['author.email']" :blog_id="blog.id" />
        </div>
        <div v-else> No blogs found </div>
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
        const res = await fetch(location.origin + '/api/feed', {
            headers : {
                'Authentication-Token' : this.$store.state.auth_token
            }
        })

        this.blogs = await res.json()
        console.log(this.blogs)
    },
    components : {
        BlogCard,
    }

}