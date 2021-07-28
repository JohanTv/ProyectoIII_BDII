const fs = require('fs');
const express = require('express');
const router = express.Router();
const axios = require('axios');

const PostAPI = 'https://jsonplaceholder.typicode.com';


router.get('/', (req, res)=>{
    res.send('it works');
})

router.get('/posts', (req, res)=>{
    const data = JSON.parse(fs.readFileSync('./src/pythonCode/initial_db.json'));
    res.json(data);
})

router.get('/send', (req, res)=>{
    const newData = JSON.parse(fs.readFileSync('./src/pythonCode/result_db.json'));
    //res.json(newData);
    res.json(newData);
})

module.exports = router;