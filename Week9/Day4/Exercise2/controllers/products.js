const todos = [
    {id:1, name: 'Alex', model: 'bmw'},
    {id:2, name: 'Mike', model: 'mercedes'},
    {id:3, name: 'Tyson', model: 'honda'},
];

const createTodos = (req, res) => {
   const {name, model}= req.body;
   console.log(req.body)
   const newtodos = {id: todos.length +1,name, model}
    todos.push(newtodos)
    res.json(todos)
}

const putTodos =  (req, res)=>{
    console.log("req recieved")
    console.log(req.params)
    const {id} = req.params
  const {name, model }= req.body
    const index = todos.findIndex((el)=> el.id == id)
    // todos[index] =   {}
console.log(name + " " + model);
    res.json("ok")
}

const deleteTodos = (req, res)=>{
    const {id} = req.params.id
    const idDelete = todos.findIndex((el)=>el.id == id )
    todos.splice(idDelete, 1)
    res.json(todos)
}

module.exports = {
    createTodos, putTodos, deleteTodos
}