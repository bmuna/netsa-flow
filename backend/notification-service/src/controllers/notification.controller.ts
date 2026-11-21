
import type { Request, Response } from 'express';
import { notificationSchema } from '../schemas/notification.schema.js';

export function createNotification(req: Request, res: Response) {
  const result = notificationSchema.safeParse(req.body);

  if (!result.success) {
    return res.status(400).json({
      message: 'Invalid notification data',
      errors: result.error.issues,
    });
  }

  return res.status(202).json({
    message: 'Notification accepted',
  });
}
