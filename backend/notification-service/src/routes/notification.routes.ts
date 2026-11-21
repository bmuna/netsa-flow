
import { Router } from 'express';
import { notificationSchema } from '../schema/ notification.schema.js';

const router: Router = Router();

router.post('/',  (req, res) => {
    const result = notificationSchema.safeParse(req.body);
    
    if (!result.success) {
    return res.status(400).json({
      message: 'Invalid notification data',
      errors: result.error.issues,
    });
  }

  res.status(202).json({
    message: 'Notification accepted'
  });
});

export default router;
