# physical-ai-journey

**From firmware and electronics to ML engineer in robotics — built in public.**

This repo is my learning log. I'm following a 65-week roadmap where every week ends with something that runs: a simulator, a controller, a trained policy, or code on real hardware. One project thread connects it all, from a pendulum simulated in NumPy to a learned policy running in C++ on a real robot.

📅 **60-day challenge:** daily updates on X → [Tzyckiii](https://x.com/TZyckiii)
🗺️ **Full week-by-week plan with all materials:** [ROADMAP.md](ROADMAP.md)

---

## The plan at a glance

| Phase | Weeks | Focus | Milestone |
| --- | --- | --- | --- |
| 1 | 1–13 | ML foundations through projects: pendulum simulator, LQR, autograd in C++, learned dynamics, MPC | Gate 1: training loop from scratch, no notes |
| 2 | 14–26 | Robot learning in simulation: my own PPO, MuJoCo, domain randomization, ROS 2 + C++ policy node | Gate 2: robustness table |
| 3 | 27–35 | Sim-to-real on real hardware: system identification, onboard C++ inference, safety layer | Gate 3: project 1 public, video |
| 4 | 36–48 | Imitation learning theory (ACT, Diffusion Policy, VLA models), SO-101 arm setup and teleoperation | Gate 4: first demonstrations recorded |
| 5 | 49–65 | Project 2: pick-and-place on SO-101, ACT vs SmolVLA, C++ edge inference with latency benchmarks | Project 2 public |

**Rules I follow**

- 6–8 h per week: about 1/3 reading, 2/3 building.
- Materials only when the project needs them.
- Nothing gets thrown away: each project builds on the previous one.
- Missed a week? Shift the schedule, don't cut the deliverable.

---

## The first 60 days

| Week | What I build | Deliverable | Status |
| --- | --- | --- | --- |
| 1 | Environment + pendulum simulator in NumPy with RK4 integration | Angle-over-time plot | ⬜ |
| 2 | Vectorization: 1000 pendulums at once, no loops | Loop vs vectorized benchmark | ⬜ |
| 3 | Linearization, eigenvalues, LQR for the inverted pendulum | Pendulum stabilized by LQR | ⬜ |
| 4 | micrograd in Python: autograd from scratch | Working autograd with gradient tests | ⬜ |
| 5 | micrograd ported to C++: computation graph, backprop, small MLP | Autograd in C++ | ⬜ |
| 6 | Probability in practice: sensor noise, MLE, fusing two measurements | Notebook on measurement uncertainty | ⬜ |
| 7 | Pendulum dynamics model as an MLP in PyTorch | 1-step vs 50-step prediction error | ⬜ |
| 8 | Light week: documentation and cleanup of weeks 1–7 | Every project folder has a README | ⬜ |
| 9 | Optimization: SGD vs Adam, LR schedules, input normalization | Optimizer comparison table | ⬜ |

Status: ⬜ not started · 🟨 in progress · ✅ done

---

## Repo structure

```
physical-ai-journey/
├── README.md
├── ROADMAP.md
├── phase-1/
│   ├── 01-pendulum-sim/
│   ├── 02-vectorization/
│   ├── 03-lqr/
│   ├── 04-micrograd-py/
│   ├── 05-micrograd-cpp/
│   └── ...
├── phase-2/
└── log/
    └── day-01.md
```

Each project folder has its own short README: what it does, how to run it, and the result (plot, GIF or numbers).

---

## Stack

Python · NumPy · SciPy · PyTorch · C++ · ONNX Runtime · MuJoCo · Gymnasium · ROS 2 · LeRobot

---

## Results

Key results land here as they come in.

- _Coming soon: pendulum simulator (week 1)_

---

## Follow along

X: [@Tzyckiii](https://x.com/TZyckiii)

Feedback, suggestions and corrections are very welcome — open an issue or reply on X.
