//filename: lab_passgen.js

'use strict' // enables strict mode for testing, will be removed

const upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

const lower = 'abcdefghijklmnopqrstuvwxyz'

const numbers = '0123456789'

const special = '!?#$%&~'

// let upperNum = document.querySelector("#upperNum")

// let lowerNum = document.querySelector("#lowerNum")

// let numberNum = document.querySelectoy("#numberNum")

// let specialNum = document.querySelector("#specialNum")

// let includeThis = document.querySelector("#includeThis")

function produce(upperNum,lowerNum,numberNum,specialNum,includeThis) {

    let product = ''
    
    for (let i = 0; i < upperNum; i++) {product += upper[Math.floor(Math.random() * upper.length)]}

    for (let i = 0; i < lowerNum; i++) {product += lower[Math.floor(Math.random() * lower.length)]}

    for (let i = 0; i < numberNum; i++) {product += numbers[Math.floor(Math.random() * numbers.length)]}

    for (let i = 0; i < specialNum; i++) {product += special[Math.floor(Math.random() * special.length)]}

    product = product.toString()
    console.log(typeof product)
   
    for (let i = 0; i < product.length; i++) {
        if (Math.round(Math.random())) {
        let character = product[i]
        product -= product[i]
        product = product.split('')
        product.splice(Math.floor(Math.random() * product.length), 0, character)
        }
    }

    product += includeThis
    
    return product
}

console.log(produce(3,3,3,3,'fucks'))
