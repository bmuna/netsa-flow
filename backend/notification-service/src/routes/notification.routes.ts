import { Router } from 'express';
import { createNotification } from '../controllers/notification.controller.js';

const router: Router = Router();

router.post('/', createNotification);

export default router;