import kue from 'kue'

const blackList = ['4153518780', '4153518781']
const myQue = kue.createQueue({
    redis: {
        port: 6379,
        host: '127.0.0.1',
    }
})

function sendNotification(phoneNumber, message, job, done){
    job.progress(0, 100);

    if (blackList.includes(phoneNumber)) {
        console.log(`Phone number ${phoneNumber} is blacklisted`);
        done(Error(`Phone number ${phoneNumber} is blacklisted`));
        return;
    }else {
        job.progress(50, 100);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
        setTimeout(() => {
            done();
        }, 1000); 
    }
}

myQue.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done)
})
