window.SPEAKER_NOTES = {
  "s01-title": {
    "durationSeconds": 50,
    "talkTrack": [
      "This is a status report, not a production-readiness claim.",
      "No platform or source-code change occurs as part of this report."
    ],
    "evidence": [
      "README scope and current status"
    ],
    "caveats": [
      "No EDAV portal or Posit Connect system was accessed."
    ],
    "audienceInteraction": "",
    "sources": [
      "readme",
      "phase3-config"
    ],
    "transitionFromPrevious": "",
    "transitionToNext": "The status snapshot makes the evidence gap visible."
  },
  "s02-evidence": {
    "durationSeconds": 90,
    "talkTrack": [
      "Keep each item in its evidence category.",
      "A local test does not prove EDAV behavior."
    ],
    "evidence": [
      "Commit diff, selected pytest output, verifier output"
    ],
    "caveats": [
      "The complete pytest run has eight archive-chat tests blocked by managed temporary-directory permissions before their assertions ran."
    ],
    "audienceInteraction": "",
    "sources": [
      "token-commit",
      "host-tests",
      "phase3-verifier"
    ],
    "transitionFromPrevious": "The cover stated the evidence boundary.",
    "transitionToNext": "The scope split explains why the boundary matters."
  },
  "s03-scope": {
    "durationSeconds": 65,
    "talkTrack": [
      "Keep the parent host small and scoped.",
      "Future CAT integration is a separate decision."
    ],
    "evidence": [
      "README scope boundary"
    ],
    "caveats": [
      "No manual contents appear in this deck."
    ],
    "audienceInteraction": "",
    "sources": [
      "readme",
      "phase3-config"
    ],
    "transitionFromPrevious": "Evidence categories describe what is known.",
    "transitionToNext": "The checkout establishes the source-control constraint."
  },
  "s04-checkout": {
    "durationSeconds": 75,
    "talkTrack": [
      "Preserve the .gitignore modification.",
      "PR #13 is verified from the local merge commit. The underlying issue relationship remains unverified."
    ],
    "evidence": [
      "git status, git rev-list, git branch, and git show d592c96"
    ],
    "caveats": [
      "Use an updated local dev checkout, not this retained feature checkout, for the Git-backed deployment selection."
    ],
    "audienceInteraction": "",
    "sources": [
      "git-preflight",
      "token-commit",
      "merge-pr13"
    ],
    "transitionFromPrevious": "The pilot boundary protects the source corpus.",
    "transitionToNext": "The release path is now evidenced by the merged PR."
  },
  "s05-release-path": {
    "durationSeconds": 85,
    "talkTrack": [
      "The issue-first PR step is complete through PR #13, and PR #19 records the later dev-to-main promotion.",
      "For deployment, update the local dev checkout and confirm the selected dev commit."
    ],
    "evidence": [
      "Merge commits d592c96 and 67ca23b, origin/dev history, and README workflow"
    ],
    "caveats": [
      "No new issue, PR, push, or merge happened during this correction."
    ],
    "audienceInteraction": "",
    "sources": [
      "merge-pr13",
      "merge-pr19",
      "git-preflight",
      "readme"
    ],
    "transitionFromPrevious": "The checkout is merged upstream but remains a stale feature checkout.",
    "transitionToNext": "External owners must supply the Phase 2 facts that code cannot infer."
  },
  "s06-owner-inputs": {
    "durationSeconds": 90,
    "talkTrack": [
      "Ask for observed settings and evidence locations.",
      "Do not substitute a portal token or guess the audience and scope."
    ],
    "evidence": [
      "Phase 3 configuration sections 4, 5, and 7"
    ],
    "caveats": [
      "The code expects app-only client credentials and a /.default scope. EDAV must approve the actual contract."
    ],
    "audienceInteraction": "",
    "sources": [
      "phase3-config",
      "readme"
    ],
    "transitionFromPrevious": "Source-control review makes the code bundle traceable.",
    "transitionToNext": "With external evidence and a reviewed dev merge, Connect activation remains staged and fail closed."
  },
  "s07-connect": {
    "durationSeconds": 95,
    "talkTrack": [
      "Deploy only the isolated host_app folder.",
      "Do not place secrets in Git, chat, commands, or the deck."
    ],
    "evidence": [
      "README Git-backed Posit Connect deployment and .env.example"
    ],
    "caveats": [
      "This step depends on a reviewed dev merge and approved EDAV contract."
    ],
    "audienceInteraction": "",
    "sources": [
      "readme"
    ],
    "transitionFromPrevious": "External facts make the configuration intentional.",
    "transitionToNext": "Handoff validation uses status information rather than exposed bearer tokens."
  },
  "s08-handoff": {
    "durationSeconds": 85,
    "talkTrack": [
      "A green health response alone does not prove EDAV accepted the token.",
      "The evidence record must not contain the token."
    ],
    "evidence": [
      "app.py, entra_auth.py, microbot.js, and selected tests"
    ],
    "caveats": [
      "Only a real EDAV handoff validates audience, scope, and bot acceptance."
    ],
    "audienceInteraction": "",
    "sources": [
      "token-commit",
      "host-tests"
    ],
    "transitionFromPrevious": "Activation produces a safe but still unverified live handoff.",
    "transitionToNext": "Phase 3 begins only when Phase 2 evidence is complete."
  },
  "s09-phase3-apply": {
    "durationSeconds": 90,
    "talkTrack": [
      "Do not invent a setting that EDAV does not expose.",
      "Record unavailable controls and test the resulting behavior."
    ],
    "evidence": [
      "Phase 3 configuration sections 4 and 5"
    ],
    "caveats": [
      "The local verifier checks consistency only."
    ],
    "audienceInteraction": "",
    "sources": [
      "phase3-config",
      "phase3-verifier"
    ],
    "transitionFromPrevious": "The Phase 2 gate protects Phase 3 from unknown platform state.",
    "transitionToNext": "Each acceptance case needs a fresh conversation and an evidence record."
  },
  "s10-p3-record": {
    "durationSeconds": 90,
    "talkTrack": [
      "Run prompts exactly as written on the first pass.",
      "A missing platform capability is Blocked, not Pass."
    ],
    "evidence": [
      "Phase 3 test instructions and result table"
    ],
    "caveats": [
      "Do not reuse a conversation between cases."
    ],
    "audienceInteraction": "",
    "sources": [
      "phase3-tests"
    ],
    "transitionFromPrevious": "The release process reaches its evidence-producing step.",
    "transitionToNext": "Some observed failures stop release progression immediately."
  },
  "s11-blockers": {
    "durationSeconds": 75,
    "talkTrack": [
      "Keep blocked tests visible.",
      "Do not build an unapproved custom RAG or direct model workaround."
    ],
    "evidence": [
      "Phase 3 test pass rule and failure handling"
    ],
    "caveats": [
      "A behavior change needs controlled release tracking and applicable retesting."
    ],
    "audienceInteraction": "",
    "sources": [
      "phase3-tests",
      "phase3-config"
    ],
    "transitionFromPrevious": "Each test produces evidence rather than a narrative of success.",
    "transitionToNext": "The current conclusion keeps unobserved milestones visible."
  },
  "s12-conclusion": {
    "durationSeconds": 65,
    "talkTrack": [
      "This is the evidence-based conclusion.",
      "Refresh it after every observed platform milestone."
    ],
    "evidence": [
      "README current status, Phase 3 completion gate, verifier output"
    ],
    "caveats": [
      "No live verification has been inferred."
    ],
    "audienceInteraction": "",
    "sources": [
      "readme",
      "phase3-config",
      "phase3-verifier"
    ],
    "transitionFromPrevious": "Release blockers explain why a completed evidence record matters.",
    "transitionToNext": "The Phase 4 proposal is conditional on a genuine Phase 3 pass."
  },
  "s13-phase4-approvals": {
    "durationSeconds": 75,
    "talkTrack": [
      "This review created only the presentation artifact.",
      "PR #13 already merged this feature into origin/dev. Pause for approval before refresh, deployment, EDAV configuration, or secret activation."
    ],
    "evidence": [
      "Phase 3 handoff guidance and README workflow"
    ],
    "caveats": [
      "No secret, token, credential, PII, or manual content appears in the presentation."
    ],
    "audienceInteraction": "",
    "sources": [
      "phase3-config",
      "readme"
    ],
    "transitionFromPrevious": "A credible Phase 4 depends on a completed Phase 3 gate.",
    "transitionToNext": ""
  }
};
