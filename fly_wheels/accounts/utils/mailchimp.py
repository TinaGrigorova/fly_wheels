# accounts/utils/mailchimp.py
"""
Thin Mailchimp helper with safe fallbacks.

- If the 'mailchimp_marketing' SDK is not installed, or required env vars
  are missing, functions just return False (no-op) so imports never break.
- Uses 'set_list_member' (idempotent upsert) keyed by the MD5 hash of email.
- Supports either MAILCHIMP_LIST_ID or MAILCHIMP_AUDIENCE_ID for the list.
"""

from __future__ import annotations

import hashlib
import logging
import os
from typing import Iterable, Optional

try:
    import mailchimp_marketing as MailchimpMarketing
    from mailchimp_marketing.api_client import ApiClientError
except Exception:  
    MailchimpMarketing = None  
    class ApiClientError(Exception): 
        pass

log = logging.getLogger(__name__)

# Read configuration once; support both names for the list id
API_KEY = os.getenv("MAILCHIMP_API_KEY")
SERVER = os.getenv("MAILCHIMP_SERVER_PREFIX")
LIST_ID = os.getenv("MAILCHIMP_LIST_ID") or os.getenv("MAILCHIMP_AUDIENCE_ID")

_client_cache = None


def _member_hash(email: str) -> str:
    return hashlib.md5(email.strip().lower().encode("utf-8")).hexdigest()


def _client():
    """Return a configured Mailchimp client or None if unavailable."""
    global _client_cache
    if MailchimpMarketing is None:
        log.debug("Mailchimp SDK not installed; skipping.")
        return None
    if not (API_KEY and SERVER):
        log.debug("MAILCHIMP_API_KEY / MAILCHIMP_SERVER_PREFIX not set; skipping.")
        return None
    if _client_cache is None:
        c = MailchimpMarketing.Client()
        c.set_config({"api_key": API_KEY, "server": SERVER})
        _client_cache = c
    return _client_cache


def subscribe(
    email: str,
    first_name: str = "",
    last_name: str = "",
    tags: Optional[Iterable[str]] = None,
    double_opt_in: bool = True,
) -> bool:
    """
    Upsert a list member and (optionally) tag them.
    Returns True on success, False on any failure or when not configured.
    """
    cli = _client()
    if not (cli and LIST_ID):
        return False

    email = (email or "").strip().lower()
    if not email:
        return False

    payload = {
        "email_address": email,
      
        "status_if_new": "pending" if double_opt_in else "subscribed",
       
        "status": "subscribed",
        "merge_fields": {"FNAME": first_name or "", "LNAME": last_name or ""},
    }
    if tags:
        payload["tags"] = list(tags)

    try:
        cli.lists.set_list_member(LIST_ID, _member_hash(email), payload)
        return True
    except ApiClientError as e:
        
        msg = getattr(e, "text", str(e))
        log.warning("Mailchimp subscribe failed for %s: %s", email, msg)
        return False


def unsubscribe(email: str) -> bool:
    """
    Mark a member as 'unsubscribed'. Returns True on success, False otherwise.
    """
    cli = _client()
    if not (cli and LIST_ID):
        return False

    email = (email or "").strip().lower()
    if not email:
        return False

    try:
        cli.lists.update_list_member(LIST_ID, _member_hash(email), {"status": "unsubscribed"})
        return True
    except ApiClientError as e:
        msg = getattr(e, "text", str(e))
        log.warning("Mailchimp unsubscribe failed for %s: %s", email, msg)
        return False
