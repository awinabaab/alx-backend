import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`)
});

client.subscribe('ALXchannel', (err, count) => {
  if (err) console.log(err.message);
})

client.on('message', (channel, message) => {
  if (message == 'KILL_SERVER') {
    client.unsubscribe('ALXchannel', (err, count) => {
      if (err) console.log(err.message);
    })
    client.quit();
  }
  console.log(message);
});
