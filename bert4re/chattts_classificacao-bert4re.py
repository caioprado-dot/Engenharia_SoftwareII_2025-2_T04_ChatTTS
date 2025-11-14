#!/usr/bin/env python3
"""
Classifica automaticamente o código-fonte do ChatTTS usando o modelo BERT4RE
para detectar padrões de arquitetura de software.
"""

import os
import argparse
from transformers import pipeline
from tqdm import tqdm
import pandas as pd


#  FUNÇÃO PRINCIPAL
def main(repo_path):
    # Carrega modelo
    classifier = pipeline(
        "text-classification",
        model="thearod5/bert4re",
        truncation=True,
        max_length=512,
        top_k=None
    )

    # Labels-alvo (arquitetura)
    labels = [
        "pipeline",
        "mvc", "layers", "microservices", "blackboard",
        "event-driven", "client-server", "repository", "pipe-filter"
    ]

    # Coleta arquivos do repo
    def collect_files(base_path, exts=(".py", ".js", ".ts", ".cpp", ".json", ".md")):
        files = []
        for root, _, fnames in os.walk(base_path):
            for f in fnames:
                if f.endswith(exts):
                    files.append(os.path.join(root, f))
        return files

    source_files = collect_files(repo_path)
    print(f"Encontrados {len(source_files)} arquivos.")

    # Classificação de um arquivo
    def classify_file(path):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception as e:
            return {"file": path, "error": str(e)}

        if len(content) > 2000:
            content = content[:2000]

        scores = {}

        for lbl in labels:
            prompt = f"This source code is about {lbl}."
            text = content + "\n" + prompt

            result = classifier(text, truncation=True, max_length=512)

            # Normalização do retorno
            if isinstance(result, list) and len(result) > 0 and isinstance(result[0], dict):
                r = result[0]
            elif isinstance(result, list) and len(result) > 0 and isinstance(result[0], list):
                r = result[0][0]
            else:
                r = {"label": "LABEL_0", "score": 0.0}

            score = r["score"] if r["label"].startswith("LABEL_1") else 1 - r["score"]
            scores[lbl] = score

        top3 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
        return {"file": path, "top_labels": [lbl for lbl, _ in top3]}

    # Executa classificação
    results = []
    for path in tqdm(source_files):
        results.append(classify_file(path))

    # Salva como CSV
    df = pd.DataFrame([
        {"file": r["file"], "top_labels": ", ".join(r["top_labels"])}
        for r in results if "top_labels" in r
    ])

    df.to_csv("chattts_architecture_labels.csv", index=False)
    print("\n✅ Arquivo gerado: chattts_architecture_labels.csv")

# CLI
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classifica arquitetura no código do ChatTTS.")
    parser.add_argument(
        "--repo",
        type=str,
        required=True,
        help="Caminho para o diretório do código-fonte do ChatTTS"
    )
    args = parser.parse_args()
    main(args.repo)

