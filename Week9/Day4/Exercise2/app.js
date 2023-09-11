const express = require("express")
const {router} = require("./routes/todos.js")

const app = express()
app.use(express.json())
const PORT = 3000

app.listen(PORT, ()=> {
    console.log(`run on port ${PORT}`)
})

app.use("/", router)
