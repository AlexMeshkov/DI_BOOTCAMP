const express = require("express")
const app = express()
const {router} = require("./routes/index.js")
const PORT = 3000

app.listen(PORT, ()=> {
    console.log(`run on port ${PORT}`)
})

app.use("/", router)