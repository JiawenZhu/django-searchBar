<template>
  <div id='SearchApp'>
    <input type="text" v-model="search" placeholder="search a title"/>
    <div v-for="filter in filtered" :key="filter.id">
      <span>{{filter}}</span>
    </div>
  </div>
</template>

<script>
import json from '../../../data.json';
const products = JSON.parse(json);

export default {
  name: 'SearchApp',
  data () {  
    return {
      filteredData : [],
      search: ''
    }
  },
  created(){
    this.filteredData= products
  },
  computed: {
    filtered: function(){
        return this.filteredData.filter(function (product) {
          return product.fields.title.match(app.this.search);
          // return product.fields.title.match('water');
          // return (product.fields.title.match('water') || product.fields.price.match('25'));
      });
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
