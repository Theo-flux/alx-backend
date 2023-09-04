import express from 'express'
import { createClient } from 'redis'
import {promisify} from 'util'

const PORT = 1245
const app = express()
const client = createClient()

client.on('connect', () => 
    console.log('Redis client connected to the server'
))
.on('error', (error) => 
    console.log('Redis client not connected to the server: '+ error
))

const redisClientGet = promisify(client.get).bind(client)

const listProducts = [
    {Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
    {Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
    {Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
]

const getItemById = (id) => {
    return listProducts.filter((prod) => prod.Id === id)[0]
}

const reserveStockById = (itemId, stock) => {
    client.set(itemId, stock)
}

async function getCurrentReservedStockById(itemId) {
    const stock = await redisClientGet(itemId)
    return stock

}

const transformProdList = (arr) => {
    return arr.map((prod, _) => {
        const {Id, name, price, stock} = prod;

        const transformed = {
            itemId: Id,
            itemName: name,
            price,
            initialAvailableQuantity: stock
        }

        return transformed;
    })
}

app.get('/list_products', (req, res) => {
    const newProducts = transformProdList(listProducts);
    res.statusCode = 200;
    res.json(newProducts);
})

app.get('/list_products/:itemId', async(req, res) => {
    const itemId = parseInt(req.params.itemId)
    const prod = getItemById(itemId)

    if (prod) {
        const reserve = await getCurrentReservedStockById(itemId)
        prod.currentQuantity = reserve

        res.statusCode = 200
        res.json(prod)
    }else {
        res.statusCode = 404;
        res.send({"status":"Product not found"})
    }
})

app.get('/reserve_product/:itemId', (req, res) => {
    const item = getItemById(parseInt(req.params.itemId))

    if (item) {
        if (item.stock >= 1) {
            reserveStockById(item.Id, 1)
            res.statusCode = 200
            res.send({"status":"Reservation confirmed","itemId":item.Id})
        }else {
            res.statusCode = 403
            res.send({"status":"Not enough stock available","itemId": item.Id})
        }
    }else {
        res.statusCode = 404
        res.send({"status":"Product not found"})
    }
})

app.listen(PORT, () => {
    console.log('Listening on port: ' + PORT)
})
