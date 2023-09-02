import { createClient } from "redis";
import { promisify } from 'util'

const client = createClient();
client.on('connect', () => 
    console.log('Redis client connected to the server'
))
.on('error', (error) => 
    console.log('Redis client not connected to the server: '+ error
))

function setNewSchool(schoolName, value){
    client.set(schoolName, value)
}

const get = promisify(client.get).bind(client)

function displaySchoolValue(schoolName){
    get(schoolName)
    .then(res => console.log(res))
    .catch((err) => {
        console.log(err);
        throw err;
    })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
