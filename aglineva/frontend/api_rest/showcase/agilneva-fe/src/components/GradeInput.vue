<template>
  <div>
    <input class="input-field" v-model="grade.resto" type="text" placeholder="Resto">
    <input class="input-field" v-model="grade.name" type="text" placeholder="Name">
    <input class="input-field" v-model.number="grade.grade" type="number" placeholder="Grade" min="0" max="5">
    <button class="submit-button" @click="validateInputs">Submit</button>
    <div v-if="showError" class="error-message">All inputs must be filled!</div>
  </div>
</template>

<script setup lang="ts">
import { DefaultService, type Grade } from '@/api';
import { ref } from 'vue';
import {useStore} from "@/stores/store"

const store = useStore();


let grade: Grade = {
  resto: '',
  name: '',
  grade: 0,
};
let showError = ref<boolean>(false);

function validateInputs() {
  if (grade.resto && grade.name && grade.grade !== 0) {
    showError.value = false;
    DefaultService.addGrade(grade).then(() => {
      store.getRestaurant()
    })
    
  } else {
    showError.value = true;
  }
}
</script>

<style scoped>
.input-field {
  width: 200px;
  padding: 8px;
  margin-bottom: 10px;
}

.submit-button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

.error-message {
  color: red;
}
</style>
