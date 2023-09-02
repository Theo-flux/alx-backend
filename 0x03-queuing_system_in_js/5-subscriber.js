import { createClient } from "redis";

const subscriber = createClient()

subscriber.on('connect', () => console.log('Redis client connected to server'))
.on('error', (error) => console.log('Redis client not connected to server: ' + error))

subscriber.subscribe('holberton school channel')
subscriber.on('message', (channel, msg) => {
    console.log(msg)
    if (msg === 'KILL_SERVER') {
        subscriber.unsubscribe(channel)
        subscriber.end(true)
    }
})