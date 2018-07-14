const express = require('express')
const axios = require('axios')
const app = express()

const QUOTES_API_GATEWAY = process.env.QUOTES_API

app.get('/api/status', (req, res) => {
    return res.json({status: 'ok'})
})

app.get('/api/randomquote',async (req, res) => {
    try {
        const url = QUOTES_API_GATEWAY + '/api/quote'
        const quote = await axios.get(url)
        return res.json({
            time: Date.now(),
            quote: quote.data
        })
    } catch (error) {
        console.log(error)
        res.status(500)
        return res.json({
            message: "Internal server error",
        })
    }
    
})

app.listen(3000, () => {
    console.log('API Gateway is listening on port 3000!')
})