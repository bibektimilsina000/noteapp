<template>
  <headerComp />
  <div class="bg-gray-900 h-screen text-justify">
    <div>
      <label class="text-white mx-6 font-black text-2xl my-6" for="heading">
        Note Title:
      </label>
      <input type="text" name="heding" id="heading" v-model="title" />
    </div>

    <label
      class="text-white float-left my-6 ml-6 font-black text-4xl"
      for="text"
      >Note:</label
    >
    <textarea
      v-model="text"
      class="rounded-lg m-6 border-2 border-gray-800"
      name="text"
      id="text"
      cols="90"
      rows="10"
    ></textarea>

    <button
      class="rounded py-1 px-2 border-2 border-gray-800 text-white my-10 hover:bg-blue-500"
    >
      Add note
    </button>

    <div class="p-4 md:w-1/3">
      <div class="h-full border-2 border-gray-800 rounded-lg overflow-hidden">
        {{ result }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import headerComp from "./headerComp.vue";
export default {
  name: "homeComp",
  data() {
    return {
      title: "",
      text: "",
      result: [],
    };
  },

  components: {
    headerComp,
  },

  async mounted() {
    await axios({
      method: "get",
      url: "http://127.0.0.1:8000/",
      auth: {
        username: "admin",
        password: "admin",
      },
    }).then((response) => (this.result = response.data));

    console.log(this.result);
  },
};
</script>

<style></style>
