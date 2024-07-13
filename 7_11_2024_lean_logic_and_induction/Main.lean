import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.Finset
import Mathlib.Algebra.GeomSum

/- Supply proofs for 2 out of the 3 assignments.
   Do all 3 for 5 points of extra credit.

   All assignments can be proven through induction and appropriate use of library functions and logic operations.
-/

-- Assignment 1: Show that 2^n % 7 = 1, 2, or 4 for all n.
theorem assignment1 : ∀ n:ℕ, 2^n % 7 = 1 ∨ 2^n % 7 = 2 ∨ 2^n % 7 = 4 := by
  intro n
  induction n with
  | zero =>
    left
    ring
  | succ n ih =>
    cases ih with
    | inl h_left =>
      right
      left
      rw [pow_succ, Nat.mul_mod]
      simp [h_left]
    |inr h_right =>
      cases h_right with
      | inl h_right =>
        right
        right
        rw [pow_succ, Nat.mul_mod]
        simp [h_right]
      | inr h_left =>
        left
        rw [pow_succ, Nat.mul_mod]
        simp [h_left]

-- Assignment 2: Show that (1-x)*(1+x+x^2+...+x^{n-1}) = (1-x^n)
theorem assignment2
    (x:ℝ)
    : ∀ n:ℕ, (1-x)*(∑ i ∈ Finset.range n, x^i) = 1-x^n := by
    intro n
    induction n with
    | zero =>
      simp
    | succ n ih =>
      rw [Finset.sum_range_succ]
      rw [mul_add]
      rw [ih]
      rw [pow_succ]
      ring

-- Assignment 3: Show that if a_0 = 0, a_{n+1} = 2*a_n+1 then a_n = 2^n-1.
theorem assignment3
    (a: ℕ → ℝ) (h_zero: a 0 = 0) (h_rec: ∀ n:ℕ, a (n+1) = 2 * (a n) + 1)
    : ∀ n:ℕ, a n = 2^n - 1 := by
    intro n
    induction n with
    | zero =>
      rw [h_zero]
      simp
    | succ n ih =>
      calc a (n + 1) = (2 * (a n)) + 1 := by rw [h_rec]
                  _  = (2 * ((2^n) - 1)) + 1 := by rw [ih]
                  _  = (2^(n + 1) - 2) + 1 := by ring
                  _ = 2^(n + 1) - 1 := by ring
