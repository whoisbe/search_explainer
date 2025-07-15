# utils/hybrid_search.py

import argparse
from collections import defaultdict
from utils.schema import get_connection
from utils.lexical_search import lexical_search
from utils.fts_search import full_text_search
from utils.vss import vector_search

DEFAULT_K = 60
DEFAULT_LIMIT = 10

def rrf_score(rank, k=DEFAULT_K):
    return 1 / (k + rank)

def reciprocal_rank_fusion(results_lists, k=DEFAULT_K):
    scores = defaultdict(float)
    seen = {}

    for result_list in results_lists:
        for rank, item in enumerate(result_list):
            movie_id = item[0]  # id is expected to be at index 0
            score = rrf_score(rank, k)
            scores[movie_id] += score
            seen[movie_id] = item  # Save the full result (overwrite is fine)

    # Sort by aggregated RRF score
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [(seen[mid], score) for mid, score in ranked]

def run_hybrid_search(query, limit, k):
    con = get_connection(readonly=True)

    # Collect ranked lists from all methods
    lex_results = lexical_search(query, con, limit=limit)
    fts_results = full_text_search(query, con, limit=limit)
    vss_results = vector_search(query, con, limit=limit)

    # Each list is a list of tuples with movie id as first element
    fused = reciprocal_rank_fusion([lex_results, fts_results, vss_results], k=k)

    print(f"\n🔎 Hybrid Search Results for query: '{query}'\n")
    for i, (row, score) in enumerate(fused[:limit], start=1):
        print(f"#{i} 🎬 {row[1]} (ID: {row[0]}) | RRF Score: {score:.4f}\n📝 {row[2]}\n{'-'*40}")

    con.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hybrid Search with RRF")
    parser.add_argument("query", type=str, help="Search query text")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="Limit number of results")
    parser.add_argument("--rrf_k", type=int, default=DEFAULT_K, help="RRF k parameter (default 60)")

    args = parser.parse_args()

    run_hybrid_search(args.query, args.limit, args.rrf_k)
