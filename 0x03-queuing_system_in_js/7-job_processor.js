import { createQueue } from 'kue';

function sendNotification(phoneNumber, message, job, done) {
  const queue = createQueue();
  const blacklist = ['4153518780', '4153518781'];

  job.progress(0, 100);

  if (blacklist.includes(phoneNumber)) {
    return (done(new Error(`Phone number ${phoneNumber} is blacklisted`)));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  setTimeout(() => {
    done();
  }, 1000);
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
