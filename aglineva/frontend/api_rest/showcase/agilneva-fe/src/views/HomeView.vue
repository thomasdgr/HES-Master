<script setup lang="ts">
import List from '../components/List.vue'
import GradeInput from '@/components/GradeInput.vue';
</script>

<template>
  <main>
    <div class="left">
      <List />
    </div>

    <div class="right">
      <GradeInput/>
    </div>
    
  </main>
</template>

<style>

main{
  width: 100%;
}

.left{
  width : 50%;
  float: left;
}

.right{
  padding-left: 100px;
  padding-top: 300px;
  
  width : 50%;
  height: auto;

  float: right;
}


</style>