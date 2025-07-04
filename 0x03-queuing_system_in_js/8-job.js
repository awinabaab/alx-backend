import { createQueue } from 'kue';

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  const jobQueue = createQueue();

  jobs.forEach((jobData) => {
    const job = jobQueue.create('push_notification_code_3', jobData)

    job.save((err) => {
      if (err) console.log(err.message);
      console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`)
    });

    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job #${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
