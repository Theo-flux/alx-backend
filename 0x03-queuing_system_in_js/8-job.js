export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        console.log('Jobs is not an array')
    }else {
        jobs.forEach((jobData, _) => {
            const job = queue.create('push_notification_code_3', jobData)

            job.save((err) => {
                if (!err) {
                    console.log(`Notification job created: ${job.id}`)
                }
            })

            job.on('complete', () => {
                console.log(`Notification job JOB_ID completed`)
            })

            job.on('failed', (err) => {
                console.log(`Notification job JOB_ID failed: ${err}`)
            })

            job.on('progress', (progress) => {
                console.log(`Notification job JOB_ID ${progress}% complete`)
            })
        })
    }
}