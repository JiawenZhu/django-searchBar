<template>
  <div id='SearchApp'>
    <input type="text" v-model="search" placeholder="search a user"/>
    <!-- <div v-for="x in data"> -->
      <h3>{{name}}</h3>
    <!-- </div> -->

  </div>
</template>
<script>
import json from '../../../data.json';
var newData = JSON.parse(json);
export default {
  name: 'SearchApp',
  data () {
    return {
      name: newData,
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 input{
   width: 500px;
   height: 30px;
 }
</style>
