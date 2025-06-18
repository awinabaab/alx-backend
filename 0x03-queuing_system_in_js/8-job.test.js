import { createQueue } from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = createQueue();
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
    expect(() => createPushNotificationsJobs(null, queue)).to.throw(Error, 'Jobs is not an array');
    expect(() => createPushNotificationsJobs('string', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs in the queue for each job data object', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Test message 1' },
      { phoneNumber: '0987654321', message: 'Test message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(jobs.length);

    jobs.forEach((jobData, index) => {
      const job = queue.testMode.jobs[index];
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.deep.equal(jobData);
    });
  });
});
