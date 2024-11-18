export default {
    props : ['title', 'author_email', 'date', 'blog_id'],
    template : `
    <div class="jumbotron">
        <h2 @click="$router.push('/blogs/' + blog_id)"> {{title}} </h2>
        <p> {{author_email}} </p>
        <hr>
        <p> Published : {{formattedDate}}</p>
    </div>
    `,
    computed: {
        formattedDate(){
            return new Date(this.date).toLocaleString();
        }
    }
}