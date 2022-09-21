<template>

    <div class="registro_user">
        <div class="container_registro_user">
            <h2>Registrarse</h2>

            <form v-on:submit.prevent="processRegistro">
                <input type="text" v-model="user.rol" placeholder="Rol">
                <br>
                <input type="text" v-model="user.username" placeholder="Username">
                <br>
                <input type="password" v-model="user.password" placeholder="Password">
                <br>
                <input type="text" v-model="user.nombres" placeholder="Name">
                <br>
                <input type="text" v-model="user.apellidos" placeholder="Lastname">
                <br>
                <input type="number" v-model="user.telefono" placeholder="Phone">
                <br>
                <input type="text" v-model="user.genero" placeholder="Gender">
                <br>
                <button type="submit">Registrarse</button>
            </form>

        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default{
    name: "Registro",

    data: function(){
        return {
            user: {
                rol: "",
                username: "",
                password: "",
                nombres: "",
                apellidos: "",
                telefono: "",
                genero: ""
            }
        }
    },

    methods: {
        processRegistro: function(){
            axios.post(
                "https://slydevelopers-homecareapp.herokuapp.com/user/",
                this.user,
                {headers: {}}
            )
                .then((result) => {
                    let dataRegistro = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    this.$emit('completedRegistro', dataRegistro)
                })
                .catch((error) => {
                    console.log(error)
                    alert("ERROR: Fallo en el registro");
                });
        }
    }
}
</script>

<style>
    .registro_user{
        margin: 0%;
        padding: 0;
        width: 100%;
        height: 100%;

        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_registro_user {
        border: 3px solid #283747;
        border-radius: 10px;
        width: 25%;
        height: 70%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .registro_user h2{
        color: #283747;
    }

    .registro_user form{
        width: 70%;
    }

    .registro_user input{
        height: 40px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;

        border: 1px solid #283747;
    }

    .registro_user button{
        width: 100%;
        height: 40px;

        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0 25px 0;
    }
    .registro_user button:hover{
        color: #E5E7E9;
        background: crimson;
        border: 1px solid #283747;
    }

</style>