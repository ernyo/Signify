const express = require('express');

const router = express.Router();


// GET all workouts
router.get('/', (req, res)=>{
    res.json({"mssg":"GET all"})
})

// GET a single workout
router.get('/:id', (req, res)=>{
    res.json({"mssg":"GET one"})
})

// POST a single workout
router.post('/', (req, res)=>{
    res.json({"mssg":"POST one"})
})

// DELETE a single workout
router.delete('/:id', (req, res)=>{
    res.json({"mssg":"DELETE one"})
})

// UPDATE a single workout
router.patch('/:id', (req, res)=>{
    res.json({"mssg":"UPDATE one"})
})

module.exports = router