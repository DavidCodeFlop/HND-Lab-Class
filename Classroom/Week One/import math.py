import math
import pandas as pd

def generate_bigO_data(start=1, end=20):
    rows = []
    for n in range(start, end):
        o_1 = 1
        o_log_n = round(math.log2(n), 2)
        o_n = n
        o_n_log_n = round(n * math.log2(n), 2)
        o_n2 = n**2
        o_n3 = n**3
        o_exp = 2**n
        o_fact = math.factorial(n)
        rows.append(
            {
                "n": n,
                "O(1)": o_1,
                "O(log n)": (
                    f"{o_log_n:.2f}" if o_log_n != int(o_log_n) else str(int(o_log_n))
                ),
                "O(n)": o_n,
                "O(n log n)": (
                    f"{o_n_log_n:.2f}"
                    if o_n_log_n != int(o_n_log_n)
                    else str(int(o_n_log_n))
                ),
                "O(n*n)": o_n2,
                "O(n*n*n)": o_n3,
                "Exponential O(2^n)": f"{o_exp:,}",
                "Factorial O(n!)": f"{o_fact:,}",
            }
        )

    df = pd.DataFrame(rows)
    print(df.to_markdown(index=False))

if __name__ == "__main__":
    generate_bigO_data()
