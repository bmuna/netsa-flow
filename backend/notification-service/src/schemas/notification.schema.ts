
import { z } from 'zod';

export const notificationSchema = z.object({
  recipient: z.string().email(),
  channel: z.enum(['EMAIL']),
  subject: z.string().trim().min(1),
  message: z.string().trim().min(1),
});

export type NotificationInput = z.infer<typeof notificationSchema>;