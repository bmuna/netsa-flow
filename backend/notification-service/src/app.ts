
import express, { type Express } from 'express';
import notificationRoutes from './routes/notification.routes.js';

const app: Express = express();

app.use(express.json());

app.get('/health', (_req, res) => {
  res.json({ status: 'ok' });
});

app.use('/notifications', notificationRoutes);

export default app;
