import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: '0123456789',
  message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', jobData)

job.save((err) => {
  if (err) console.log(`Error creating job: ${err.message}`);
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
