# NCKH – Hybrid Quantum Computing and Graph Neural Network Techniques for IoT Intrusion Detection in 5G Edge Computing

Welcome to the research repository for **Hybrid Quantum Computing and Graph Neural Network Techniques for IoT Intrusion Detection in 5G Edge Computing**.

This project investigates the application of Quantum Graph Neural Networks (QGNN) and classical Graph Neural Networks to enhance the detection of anomalous traffic and intrusions in 5G-enabled IoT edge networks.

## 📖 Introduction
For a detailed theoretical background and introduction to the concepts used in this research (IoT, IDS, GNN, Quantum Computing, and QGNN), please refer to the [INTRODUCE.md](INTRODUCE.md) file.

## 📂 Project Structure

```text
/
├── data/                        # Dữ liệu phục vụ cho huấn luyện mô hình
│   └── raw/                     # File dữ liệu thô (vd: tron.csv)
├── docs/                        # Tài liệu dự án
│   ├── img/                     # Thư mục chứa hình ảnh minh họa
│   ├── references/              # Các tài liệu PDF tham khảo và lý thuyết
│   └── reports/                 # Các báo cáo tiến độ và kết quả (.docx)
├── notebooks/                   # Jupyter Notebooks cho quá trình EDA và thử nghiệm mô hình
│   └── Quantum_CNN_for_Intrusion_Detection_On_MIot_dataset.ipynb
├── scripts/                     # Các file mã nguồn chạy độc lập
│   └── analyze.py               # Phân tích dữ liệu
├── src/                         # Mã nguồn chính của dự án (kiến trúc mô hình, utils, etc.)
├── INTRODUCE.md                 # Giới thiệu chi tiết về bối cảnh nghiên cứu
└── README.md                    # File thông tin tổng quan dự án
```

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed. It is recommended to use a virtual environment (e.g., `venv` or `conda`) to manage dependencies.

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd NCKH-hybrid-Quantum-Computing-and-GNNTechniques-for-IoT-IDS-in-5G-Edge-Computing-1
   ```

2. *(To be updated)* Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

- **Data Analysis**: Run the analysis script to explore the dataset.
  ```bash
  python scripts/analyze.py
  ```
- **Model Training / Testing**: Open the notebooks in `notebooks/` via Jupyter to see the interactive experiments.

## 📊 Results & Reports

Detailed progress reports and results tested on various datasets (TON_IoT, IDS2017, CTU) can be found in the `docs/reports/` directory.