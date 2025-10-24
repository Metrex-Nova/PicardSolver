# PicardSolver

PicardSolver is a Python implementation of the Picard iteration method for approximating solutions to ordinary differential equations (ODEs). This project focuses on solving initial value problems (IVPs) using successive approximations to converge on the exact solution within a specified tolerance.

## Overview

The code approximates the solution of ODEs by converting the differential equation into an integral equation and iteratively refining the solution. Specifically, it solves the initial value problem:

\[
\frac{du}{dt} = u, \quad u(0) = 1
\]

using the Picard iteration sequence:

\[
u_{n+1}(t) = 1 + \int_0^t u_n(s) \, ds
\]

Starting with \( u_0(t) = 1 \), the iterations converge to the exact solution \( u(t) = e^t \).

## Features

- Symbolic integration using SymPy to perform the Picard iterations.
- Numerical evaluation and plotting of iterative approximations.
- Automatic convergence check against user-defined tolerance.
- Visualization of approximates alongside the exact solution for clarity.
- Modular design for adaptation to other ODEs solvable via Picard method.

## Requirements

- Python 3.x
- NumPy
- SymPy
- Matplotlib

Install dependencies via pip if needed:


