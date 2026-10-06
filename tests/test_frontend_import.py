import os
import re
import subprocess
import sys
import unittest


ROOT = os.path.dirname(os.path.dirname(__file__))


class FrontendImportTests(unittest.TestCase):
    def test_frontend_module_import_is_not_eagerly_loading_backend_services(self):
        code = r'''
import sys
import time

ROOT = r"%s"
sys.path.insert(0, ROOT)

start = time.perf_counter()
import frontend.app
elapsed = time.perf_counter() - start
print(f"ELAPSED={elapsed:.2f}")
''' % ROOT

        result = subprocess.run(
            [sys.executable, "-c", code],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=15,
        )

        stdout = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0, stdout)

        match = re.search(r"ELAPSED=(\d+(?:\.\d+)?)", stdout)
        self.assertIsNotNone(match, stdout)
        elapsed = float(match.group(1))
        self.assertLess(elapsed, 5.0, f"Frontend import took too long: {elapsed}s\n{stdout}")

    def test_camera_component_uses_ready_state_text(self):
        html_path = os.path.join(ROOT, "frontend", "camera_component", "index.html")
        with open(html_path, "r", encoding="utf-8") as handle:
            content = handle.read()

        self.assertIn("Camera and microphone are ready.", content)
        self.assertIn("Requesting camera and microphone permission...", content)


if __name__ == "__main__":
    unittest.main()
