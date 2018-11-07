<template>
  <div id='SearchApp'>
    <input type="text" v-model="search" placeholder="search a title, descritopn, price, summary or time"/>
    <div v-for="filter in filtered" :key="filter.id">
      <span class='project'>{{filter}}</span>
    </div>
  </div>
</template>

<script>
import json from '../../data.json';
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
      const app = this;
        return this.filteredData.filter(function (product) {
            return (product.fields.title.match(app.search)       ||
                    product.fields.description.match(app.search) ||
                    product.fields.price.match(app.search)       ||
                    product.fields.summary.match(app.search)     ||
                    product.fields.timestamp.match(app.search)
            );          
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
 .project{
  box-shadow: rgba(0, 0, 0, 0.117647) 0px 1px 6px, rgba(0, 0, 0, 0.117647) 0px 1px 4px;
  max-width: 124px;
  margin: 12px;
  transition: .15s all ease-in-out;   
 }

</style>
