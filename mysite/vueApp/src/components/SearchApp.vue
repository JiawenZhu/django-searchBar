<template>
  <div id='SearchApp'>
    <input ref="search" type="text" v-model="search" placeholder="search a title"/>
    <div v-for="x in data">
      {{x}}
    </div>
  </div>
</template>

<script>
import json from '../../../data.json';
const projects = JSON.parse(json);
var search = '';

var filteredData = projects.filter(function (project) {
  return (project.fields.title.includes('water') && project.fields.price.includes(''));
});

export default {
  name: 'SearchApp',
  data () {
  
    return {
      data : filteredData,
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
