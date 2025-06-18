import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';

const app = express();

const client = createClient();
client.on('error', (err) => console.error('Redis error:', err));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const queue = createQueue();

let reservationEnabled = true;

const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10);
};

reserveSeat(50);

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats.toString() });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservations are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();

    if (currentSeats > 0) {
      await reserveSeat(currentSeats - 1);
      if (currentSeats - 1 === 0) reservationEnabled = false;

      console.log(`Seat reservation job ${job.id} completed`);
      done();
    } else {
      const errMsg = 'Not enough seats available';
      console.log(`Seat reservation job ${job.id} failed: ${errMsg}`);
      done(new Error(errMsg));
    }
  });
});

app.listen(1245);
