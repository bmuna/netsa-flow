
import type { Request, Response } from 'express';
import { notificationSchema } from '../schemas/notification.schema.js';
import { createNotification } from '../services/notification.service.js';

export async function createNotificationController(
  req: Request,
  res: Response,
) {
  const result = notificationSchema.safeParse(req.body);

  if (!result.success) {
    return res.status(400).json({
      message: 'Invalid notification data',
      errors: result.error.issues,
    });
  }

  await createNotification(result.data);

  return res.status(202).json({
    message: 'Notification accepted',
  });
}
