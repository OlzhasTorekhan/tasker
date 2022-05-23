<template>
  <div class="container">
    <div class="todo_header">
      <h1><a href="#">Tasker</a></h1>
      <input class="todo_header_search" type="text" placeholder="Search" />
    </div>
    <section class="app">
      <div class="todo_list">
        <ul>
          <li><span>Make first page</span> <input type="checkbox" /></li>
          <li><span>Make minimal design</span> <input type="checkbox" /></li>

        </ul>
      </div>
      <div class="todo_menu">
        <ul>
          <li><a href="#">Main</a></li>
          <li><a href="#">Settings</a></li>
          <li><a href="#">Friends</a></li>
          <li><a href="#">Visibility</a></li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "tasker",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
* {
  margin: 0;
  padding: 0;
  overflow: hidden;
}

a {
  text-decoration: none;
  color: white;
}
.todo_header {
  display: flex;
  align-content: center;
  justify-content: center;
  padding: 5px;
  gap: 10px;
  background-color: #3083dcff;
  top: 0;
  position: fixed;
  width: 100%;
  
}
.todo_header + .app {
  padding-top: 45px;
}
.todo_header .todo_header_search {
  background-color: inherit;
}
.todo_header .todo_header_search::placeholder {
  color: white;
}
.todo_header .todo_header_search:hover {
  background-color: lightgray;
}
.todo_list {
  background-color: #7dde92ff;
  width: 80vw;
}
.todo_list ul {
  display: flex;
  flex-direction: column;
  align-items: center;
  border:thin solid black;
  border-radius:5px;
  margin:10px;
  padding: 0 0 10px;
}
.todo_list ul li {
  display: flex;
  justify-content: space-between;
  width: 20%;
  color: white;
  margin: 10px 0 0 0;
  padding: 10px;
  flex-wrap: nowrap;
  gap: 10px;
  white-space: nowrap;
  border: thin solid #f8ffe5ff;
}
li {
  display: flex;
  flex-wrap: wrap;
  padding: 10px 0 10px 0;
  margin: 0 10px;
}
.app {
  display: flex;
  height: 150vh;
}

.todo_menu {
  background-color: #2ebfa5ff;
  width: 20vw;
}
.todo_menu ul {
  position: fixed;
}
</style>
