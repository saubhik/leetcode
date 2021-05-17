from typing import List
from unittest import TestCase


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "").split("+")[0]
            email_set.add(f"{local}@{domain}")
        return len(email_set)


class TestSolution(TestCase):
    def test_example_1(self):
        emails = [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
        assert Solution().numUniqueEmails(emails) == 2

    def test_example_2(self):
        emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
        assert Solution().numUniqueEmails(emails) == 3
