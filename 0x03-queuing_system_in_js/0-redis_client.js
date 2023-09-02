import { createClient } from 'redis';

export function redisCreateClient(){
    const client = createClient();
    client.on('connect', () => 
        console.log('Redis client connected to the server'
    ))
    .on('error', (error) => 
        console.log('Redis client not connected to the server: '+ error
    ))
}

redisCreateClient()
