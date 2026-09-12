"""Basic tower defense game loop skeleton."""

from __future__ import annotations

import argparse
import time


def run_game_loop(max_ticks: int | None = None, target_fps: int = 60) -> None:
    """Run the main game loop skeleton.

    Args:
        max_ticks: Optional tick limit to stop the loop.
        target_fps: Target loop frequency.
    """
    tick = 0
    tick_duration = 1 / target_fps

    print("Starting tower defense loop...")

    try:
        while True:
            frame_start = time.perf_counter()

            # 1) Poll input/events
            # 2) Update game state
            # 3) Render frame

            tick += 1
            if max_ticks is not None and tick >= max_ticks:
                break

            elapsed = time.perf_counter() - frame_start
            time.sleep(max(0, tick_duration - elapsed))
    except KeyboardInterrupt:
        print("Loop interrupted by user.")

    print(f"Loop stopped after {tick} tick(s).")


def main() -> None:
    parser = argparse.ArgumentParser(description="Tower defense loop skeleton")
    parser.add_argument(
        "--ticks",
        type=int,
        default=None,
        help="Optional number of ticks before exiting (useful for quick checks).",
    )
    args = parser.parse_args()
    run_game_loop(max_ticks=args.ticks)


if __name__ == "__main__":
    main()
