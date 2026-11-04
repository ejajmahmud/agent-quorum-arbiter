"""Byzantine fault tolerant voting arbiter for multi-agent decisions."""
from typing import Dict, List, Any


class QuorumArbiter:
    def __init__(self, total_nodes: int):
        self.total_nodes = total_nodes
        # Byzantine requirement: N >= 3F + 1 => max F = (N - 1) // 3
        self.max_faulty = (total_nodes - 1) // 3
        self.required_quorum = (2 * total_nodes // 3) + 1
        self._ballots: Dict[str, Dict[str, str]] = {}

    def cast_vote(self, proposal_id: str, voter_id: str, decision: str):
        if proposal_id not in self._ballots:
            self._ballots[proposal_id] = {}
        self._ballots[proposal_id][voter_id] = decision

    def tally(self, proposal_id: str) -> Dict[str, Any]:
        votes = self._ballots.get(proposal_id, {})
        counts: Dict[str, int] = {}
        for dec in votes.values():
            counts[dec] = counts.get(dec, 0) + 1

        winner = None
        for dec, count in counts.items():
            if count >= self.required_quorum:
                winner = dec
                break

        return {
            "proposal_id": proposal_id,
            "total_votes_cast": len(votes),
            "required_quorum": self.required_quorum,
            "has_consensus": winner is not None,
            "decision": winner,
            "tally_breakdown": counts
        }
