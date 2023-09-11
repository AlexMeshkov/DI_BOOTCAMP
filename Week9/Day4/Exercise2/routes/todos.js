const express = require("express")
const router = express.Router()
const {createTodos, putTodos, deleteTodos} = require("../controllers/products.js")


router.get("/", (req, res)=>{
    res.json(todos)
})

router.post("/", createTodos)

router.put("/:id", putTodos)

router.delete("/:id", deleteTodos)



module.exports = {router}


