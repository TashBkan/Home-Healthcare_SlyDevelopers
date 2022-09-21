import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import App from './App.vue'

import Login from './components/Login.vue'
import Registro from './components/Registro.vue'
import Home from './components/Home.vue'
import User from './components/User.vue'

const routes = [{
    path: '/',
    name: 'root',
    component: App
  },
  {
    path: '/user/login',
    name: "login",
    component: Login
  },
  {
    path: '/user/registro',
    name: "registro",
    component: Registro
  },
  {
    path: '/user/home',
    name: "home",
    component: Home
  },
  {
    path: '/user',
    name: "user",
    component: User
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;