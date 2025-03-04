import os
import argparse


def main():
    parser = argparse.ArgumentParser(description="Run batch experiments with OpenDevin")
    parser.add_argument(
        "--llm_name",
        type=str,
        required=True,
        help='LLM name (should be the suffix following "llm." in the corresponding config.toml section)',
    )
    parser.add_argument(
        "--agent_name",
        type=str,
        required=True,
        help="Agent name to use for the experiments",
    )
    parser.add_argument(
        "--port", type=int, default=3333, help="Port to use (default: 3333)"
    )
    parser.add_argument(
        "--behaviors", type=str, help="comma separated list of behavior ids to run"
    )
    parser.add_argument(
        "--skip", type=str, help="comma separated list of behavior ids to skip"
    )
    args = parser.parse_args()

    behaviors = set()
    if args.behaviors:
        behaviors.update(map(int, args.behaviors.split(",")))
    else:
        behaviors = set(range(100))
    if args.skip:
        behaviors.difference_update(map(int, args.skip.split(",")))

    for i in behaviors:
        os.system(
            f"sh ../websites/experiment_opendevin.sh --behavior_id={i} --llm_name={args.llm_name} --agent_name={args.agent_name} --env_name=hbb --port={args.port}"
        )


if __name__ == "__main__":
    main()
