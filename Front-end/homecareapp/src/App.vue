<template>
  <div id="app" class="app">

    <div class="header">
      <h1>Cuidado en Casa</h1>
      <nav>
        <button v-if="is_HomeCare" > Cuenta </button>
        <button v-if="is_HomeCare" v-on:click="loadHome"> Inicio </button>
        <button v-if="is_HomeCare" v-on:click="logOut"> Cerrar Sesión </button> 
        <button v-if="!is_HomeCare" v-on:click="loadLogin"> Iniciar Sesión </button>
        <button v-if="!is_HomeCare" v-on:click="loadRegistro"> Registrarse </button>
      </nav>
    </div>


    <div class="main-component">
      <router-view
        v-on:completedLogin="completedLogin"
        v-on:completedRegistro="completedRegistro"
      >
      </router-view>
    </div>


    <div class="footer">
      <h2>Tu cuidado nuestro compromiso</h2>
    </div>

  </div>
</template>


<script>
export default {
  name: 'App',

  data: function(){
    return{
      is_HomeCare: false
    }
  },

  components: {  
  },

  methods:{
    verifyAuth: function() {
      this.is_HomeCare = localStorage.getItem("isAuth") || false;

      if(this.is_HomeCare == false)
        this.$router.push({name: "login"});
      else
        this.$router.push({name: "home"});
    },

    loadLogin: function(){
      this.$router.push({name: "login"});
    },

    loadRegistro: function(){
      this.$router.push({name: "registro"});
    },

    completedLogin: function(data) {
      localStorage.setItem("isAuth", true)
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autentificación Exitosa");
      this.verifyAuth();
    },

    completedRegistro: function(data) {
      alert("Registro Exitoso");
      this.completedLogin(data);
    },

    loadHome: function(){
      this.$router.push({name: "home"});
    },
        
    logOut: function () {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    }

  },

  created: function(){
    this.verifyAuth()
  }
}
</script>

<style>
  .body{
    margin: 0 0 0 0;
  }

  .header{
    margin: 0%;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;

    background-color: #283747;
    color: #E5E7E9;

    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header h1{
    width: 20%;
    text-align: center;
  }

  .header nav{
    height: 100%;
    width: 20%;

    display: flex;
    justify-content: space-around;
    align-items: center;

    font-size: 20px;
  }
  
  .header nav button{
    color: #E5E7E9;
    background: #283747;
    border: 1px solid #E5E7E9;

    border-radius: 5px;
    padding: 10px 20px;
  }

  .header nav button:hover{
    color: #283747;
    background: #E5E7E9;
    border: 1px solid #E5E7E9;
  }

  .main-component{
    height: 75vh;
    margin: 0%;
    padding: 0%;

    background: #FDFEFE;
  }

  .footer{
    margin: 0%;
    padding: 0%;
    width: 100%;
    height: 10vh;
    min-height: 100px;

    background: #283747;
    color: #E5E7E9;
  }

  .footer h2{
    height: 100%;
    width: 100%;

    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>