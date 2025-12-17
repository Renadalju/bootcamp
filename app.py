import pandas as pd
import streamlit as st
import csv
from io import StringIO
import sys
from pathlib import Path
import tempfile
import json

# Allow imports from src/
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from csv_profiler.profile import basic_profile
from csv_profiler.render import write_markdown, write_json



# Streamlit Page Config
st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")


# Upload CSV
uploaded = st.file_uploader("Upload a CSV", type=["csv"])
show_preview = st.checkbox("Show preview", value=True)

rows: list[dict] = []

if uploaded is None:
    st.info("📂 Please upload a CSV file to begin.")
    st.stop()

try:
    text = uploaded.getvalue().decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))
except Exception as e:
    st.error(f"❌ Failed to read CSV: {e}")
    st.stop()

if len(rows) == 0:
    st.error("CSV has no data. Upload a CSV with at least 1 row.")
    st.stop()

if len(rows[0]) == 0:
    st.warning("CSV has no headers (no columns detected).")


# CSV Info
st.write("**Filename:**", uploaded.name)
st.write("**Rows Loaded:**", len(rows))

if show_preview:
    st.subheader("Preview (first 5 rows)")
    st.dataframe(pd.DataFrame(rows[:5]), use_container_width=True)


# Generate Report
if st.button("Generate Report"):
    report = basic_profile(rows)
    st.session_state["report"] = report

report = st.session_state.get("report")


# Display + Export
if report:
    #  Report name
    report_name = st.text_input("Report name", value="report")

    tab1, tab2, tab3 = st.tabs(
        ["📊 Tables", "📝 Markdown Report", "⬇️ Export"]
    )

    #  Tab 1: Tables 
    with tab1:
        st.subheader("Dataset Summary")

        summary_df = pd.DataFrame(
            {
                "Metric": ["Rows", "Columns"],
                "Value": [report["rows"], report["n_cols"]],
            }
        )
        st.table(summary_df)

        st.subheader("Missing & Non-empty Counts per Column")

        cols = report["columns"]
        missing = report["missing"]
        non_empty = report["non_empty"]

        counts_df = pd.DataFrame({
            "Column": cols,
            "Missing": [missing[c] for c in cols],
            "Non-empty": [non_empty[c] for c in cols],
        })

        st.dataframe(counts_df, use_container_width=True)

    #  Tab 2: Markdown 
    with tab2:
        with tempfile.TemporaryDirectory() as tmpdir:
            md_path = Path(tmpdir) / f"{report_name}.md"
            write_markdown(report, md_path)
            markdown_text = md_path.read_text(encoding="utf-8")

        st.markdown(markdown_text)

    #  Tab 3: Export 
    with tab3:
        st.subheader("Download")

        json_bytes = json.dumps(report, indent=2, ensure_ascii=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download JSON",
            data=json_bytes,
            file_name=f"{report_name}.json",
            mime="application/json",
        )

        st.download_button(
            label="⬇️ Download Markdown",
            data=markdown_text,
            file_name=f"{report_name}.md",
            mime="text/markdown",
        )

        st.divider()

        # Save to outputs/ 
        if st.button("💾 Save to outputs/"):
            outputs_dir = Path("outputs")
            outputs_dir.mkdir(exist_ok=True)

            json_path = outputs_dir / f"{report_name}.json"
            md_path = outputs_dir / f"{report_name}.md"

            write_json(report, json_path)
            write_markdown(report, md_path)

            st.success("✅ Saved report.json and report.md to outputs/")
