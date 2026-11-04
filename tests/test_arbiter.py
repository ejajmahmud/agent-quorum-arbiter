"""Tests for agent-quorum-arbiter."""
import unittest
from agent_quorum_arbiter.arbiter import QuorumArbiter


class TestQuorumArbiter(unittest.TestCase):
    def setUp(self):
        self.arbiter = QuorumArbiter(total_nodes=4)

    def test_supermajority_consensus(self):
        self.arbiter.cast_vote("p1", "a1", "YES")
        self.arbiter.cast_vote("p1", "a2", "YES")
        self.arbiter.cast_vote("p1", "a3", "YES")
        self.arbiter.cast_vote("p1", "a4", "NO")
        res = self.arbiter.tally("p1")
        self.assertTrue(res["has_consensus"])
        self.assertEqual(res["decision"], "YES")

    def test_insufficient_quorum(self):
        self.arbiter.cast_vote("p2", "a1", "YES")
        self.arbiter.cast_vote("p2", "a2", "NO")
        res = self.arbiter.tally("p2")
        self.assertFalse(res["has_consensus"])
        self.assertIsNone(res["decision"])


if __name__ == "__main__":
    unittest.main()
