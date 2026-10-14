import logging
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils import timezone
from django.template.loader import render_to_string

from .models import Alert, Incident

logger = logging.getLogger(__name__)


class AlertService:
    """Service for managing alerts and sending notifications."""

    def send_notification(self, alert: Alert) -> bool:
        """
        Send email notification for an alert.
        
        Args:
            alert: The alert to notify about
            
        Returns:
            True if notification sent successfully
        """
        try:
            website = alert.website
            user = website.user
            
            # Collect notification emails
            recipients = [user.email]
            
            # Add additional notification emails from website settings
            if website.notification_emails:
                recipients.extend(website.notification_emails)

            # Add the configured security operations contact without replacing
            # the website owner's configured recipients.
            if settings.ALERT_NOTIFICATION_EMAIL:
                recipients.append(settings.ALERT_NOTIFICATION_EMAIL)
            
            # Remove duplicates
            recipients = list(set(recipients))
            
            # Prepare email content
            subject = f"[Deface Spy] {alert.severity.upper()}: {alert.title}"
            
            message = self._build_email_message(alert)
            html_message = self._build_html_email_message(alert)
            
            # Send email
            email = EmailMultiAlternatives(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipients,
            )
            email.attach_alternative(html_message, 'text/html')
            email.send(fail_silently=False)
            
            # Update alert status
            alert.is_email_sent = True
            alert.email_sent_at = timezone.now()
            alert.save()
            
            logger.info(f"Alert notification sent for alert {alert.id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send alert notification: {str(e)}")
            return False

    def _build_email_message(self, alert: Alert) -> str:
        """Build the email message content."""
        website = alert.website
        incident = alert.incident
        
        message = f"""
DEFACE SPY - DEFACEMENT ALERT
================================

Alert: {alert.title}
Severity: {alert.severity.upper()}
Website: {website.name}
URL: {website.url}

Message:
{alert.message}

"""
        
        if incident:
            message += f"""
Incident Details:
- Change Percentage: {incident.change_percentage}%
- Affected Blocks: {incident.affected_blocks}
- Status: {incident.status}

"""
        
        message += f"""
Time Detected: {alert.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}

Action Required:
Please log in to your Deface Spy dashboard to review this alert and take appropriate action.

---
This is an automated message from Deface Spy.
"""
        
        return message

    def _build_html_email_message(self, alert: Alert) -> str:
        """Build a security-themed HTML notification without user/profile photos."""
        website = alert.website
        incident = alert.incident
        incident_details = ''
        if incident:
            incident_details = f"""
                <div style="margin-top:20px;padding:16px;border:1px solid #263548;border-radius:10px;background:#111a26">
                    <div style="color:#94a3b8;font-size:12px;letter-spacing:1px">INCIDENT DETAILS</div>
                    <p style="margin:10px 0 0;color:#e2e8f0">
                        Change percentage: <strong>{incident.change_percentage}%</strong><br>
                        Affected blocks: <strong>{incident.affected_blocks}</strong><br>
                        Status: <strong>{incident.status}</strong>
                    </p>
                </div>
            """

        severity_color = '#ef4444' if alert.severity == 'critical' else '#f59e0b'
        return f"""
        <!doctype html>
        <html>
          <body style="margin:0;background:#0b1220;color:#e2e8f0;font-family:Arial,sans-serif">
            <div style="max-width:680px;margin:24px auto;padding:0 16px">
              <div style="border:1px solid #263548;border-radius:16px;overflow:hidden;background:#101a28">
                <div style="padding:28px;text-align:center;background:linear-gradient(135deg,#0f766e,#123047)">
                  <div style="display:inline-block;padding:18px;border:2px solid #5eead4;border-radius:24px">
                    <svg width="76" height="76" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Cyber security shield">
                      <path d="M12 3L19 6V11.5C19 16.2 16.1 19.6 12 21C7.9 19.6 5 16.2 5 11.5V6L12 3Z" stroke="#ccfbf1" stroke-width="1.5"/>
                      <rect x="9" y="10" width="6" height="5" rx="1" fill="#ccfbf1"/>
                      <path d="M10.5 10V8.8C10.5 7.97 11.17 7.3 12 7.3C12.83 7.3 13.5 7.97 13.5 8.8V10" stroke="#0f766e" stroke-width="1.2"/>
                    </svg>
                  </div>
                  <h1 style="margin:16px 0 4px;font-size:24px;color:#f0fdfa">DEFACE SPY</h1>
                  <p style="margin:0;color:#ccfbf1;font-size:12px;letter-spacing:2px">CYBER SECURITY ALERT</p>
                </div>
                <div style="padding:28px">
                  <div style="display:inline-block;padding:6px 10px;border-radius:999px;background:{severity_color}22;color:{severity_color};font-size:12px;font-weight:bold;letter-spacing:1px">
                    {alert.severity.upper()} THREAT
                  </div>
                  <h2 style="margin:16px 0 8px;color:#f8fafc">{alert.title}</h2>
                  <p style="line-height:1.6;color:#cbd5e1">{alert.message}</p>
                  <div style="margin-top:20px;padding:16px;border:1px solid #263548;border-radius:10px;background:#111a26">
                    <div style="color:#94a3b8;font-size:12px;letter-spacing:1px">DETECTION DETAILS</div>
                    <p style="margin:10px 0 0;line-height:1.7;color:#e2e8f0">
                      Website: <strong>{website.name}</strong><br>
                      URL: <strong>{website.url}</strong><br>
                      Detected: <strong>{alert.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}</strong><br>
                      Status: <strong>{alert.status.upper()}</strong>
                    </p>
                  </div>
                  {incident_details}
                  <p style="margin:24px 0 0;color:#94a3b8;font-size:12px">
                    Review this alert in your Deface Spy dashboard and take the recommended remediation steps.
                  </p>
                </div>
                <div style="padding:16px 28px;border-top:1px solid #263548;color:#64748b;font-size:11px">
                  Automated security notification from Deface Spy.
                </div>
              </div>
            </div>
          </body>
        </html>
        """

    def resolve_alert(self, alert: Alert, user=None) -> Alert:
        """
        Resolve an alert.
        
        Args:
            alert: The alert to resolve
            user: The user resolving the alert
            
        Returns:
            The updated alert
        """
        alert.status = 'resolved'
        alert.resolved_at = timezone.now()
        alert.save()
        
        # Also resolve the associated incident if exists
        if alert.incident:
            alert.incident.status = 'resolved'
            alert.incident.resolved_at = timezone.now()
            alert.incident.resolved_by = user
            alert.incident.save()
        
        return alert

    def acknowledge_alert(self, alert: Alert, user) -> Alert:
        """
        Acknowledge an alert.
        
        Args:
            alert: The alert to acknowledge
            user: The user acknowledging the alert
            
        Returns:
            The updated alert
        """
        alert.status = 'acknowledged'
        alert.acknowledged_by = user
        alert.acknowledged_at = timezone.now()
        alert.save()
        
        # Update incident status
        if alert.incident:
            alert.incident.status = 'investigating'
            alert.incident.save()
        
        return alert

    def dismiss_alert(self, alert: Alert) -> Alert:
        """
        Dismiss an alert (mark as false positive).
        
        Args:
            alert: The alert to dismiss
            
        Returns:
            The updated alert
        """
        alert.status = 'dismissed'
        alert.save()
        
        # Mark incident as false positive
        if alert.incident:
            alert.incident.status = 'false_positive'
            alert.incident.save()
        
        return alert
