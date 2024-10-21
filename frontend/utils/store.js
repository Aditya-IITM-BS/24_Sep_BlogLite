const store = new Vuex.Store({
    state : {
        // like data
        auth_token : null,
        role : null,
        loggedIn : false,
        user_id : null,
    },
    mutations : {
        // functions that change state
        setUser(state) {
            try{
             if (JSON.parse(localStorage.getItem('user'))){
                const user = JSON.parse(localStorage.getItem('user'));
                state.auth_token = user.token;
                state.role = user.role;
                state.loggedIn = true;
                state.user_id = user.id;
             }
            } catch {
                console.warn('not logged in')
        }         
        },

        logout(state){
            state.auth_token = null;
            state.role = null;
            state.loggedIn = false;
            state.user_id = null;

            localStorage.removeItem('user')
        }
    },
    actions : {
        // actions commit mutations can be async
    }
})

store.commit('setUser')

export default store;