#!/bin/bash
# Vibe Coding Automation Quick Start
# Run this script to set up GitHub labels for multi-agent collaboration
#
# Usage: bash TONY_AUTOMATION_QUICKSTART.sh
# Requires: gh CLI installed and authenticated

set -e  # Exit on error

echo "🤖 Vibe Coding Automation Setup"
echo "================================"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ Error: GitHub CLI (gh) is not installed"
    echo "Install it from: https://cli.github.com/"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ Error: Not authenticated with GitHub CLI"
    echo "Run: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI detected and authenticated"
echo ""

# Confirm repository
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
echo "📦 Repository: $REPO"
echo ""
read -p "Is this correct? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Aborted. Run this script from the repository directory."
    exit 1
fi

echo ""
echo "🏷️  Creating labels..."
echo ""

# Agent labels
echo "Creating agent labels..."
gh label create "agent: stanley" --color "667eea" --description "Stanley (Claude Code) orchestration work" --force
gh label create "agent: michael" --color "10b981" --description "Michael (VS Code Copilot) local development" --force
gh label create "agent: tony" --color "f59e0b" --description "Tony (GitHub Cloud Agent) infrastructure & PRs" --force
gh label create "agent: multi-agent" --color "ec4899" --description "Requires coordination between multiple agents" --force
echo "✅ Agent labels created (4)"

# Phase labels
echo "Creating phase labels..."
gh label create "phase: planning" --color "3b82f6" --description "Planning and architectural design phase" --force
gh label create "phase: implementation" --color "8b5cf6" --description "Active development and implementation" --force
gh label create "phase: review" --color "f97316" --description "Under review, awaiting feedback" --force
gh label create "phase: testing" --color "06b6d4" --description "Testing and quality assurance" --force
gh label create "phase: deployment" --color "14b8a6" --description "Deployment and release phase" --force
echo "✅ Phase labels created (5)"

# Content type labels
echo "Creating content type labels..."
gh label create "content: cookbook" --color "84cc16" --description "Changes to AI × Human Cookbook content" --force
gh label create "content: documentation" --color "22c55e" --description "General documentation updates" --force
gh label create "content: ui-ux" --color "a855f7" --description "UI/UX design and component work" --force
gh label create "content: infrastructure" --color "ef4444" --description "Infrastructure, CI/CD, tooling" --force
gh label create "content: community-features" --color "f59e0b" --description "Community features (upvoting, comments, etc.)" --force
gh label create "content: branding" --color "ec4899" --description "BUNKER branding and design system" --force
echo "✅ Content type labels created (6)"

# Priority labels
echo "Creating priority labels..."
gh label create "priority: critical" --color "dc2626" --description "Critical - blocks other work or breaks production" --force
gh label create "priority: high" --color "f97316" --description "High priority - should be done soon" --force
gh label create "priority: medium" --color "eab308" --description "Medium priority - normal timeline" --force
gh label create "priority: low" --color "6b7280" --description "Low priority - nice to have" --force
echo "✅ Priority labels created (4)"

# Status labels
echo "Creating status labels..."
gh label create "status: blocked" --color "dc2626" --description "Blocked by external dependency or decision" --force
gh label create "status: needs-decision" --color "f59e0b" --description "Awaiting user decision or architectural choice" --force
gh label create "status: needs-review" --color "3b82f6" --description "Ready for review" --force
gh label create "status: work-in-progress" --color "8b5cf6" --description "Active work in progress" --force
gh label create "status: ready-to-merge" --color "10b981" --description "Approved and ready to merge" --force
echo "✅ Status labels created (5)"

# Work type labels
echo "Creating work type labels..."
gh label create "type: feature" --color "10b981" --description "New feature or enhancement" --force
gh label create "type: bugfix" --color "ef4444" --description "Bug fix" --force
gh label create "type: refactor" --color "8b5cf6" --description "Code refactoring, no functional changes" --force
gh label create "type: docs" --color "3b82f6" --description "Documentation only changes" --force
gh label create "type: chore" --color "6b7280" --description "Maintenance, dependencies, config" --force
gh label create "type: hotfix" --color "dc2626" --description "Emergency production fix" --force
echo "✅ Work type labels created (6)"

# Special labels
echo "Creating special labels..."
gh label create "special: breaking-change" --color "dc2626" --description "Contains breaking changes" --force
gh label create "special: dependencies" --color "0366d6" --description "Dependency updates" --force
gh label create "special: security" --color "dc2626" --description "Security-related changes" --force
gh label create "special: good-first-issue" --color "7057ff" --description "Good for newcomers to the project" --force
gh label create "special: help-wanted" --color "008672" --description "Extra attention or help needed" --force
gh label create "special: question" --color "d876e3" --description "Further information requested" --force
echo "✅ Special labels created (6)"

echo ""
echo "🎉 Label setup complete!"
echo ""
echo "📊 Summary:"
echo "  - Agent labels: 4"
echo "  - Phase labels: 5"
echo "  - Content type labels: 6"
echo "  - Priority labels: 4"
echo "  - Status labels: 5"
echo "  - Work type labels: 6"
echo "  - Special labels: 6"
echo "  ──────────────────"
echo "  Total: 36 labels"
echo ""
echo "✅ All labels created successfully!"
echo ""
echo "Next steps:"
echo "1. Review labels in GitHub: https://github.com/$REPO/labels"
echo "2. Create PR template: .github/PULL_REQUEST_TEMPLATE.md"
echo "3. Create issue templates: .github/ISSUE_TEMPLATE/"
echo "4. Set up auto-labeler workflow"
echo ""
echo "See AUTOMATION_IMPROVEMENTS.md for detailed implementation guide."
echo ""
