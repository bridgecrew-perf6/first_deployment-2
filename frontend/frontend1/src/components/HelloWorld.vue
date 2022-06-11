<template>
  <div class="hello">
    <input 
    v-model="animalName"
    type="text" id="nameInput">
    <input
    v-model="imageUrl"
    type="text" id="imageInput">
    <button @click="postAnimal">POST</button>
    <button @click="getAnimal">GET</button>
  <div
  v-for="animal in animalArr"
  :key="animal.animalId">
  {{animal.animalId}}
  <h1>{{animal.name}}</h1>
  <img :src="animal.imageUrl">
  </div>    
  </div>

</template>

<script>
import axios from 'axios' 

export default {
  name: 'HelloWorld',
  data(){
    return{
      animalName: null,
      imageUrl: null,
      animalArr: []
    }
  },
  methods: {
    postAnimal() {
      axios.request({
      url : "http://127.0.0.1:5000/api/animal",
      method : "POST",
      data: {
        animalName : this.animalName,
        imageUrl: this.imageUrl
      }
    }).then(()=>{
      this.getAnimals();
    }).catch((error)=>{
      console.log(error);
    })
    },
    getAnimals(){
      axios.request({
        url : "http://127.0.0.1:5000/api/animal",
        method : "GET",
    }).then((response)=>{
      this.animalArr = response.data
    }).catch((error)=>{
      console.log(error);
    })
    }
  },
  mounted() {
    this.getAnimals()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
