import { createClient } from "redis";
import kue from 'kue';

const push_notification_code = kue.createQueue()

const job = push_notification_code.create('job', {
    phoneNumber: '34567890',
    message: 'my first kue job',
})

job.save((error) => {
    if (!error) {
        console.log('Notification job created: ' + job.id)
    }
})

job.on('complete', () => console.log('Notification job completed'))
job.on('failed', () => console.log('Notification job failed'))
