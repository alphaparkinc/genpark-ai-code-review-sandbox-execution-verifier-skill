from client import AiCodeReviewSandboxExecutionVerifierClient

def main():
    client = AiCodeReviewSandboxExecutionVerifierClient()
    diff = """
-    for i in range(0, total_pages + 1):
+    for i in range(0, total_pages):
         fetch_page(i)
    """
    res = client.review_pr(diff, "python")
    print(f"Execution Status: {res['execution_status']}")
    print(f"Review Verdict: {res['review_verdict']}")
    print(f"Auto-Fix: {res['auto_fix_suggestion']}")
    print("Bugs Found:", res["bugs_found"])

if __name__ == "__main__":
    main()
