import os
import argparse
import signal
import sys
import subprocess


def signal_handler(signum, frame):
    print("\nReceived signal to suspend. Cleaning up subprocesses...")
    # Kill any running subprocesses
    if hasattr(signal_handler, "current_process"):
        try:
            signal_handler.current_process.terminate()
        except:
            pass
    sys.exit(0)


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
        "--port", type=int, default=3000, help="Port to use (default: 3000)"
    )
    parser.add_argument(
        "--behaviors", type=str, help="comma separated list of behavior ids to run"
    )
    parser.add_argument(
        "--skip",
        type=str,
        help="comma separated list of behavior ids to skip",
        default="65,66,67,68",
    )
    args = parser.parse_args()

    # Set up signal handler for SIGTSTP (Ctrl+Z)
    signal.signal(signal.SIGTSTP, signal_handler)

    behaviors = set()
    if args.behaviors:
        behaviors.update(map(int, args.behaviors.split(",")))
    else:
        behaviors = set(range(100))
    if args.skip:
        behaviors.difference_update(map(int, args.skip.split(",")))

    for i in sorted(behaviors):
        cmd = f"sh ../websites/experiment_opendevin.sh --behavior_id={i} --llm_name={args.llm_name} --agent_name={args.agent_name} --env_name=hbb --port={args.port}"
        # Store the current process in the signal handler for cleanup
        signal_handler.current_process = subprocess.Popen(cmd, shell=True)
        signal_handler.current_process.wait()


if __name__ == "__main__":
    main()
