"""CLI for agent-quorum-arbiter."""
import sys
import argparse
from .arbiter import QuorumArbiter


def main():
    parser = argparse.ArgumentParser(description="Agent Quorum Arbiter")
    parser.add_argument("--nodes", type=int, default=5, help="Total agent nodes")
    args = parser.parse_args()

    arbiter = QuorumArbiter(args.nodes)
    arbiter.cast_vote("prop_1", "agent_1", "APPROVE")
    arbiter.cast_vote("prop_1", "agent_2", "APPROVE")
    arbiter.cast_vote("prop_1", "agent_3", "APPROVE")
    arbiter.cast_vote("prop_1", "agent_4", "APPROVE")
    res = arbiter.tally("prop_1")
    print(f"Consensus achieved: {res['has_consensus']}, Decision: {res['decision']}")
    sys.exit(0)


if __name__ == "__main__":
    main()
