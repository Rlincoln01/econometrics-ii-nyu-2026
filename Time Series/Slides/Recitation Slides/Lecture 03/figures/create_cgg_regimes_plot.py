"""
Create CGG-style plot: Fed funds rate and inflation with shaded regime areas
(Burns, Miller, Volcker). Similar to Clarida, Galí, Gertler (1999/QJE 2000).

Saves: cgg_regimes.png in this folder.

Requires: pandas, matplotlib. For live FRED fetch: pandas_datareader and FRED_API_KEY.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Try FRED; fallback to pre-downloaded CSV or synthetic for demo
import pandas as pd
import os

df = None
try:
    import pandas_datareader as pdr
    fred_key = os.environ.get("FRED_API_KEY")
    if fred_key:
        ff = pdr.get_data_fred("FEDFUNDS", start="1959-01-01", end="1996-12-31", api_key=fred_key)
        cpi = pdr.get_data_fred("CPIAUCSL", start="1959-01-01", end="1996-12-31", api_key=fred_key)
        ff = ff.squeeze()
        cpi = cpi.squeeze()
        inf = cpi.pct_change(12) * 100  # y/y inflation in percent
        df = pd.DataFrame({"ff": ff, "inflation": inf}).dropna()
except Exception:
    pass
if df is None:
    csv_path = Path(__file__).resolve().parent / "cgg_regimes_data.csv"
    if csv_path.exists():
        df = pd.read_csv(csv_path, index_col=0, parse_dates=True)
    else:
        print("FRED_API_KEY not set and no cgg_regimes_data.csv. Using synthetic data.")
        dates = pd.date_range("1959-01-01", "1996-12-31", freq="MS")
        np.random.seed(42)
        t = np.arange(len(dates))
        inf = 2 + 0.03 * t + 0.5 * np.sin(2 * np.pi * t / 40) + np.random.randn(len(dates)) * 0.5
        inf = np.clip(inf.cumsum() * 0.02 + 2, 0, 18)
        inf[400:450] += np.linspace(0, 8, 50)
        ff = inf + np.random.randn(len(dates)) * 1.5
        ff = np.clip(ff, 0, 22)
        df = pd.DataFrame({"ff": ff, "inflation": inf}, index=dates)

# Resample to quarterly (end of quarter) to match CGG style
df = df.resample("QE").mean().dropna()

# Regime dates (Fed chair tenures): Burns 1970-78, Miller 1978-79, Volcker 1979-87
regimes = [
    ("Burns", "1970-01-01", "1978-02-01", 0.92, 0.95, 0.95),   # light gray
    ("Miller", "1978-03-01", "1979-08-01", 0.85, 0.88, 0.95),
    ("Volcker", "1979-08-01", "1987-08-01", 0.75, 0.85, 0.95),
]

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df.index, df["inflation"], color="black", lw=1.8, label="Inflation (y/y %)")
ax.plot(df.index, df["ff"], color="black", ls="--", lw=1.2, label="Fed funds rate (%)")

ymax = float(df[["ff", "inflation"]].max().max()) * 1.08
ax.set_ylim(0, ymax)
for name, start, end, r, g, b in regimes:
    ax.axvspan(start, end, alpha=0.35, color=(r, g, b), zorder=0)
    mid = pd.Timestamp(start) + (pd.Timestamp(end) - pd.Timestamp(start)) / 2
    ax.text(mid, ymax * 0.92, name, ha="center", va="top", fontsize=9, color="dimgray")

ax.set_ylabel("%")
ax.set_xlabel("")
ax.legend(loc="upper right", frameon=True)
ax.xaxis.set_major_locator(mdates.YearLocator(4))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%y"))
ax.grid(True, alpha=0.4)
fig.tight_layout()
out = Path(__file__).resolve().parent / "cgg_regimes.png"
fig.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved {out}")

# Save CSV for reuse when run with FRED (no key needed next time)
try:
    if fred_key and not (Path(__file__).resolve().parent / "cgg_regimes_data.csv").exists():
        df.to_csv(Path(__file__).resolve().parent / "cgg_regimes_data.csv")
except NameError:
    pass
