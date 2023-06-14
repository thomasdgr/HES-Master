import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { DefaultService } from '@/api';

export const useStore = defineStore('store', () => {
  let restaurants = ref<Record<string, Record<string, number>[]> | undefined>(undefined);


  let getRestaurant = async () => {
    restaurants.value = await DefaultService.listRestaurants();
  }

  let getMeanRestaurant = async () => {
    restaurants.value = await DefaultService.sortRestaurantsMean();
  }

  let getAlphabeticRestaurant = async () => {
    restaurants.value = await DefaultService.sortRestaurants();
  }

  return { restaurants, getRestaurant, getMeanRestaurant, getAlphabeticRestaurant }
})
