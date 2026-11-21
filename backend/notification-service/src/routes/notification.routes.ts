import { Router } from 'express';
import { createNotificationController } from '../controllers/notification.controller.js';

const router: Router = Router();

router.post('/', createNotificationController);

export default router;