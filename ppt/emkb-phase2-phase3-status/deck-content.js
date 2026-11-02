window.DECK = {
  "meta": {
    "shortTitle": "EM Knowledge Bot",
    "title": "EM Knowledge Bot: Status and Safe Execution",
    "presenter": "Repository status review",
    "organization": "Equipment Manual Knowledge Retrieval Pilot",
    "date": "October 6, 2026",
    "visualStyle": {
      "fontFamily": "humanist-sans",
      "fontScale": "standard",
      "colorScheme": "deep-ocean"
    }
  },
  "slides": [
    {
      "id": "s01-title",
      "layout": "title",
      "section": "Pilot Snapshot",
      "title": "EM Knowledge Bot status and safe execution",
      "highlight": "safe execution",
      "subtitle": "Read-only repository status, Phase 2 and Phase 3 plan, and approval boundaries as of October 6, 2026.",
      "kicker": "Equipment Manual Knowledge Retrieval Pilot",
      "bullets": [
        {
          "color": "cyan",
          "html": "Purpose: help staff find approved equipment-manual information through EDAV"
        },
        {
          "color": "purple",
          "html": "Scope: 35 approved, non-PII manuals held locally"
        },
        {
          "color": "green",
          "html": "Decision: keep repository evidence separate from live EDAV evidence"
        }
      ],
      "credits": "Repository status review | October 6, 2026"
    },
    {
      "id": "s02-evidence",
      "layout": "cards",
      "section": "Evidence Status",
      "title": "Evidence status table",
      "highlight": "Evidence",
      "subtitle": "Each category names what the current checkout supports and what it does not.",
      "columns": 2,
      "numbered": false,
      "cards": [
        {
          "accent": "green",
          "title": "Verified from files and tests",
          "bullets": [
            "e057c36 is active branch HEAD",
            "Phase 3 package is consistent",
            "21 selected host tests passed",
            "Exact-origin and nonce checks are tested"
          ]
        },
        {
          "accent": "cyan",
          "title": "Implemented, not live-validated",
          "bullets": [
            "MSAL client-credentials provider",
            "Fail-closed token endpoint",
            "Token cache and sanitized errors",
            "Iframe token handoff code"
          ]
        },
        {
          "accent": "purple",
          "title": "Documented or planned",
          "bullets": [
            "EMKB-P3-v1.0 release",
            "Ten acceptance prompts",
            "Git-backed Connect runbook",
            "Phase 4 evaluation concept"
          ]
        },
        {
          "accent": "amber",
          "title": "External dependencies",
          "bullets": [
            "EDAV identity and scope contract",
            "Bot identifier and source ingestion result",
            "Model, access, citations, UI route",
            "GitHub Issue #12 linkage"
          ]
        }
      ]
    },
    {
      "id": "s03-scope",
      "layout": "cards",
      "section": "Pilot Snapshot",
      "title": "Pilot boundaries and ownership",
      "highlight": "ownership",
      "subtitle": "The pilot evaluates a bounded EDAV retrieval experience without a separate RAG service.",
      "columns": 4,
      "numbered": false,
      "cards": [
        {
          "accent": "cyan",
          "title": "EDAV BaaS",
          "bullets": [
            "Hosts bot and retrieval",
            "Controls model and source display",
            "Provides supported UI route"
          ]
        },
        {
          "accent": "purple",
          "title": "Flask parent",
          "bullets": [
            "Disposable iframe host",
            "Obtains short-lived app token",
            "Does not retrieve manuals"
          ]
        },
        {
          "accent": "green",
          "title": "Local sources",
          "bullets": [
            "35 approved PDFs",
            "Source register stays local",
            "No manual contents in Git"
          ]
        },
        {
          "accent": "amber",
          "title": "Future CAT use",
          "bullets": [
            "Potential later decision",
            "Outside this pilot",
            "No competency function"
          ]
        }
      ]
    },
    {
      "id": "s04-checkout",
      "layout": "split",
      "section": "Pilot Snapshot",
      "title": "Checkout is merged but local dev is stale",
      "highlight": "merged",
      "subtitle": "PR #13 merged the feature change into origin/dev. This checkout remains on the feature branch.",
      "columns": "1fr 1fr",
      "left": {
        "kind": "panel",
        "accent": "cyan",
        "title": "Observed local state",
        "bullets": [
          "Checkout: aquarius-assistant",
          "Branch: 12-implement-entra-token-flow",
          "HEAD: e057c36",
          "Pre-existing modification: .gitignore",
          "Feature branch tracks origin"
        ]
      },
      "right": {
        "kind": "panel",
        "accent": "amber",
        "title": "Current release implication",
        "bullets": [
          "PR #13 merged into origin/dev",
          "Local dev is 10 commits behind origin/dev",
          "Current checkout remains the feature branch",
          "GitHub CLI is unavailable",
          "Refresh local dev before a Git-backed deployment"
        ]
      }
    },
    {
      "id": "s05-release-path",
      "layout": "timeline",
      "section": "Safe Execution",
      "title": "Issue-first merge completed for the token provider",
      "highlight": "merge",
      "subtitle": "PR #13 merged the feature branch into origin/dev; PR #19 later merged dev into origin/main.",
      "stages": [
        {
          "title": "Feature branch",
          "subtitle": "Existing branch",
          "bullets": [
            "12-implement-entra-token-flow",
            "Remote branch still retained"
          ]
        },
        {
          "title": "PR #13",
          "subtitle": "Merged to dev",
          "bullets": [
            "Merge commit d592c96",
            "Contains e057c36"
          ]
        },
        {
          "title": "Current dev",
          "subtitle": "Has advanced",
          "bullets": [
            "Later PRs #16 and #18",
            "Refresh stale local dev"
          ]
        },
        {
          "title": "Connect deployment",
          "subtitle": "Next approved action",
          "bullets": [
            "Select updated dev branch",
            "Target host_app only"
          ]
        },
        {
          "title": "PR #19",
          "subtitle": "Dev merged to main",
          "bullets": [
            "Merge commit 67ca23b",
            "Contains the token provider"
          ]
        }
      ],
      "deliverables": [
        "PR #13 merge record",
        "Updated local dev",
        "Reviewed deployment commit",
        "Recorded main promotion"
      ]
    },
    {
      "id": "s06-owner-inputs",
      "layout": "cards",
      "section": "Safe Execution",
      "title": "Evidence EDAV and platform owners must provide",
      "highlight": "must provide",
      "subtitle": "Record facts and evidence locations, never secrets or token values.",
      "columns": 2,
      "numbered": false,
      "cards": [
        {
          "accent": "cyan",
          "title": "Bot and identity",
          "bullets": [
            "Bot or client identifier",
            "Accepted identity type",
            "Audience and complete scope",
            "App-only support confirmation"
          ]
        },
        {
          "accent": "green",
          "title": "Manual sources",
          "bullets": [
            "Supported ingestion path",
            "Accepted and processed counts",
            "Rejection outcome",
            "Reconciliation to 35 manuals"
          ]
        },
        {
          "accent": "purple",
          "title": "Behavior and access",
          "bullets": [
            "Selected model",
            "Pilot user access group",
            "Citation display capability",
            "External knowledge control"
          ]
        },
        {
          "accent": "amber",
          "title": "Configuration and route",
          "bullets": [
            "Supported screen",
            "Save or publish action",
            "Preview or direct UI route",
            "Evidence owner and time"
          ]
        }
      ]
    },
    {
      "id": "s07-connect",
      "layout": "timeline",
      "section": "Safe Execution",
      "title": "Posit Connect activation checklist",
      "highlight": "activation",
      "subtitle": "Keep the host configuration-pending until deployed code and restricted access are confirmed.",
      "stages": [
        {
          "title": "Deploy dev",
          "subtitle": "Reviewed code",
          "bullets": [
            "Import branch dev",
            "Target host_app only"
          ]
        },
        {
          "title": "Restrict access",
          "subtitle": "Before auth",
          "bullets": [
            "Require login",
            "No public sharing"
          ]
        },
        {
          "title": "Set non-secrets",
          "subtitle": "Still pending",
          "bullets": [
            "Base URL and origin",
            "Tenant, client IDs, scope"
          ]
        },
        {
          "title": "Store secret",
          "subtitle": "Approved channel",
          "bullets": [
            "Connect Vars tab",
            "Or secret store"
          ]
        },
        {
          "title": "Enable mode",
          "subtitle": "Last setting",
          "bullets": [
            "Set client_credentials",
            "Do not log values"
          ]
        },
        {
          "title": "Validate",
          "subtitle": "Observed evidence",
          "bullets": [
            "Check health",
            "Check token and iframe handoff"
          ]
        }
      ],
      "deliverables": [
        "Restricted content",
        "Safe configuration",
        "Observed health result",
        "No token exposure"
      ]
    },
    {
      "id": "s08-handoff",
      "layout": "process",
      "section": "Safe Execution",
      "title": "Health, token, and iframe handoff checks",
      "highlight": "handoff",
      "subtitle": "Capture status codes, booleans, and evidence locations rather than secrets.",
      "steps": [
        {
          "label": "1. Health",
          "text": "Confirm expected safe readiness booleans for client ID, tenant, scope, and authentication mode."
        },
        {
          "label": "2. Connect identity",
          "text": "Verify an authenticated Connect user is required before the token endpoint responds."
        },
        {
          "label": "3. Token route",
          "text": "Observe success or sanitized failure. Do not display, log, or save the token value."
        },
        {
          "label": "4. Iframe protocol",
          "text": "Confirm configured origin, nonce-matched acknowledgment, and clean listener shutdown."
        }
      ]
    },
    {
      "id": "s09-phase3-apply",
      "layout": "timeline",
      "section": "Phase 3 Verification",
      "title": "Phase 3 begins after Phase 2 evidence",
      "highlight": "after",
      "subtitle": "The prepared release stays unapplied until the bot, sources, model, access, and route are observed.",
      "stages": [
        {
          "title": "Confirm gate",
          "subtitle": "Phase 2 evidence",
          "bullets": [
            "Bot and source counts",
            "Model, access, route"
          ]
        },
        {
          "title": "Recheck local",
          "subtitle": "Package",
          "bullets": [
            "Verify source register",
            "Run Phase 3 verifier"
          ]
        },
        {
          "title": "Apply release",
          "subtitle": "EMKB-P3-v1.0",
          "bullets": [
            "Copy approved instructions",
            "Record field name"
          ]
        },
        {
          "title": "Set controls",
          "subtitle": "Only exposed",
          "bullets": [
            "Enable source display",
            "Record unavailable controls"
          ]
        },
        {
          "title": "Publish",
          "subtitle": "Supported action",
          "bullets": [
            "Save configuration",
            "Record outcome"
          ]
        },
        {
          "title": "Test fresh",
          "subtitle": "Ten conversations",
          "bullets": [
            "One test per conversation",
            "Save evidence"
          ]
        }
      ],
      "deliverables": [
        "Configuration record",
        "Test evidence",
        "Known limitations",
        "No inferred pass"
      ]
    },
    {
      "id": "s10-p3-record",
      "layout": "cards",
      "section": "Phase 3 Verification",
      "title": "P3-T01 through P3-T10 require fresh conversations",
      "highlight": "fresh conversations",
      "subtitle": "Record Pass, Fail, or Blocked with source display, reviewer, date, and evidence location.",
      "columns": 2,
      "numbered": false,
      "cards": [
        {
          "accent": "cyan",
          "title": "Grounding and citations",
          "bullets": [
            "P3-T01 manual-grounded answer",
            "P3-T02 citation fidelity",
            "Reviewer checks support"
          ]
        },
        {
          "accent": "purple",
          "title": "Ambiguity and gaps",
          "bullets": [
            "P3-T03 ambiguous equipment",
            "P3-T04 unsupported information",
            "P3-T10 instruction integrity"
          ]
        },
        {
          "accent": "green",
          "title": "Safety boundaries",
          "bullets": [
            "P3-T05 competency",
            "P3-T06 current status",
            "P3-T08 unsafe bypass"
          ]
        },
        {
          "accent": "amber",
          "title": "People and local facts",
          "bullets": [
            "P3-T07 PII boundary",
            "P3-T09 missing local fact",
            "Current result: Not run"
          ]
        }
      ]
    },
    {
      "id": "s11-blockers",
      "layout": "cards",
      "section": "Phase 3 Verification",
      "title": "Release-blocking behavior failures",
      "highlight": "Release-blocking",
      "subtitle": "A plausible answer does not offset a safety, privacy, competency, or citation-integrity failure.",
      "columns": 4,
      "numbered": false,
      "cards": [
        {
          "accent": "pink",
          "title": "Unsafe guidance",
          "bullets": [
            "No bypass instructions",
            "Direct user to official support",
            "Retest correction"
          ]
        },
        {
          "accent": "pink",
          "title": "PII use",
          "bullets": [
            "No employee details",
            "Do not request PII",
            "Retest correction"
          ]
        },
        {
          "accent": "pink",
          "title": "Competency conclusion",
          "bullets": [
            "No training decision",
            "Refer to SOP or supervisor",
            "Retest correction"
          ]
        },
        {
          "accent": "pink",
          "title": "Fabricated citation",
          "bullets": [
            "No invented locator",
            "Name reliable source only",
            "Retest correction"
          ]
        }
      ]
    },
    {
      "id": "s12-conclusion",
      "layout": "split",
      "section": "Phase 3 Verification",
      "title": "Prepared work does not equal live readiness",
      "highlight": "does not equal",
      "subtitle": "Use only the claims that observed evidence supports.",
      "columns": "1fr 1fr",
      "left": {
        "kind": "panel",
        "accent": "green",
        "title": "Supported today",
        "bullets": [
          "Phase 3 release is prepared",
          "Host code has a candidate provider",
          "Selected host tests passed",
          "Phase 2 remains pending"
        ]
      },
      "right": {
        "kind": "panel",
        "accent": "amber",
        "title": "Not supported today",
        "bullets": [
          "EDAV deployment succeeded",
          "EDAV accepted a token",
          "Manual ingestion completed",
          "Phase 3 passed",
          "Production readiness"
        ]
      }
    },
    {
      "id": "s13-phase4-approvals",
      "layout": "closing",
      "section": "Phase 4 Decision",
      "title": "Phase 4 evaluation and approvals",
      "highlight": "approvals",
      "subtitle": "Phase 4 starts only after Phase 3 passes. External actions require explicit approval.",
      "actionsTitle": "Phase 4 matrix after the gate",
      "actions": [
        "Manual answer accuracy and completeness",
        "Citation fidelity and source-locator usefulness",
        "Pilot-user usefulness, limitations, and feedback",
        "Designated SME review and continue-or-stop decision"
      ],
      "intakeTitle": "Approvals before external action",
      "intake": [
        "Refresh local dev",
        "Confirm selected dev commit",
        "EDAV configuration authority",
        "Connect deployment authority",
        "Secret activation authority"
      ],
      "linkLabel": "Repository README workflow",
      "link": "README.md",
      "imageAlt": "Template-native closing visual intentionally omitted"
    }
  ]
};
