import kue from 'kue'

const notificationQueue = kue.createQueue({
    redis: {
        port: 6379,
        host: '127.0.0.1',
    }
})
function sendNotification(phoneNumber, message){
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}

notificationQueue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done()
})

