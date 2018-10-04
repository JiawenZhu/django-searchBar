<template>
  <div id='SearchApp'>
    <input type="text" v-model="search" placeholder="search a user"/>
    <div v-for="x in data">
      <h3>title: {{x.fields.title}}</h3>
      <h3>description: {{x.fields.description}}</h3>
      <h3>price: {{x.fields.price}}</h3>
      <h3>summary: {{x.fields.summary}}</h3>
      <h3>timestamp: {{x.fields.timestamp}}</h3>
      <br/><br/>
    </div>

  </div>
</template>
<script>
import json from '../../../data.json';
const project = JSON.parse(json);

export default {
  name: 'SearchApp',
  data () {
    return {
      // title: '',
      // description: '',
      // price: '',
      // summary: '',
      // timestamp: '',
      data: project
    }
  },
  method: {
      title: function(){
        return 'title: ';
        // Object.keys(this.newData).forEach(function(key){
          // var value = obj[key];
        // });
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
