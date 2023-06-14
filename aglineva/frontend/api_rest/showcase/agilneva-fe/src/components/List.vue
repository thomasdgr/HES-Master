<template>
  <div class="restaurant-list">
    <h2>List of Restaurants</h2>
    <div class="button-container">
      <button @click="store.getRestaurant" class="action-button">No sort</button>
      <button @click="store.getMeanRestaurant"  class="action-button">Mean sort</button>
      <button @click="store.getAlphabeticRestaurant" class="action-button">Alphabetic sort </button>
    </div>
    <ul>
      <li v-for="(restaurant, name) in restaurants" :key="name">
        <span class="restaurant-name">{{ name }}</span>
        <ul>
          <li v-for="(nameRest, key) in restaurant" :key="key" class="menu-item">
            <span class="menu-item-key">{{ getKey(nameRest) }}</span> - <span class="grade">{{ getValue(nameRest) }}</span> 
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { computed, defineComponent, onBeforeMount, ref } from 'vue';

import {useStore} from "@/stores/store"
import { DefaultService } from '@/api';

let restaurants = ref<Record<string, Record<string, number>[]>>();
const store = useStore();

let getKey = (obj : any) => {
  const keys = Object.keys(obj);
  return keys[0]
}

let getValue = (obj : any) => {
  const val = Object.values(obj);
  return val[0]
}


store.$subscribe(() => {
  restaurants.value = store.restaurants;

});

onBeforeMount(async () => {
  store.getRestaurant()
  });
</script>


<style scoped>
.restaurant-list {
  margin-left: 20px;
}

.restaurant-name {
  font-weight: bold;
  font-size: 18px;
}

.menu-item {
  margin-left: 15px;
  list-style-type: circle;
}

.menu-item-key {
  font-weight: bold;
}

.grade {
  color: rgb(198, 198, 83);
}


.button-container {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 10px;
}

.action-button {
  margin-left: 10px;
}
</style>