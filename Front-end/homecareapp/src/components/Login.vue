<template>

    <div class="login_user">
        <div class="container_login_user">
            <h2>Iniciar sesión</h2>

            <form v-on:submit.prevent="processLoginUser">
                <input type="text" v-model="user.username" placeholder="Username">
                <br>
                <input type="password" v-model="user.password" placeholder="Password">
                <br>
                <button type="submit">Iniciar Sesion</button>
            </form>

        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: "Login",

    data: function(){
        return {
            user:{
                username:"",
                password:""
            }
        }
    },

    methods: {
        processLoginUser: function(){
            axios.post(
                "https://slydevelopers-homecareapp.herokuapp.com/login/",
                this.user,
                {headers: {}}
                )
                .then((result) => {
                    let dataLogin = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    this.$emit('completedLogin', dataLogin)
                })
                .catch((error) => {
                    if(error.response.status == "401")
                        alert("ERROR 401: Credenciales Incorrectas.");
                }
            );
        }
    }
}
</script>

<style>
    .login_user{
        margin: 0%;
        padding: 0;
        width: 100%;
        height: 100%;
        min-height: 100px;

        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_login_user {
        border: 3px solid #283747;
        border-radius: 10px;
        width: 25%;
        height: 60%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .login_user h2{
        color: #283747;
    }

    .login_user form{
        width: 70%;
    }

    .login_user input{
        height: 40px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;

        border: 1px solid #283747;
    }

    .login_user button{
        width: 100%;
        height: 40px;

        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0;
    }
    .login_user button:hover{
        color: #E5E7E9;
        background: crimson;
        border: 1px solid #283747;
    }

</style>