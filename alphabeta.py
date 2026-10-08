
# Alpha-Beta Pruning
import math

def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):

    # Base case: leaf node reached
    if depth == height:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        for i in range(2):
            val = alpha_beta(
                depth + 1, nodeIndex * 2 + i,
                False, values, alpha, beta, height
            )

            best = max(best, val)
            alpha = max(alpha, best)

            # Beta cut-off
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            val = alpha_beta(
                depth + 1, nodeIndex * 2 + i,
                True, values, alpha, beta, height
            )

            best = min(best, val)
            beta = min(beta, best)

            # Alpha cut-off
            if beta <= alpha:
                break

        return best


# Main program
values = list(map(int, input("Enter 8 leaf node values: ").split()))

if len(values) != 8:
    print("Please enter exactly 8 values.")
else:
    height = 3

    result = alpha_beta(
        0, 0, True, values, -math.inf, math.inf, height
    )

    print("\nThe optimal value is:", result)
