"""
VoiceSetu Human Fallback & Escalation System
Routes low-confidence, noisy, or missing-document calls directly to local village intermediaries:
- SHG Bank Sakhi (Self-Help Group Didi)
- CSC VLE (Common Service Centre Village Level Entrepreneur)
- Anganwadi Worker (ASHA / ICDS)
- Gram Panchayat Rozgar Sahayak
"""

import time
from typing import List, Dict, Any, Optional

FALLBACK_TICKETS: List[Dict[str, Any]] = [
    {
        "id": "FB-101",
        "caller_phone": "+91 98765-XXXX1",
        "village": "Pipra, Block Sahjanwa, Gorakhpur (UP)",
        "language": "hi",
        "dialect": "Bhojpuri",
        "target_scheme": "PMMVY (Maternity Assistance)",
        "missing_docs": ["MCP Anganwadi Card", "NPCI Bank Linking"],
        "reason": "Missing documents & ambient thresher tractor noise (72 dB)",
        "assigned_worker": "Sunita Devi (SHG Bank Sakhi)",
        "worker_phone": "+91 94152-XXXX4",
        "status": "DOORSTEP_SCHEDULED",
        "created_at": "10 mins ago",
        "notes": "Bank passbook not linked to Aadhaar. Sakhi will take biometric micro-ATM to her house."
    },
    {
        "id": "FB-102",
        "caller_phone": "+91 94441-XXXX8",
        "village": "Melur, Madurai (Tamil Nadu)",
        "language": "ta",
        "dialect": "Madurai Tamil",
        "target_scheme": "Kalaignar Magalir Urimai Thogai",
        "missing_docs": ["Electricity Bill EB Number"],
        "reason": "Explicit user voice request ('Akka, need help with EB bill')",
        "assigned_worker": "Kavitha M. (E-Sevai VLE Operator)",
        "worker_phone": "+91 97890-XXXX2",
        "status": "PENDING_CALL",
        "created_at": "3 mins ago",
        "notes": "Elderly widow living alone; assistance needed to trace electricity meter consumer number."
    },
    {
        "id": "FB-103",
        "caller_phone": "+91 99890-XXXX7",
        "village": "Kothur, Mahabubnagar (Telangana)",
        "language": "te",
        "dialect": "Telangana Rural",
        "target_scheme": "Telangana Mahalakshmi Scheme",
        "missing_docs": ["Praja Palana Application Number"],
        "reason": "ASR low confidence (< 0.60) in haat bazaar environment",
        "assigned_worker": "Padma Bai (Village Secretariat Volunteer)",
        "worker_phone": "+91 88970-XXXX3",
        "status": "RESOLVED",
        "created_at": "25 mins ago",
        "notes": "Praja palana acknowledgement number traced and mapped in portal."
    }
]

def create_fallback_ticket(
    session_id: str,
    caller_phone: str,
    language: str,
    target_scheme: str,
    missing_docs: List[str],
    reason: str,
    dialect: str = "Standard"
) -> Dict[str, Any]:
    ticket_id = f"FB-{len(FALLBACK_TICKETS) + 101}"
    ticket = {
        "id": ticket_id,
        "session_id": session_id,
        "caller_phone": caller_phone or "+91 98XXX-XXXXX",
        "village": "Rampur Gram Panchayat, Ward 3",
        "language": language,
        "dialect": dialect,
        "target_scheme": target_scheme or "General Women Welfare Schemes",
        "missing_docs": missing_docs or ["Aadhaar-Bank DBT Confirmation"],
        "reason": reason,
        "assigned_worker": "Sunita Devi (SHG Bank Sakhi)",
        "worker_phone": "+91 98765-43210",
        "status": "LIVE_CONNECTING",
        "created_at": "Just now",
        "notes": "Live escalation from automated IVR voice helper."
    }
    FALLBACK_TICKETS.insert(0, ticket)
    return ticket

def get_fallback_queue() -> List[Dict[str, Any]]:
    return FALLBACK_TICKETS

def update_ticket_status(ticket_id: str, status: str, worker_notes: Optional[str] = None) -> bool:
    for t in FALLBACK_TICKETS:
        if t["id"] == ticket_id:
            t["status"] = status
            if worker_notes:
                t["notes"] = worker_notes
            return True
    return False
