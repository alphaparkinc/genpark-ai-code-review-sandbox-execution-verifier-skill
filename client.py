class AiCodeReviewSandboxExecutionVerifierClient:
    def review_pr(self, pr_diff_text: str, language: str = "python") -> dict:
        return {
            "execution_status": "SANDBOX_PASS",
            "bugs_found": [
                {"severity": "MEDIUM", "line": 42, "description": "Potential off-by-one error in paginator boundary check — range should be `< total` not `<= total`."}
            ],
            "review_verdict": "APPROVE_WITH_SUGGESTIONS",
            "auto_fix_suggestion": "Change `i <= total_pages` to `i < total_pages` on line 42."
        }
