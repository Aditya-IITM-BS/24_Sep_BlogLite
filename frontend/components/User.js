import { fetchWithAuth } from "../utils/fetchWithAuth.js"

export default {
    props : ['email', 'followers', 'id', 'posts'],
    template : `
    <div class="jumbotron">
        <h2> {{email}} </h2>
        <hr>
        <p> followers {{followers}} </p>
        <p> Posts {{posts}} </p>
        <button class="btn btn-info btn-lg" @click="sendFollow">Follow </button>
        <button class="btn btn-warn btn-lg" @click="sendUnfollow">Un-Follow </button>
    </div>
    `,
    methods : {
        async sendFollow(){
            const res = await fetchWithAuth('/follow/' + this.id)

            if (res.ok){
                // add popup
                console.log('user followed')
            }
        },
        async sendUnFollow(){
            const res = await fetchWithAuth('/unfollow/' + this.id)

            if (res.ok){
                // add popup
                console.log('user un-followed')
            }
        }
    }
}