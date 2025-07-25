#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <tuple>
#include <algorithm>
#include <utility>

// Use the standard namespace for brevity
using namespace std;

// Global variables to match the structure of the Python script
int N, M, Q;
// The graph is represented as a vector of maps.
// graph[u] maps a neighbor 'v' to a pair {cost, edge_index}.
vector<map<int, pair<int, int>>> graph;
// 'cycle' stores the biconnected components that are simple cycles.
// Each cycle is a set of its edges, represented as tuples {cost, u, v}.
vector<set<tuple<int, int, int>>> cycle;
// 'position[i]' stores the index in the 'cycle' vector where edge 'i' is located.
// It's -1 if the edge is not part of a cycle.
vector<int> position;
// 'SUM' holds the total cost of the minimum spanning cactus.
long long SUM = 0;

// Global variables for the DFS algorithm
vector<int> visit;
int dfs_cnt = 0;
// 'edge_stack' is used by the DFS to identify biconnected components.
vector<tuple<int, int, int>> edge_stack;

/**
 * @brief Performs a Depth First Search to find biconnected components (cycles).
 *
 * This function is a C++ translation of the Python DFS logic. It uses discovery times
 * and an edge stack to identify cycles (BCCs with more than 2 edges).
 *
 * @param x The current vertex.
 * @param bx The parent vertex in the DFS tree, to avoid traversing back immediately.
 * @return The lowest discovery time reachable from vertex x.
 */
int dfs(int x, int bx) {
    visit[x] = ++dfs_cnt;
    int min_val = visit[x];

    for (auto const& [nx, val] : graph[x]) {
        if (nx == bx) continue;

        auto [nc, ni] = val;

        // This condition, as in the Python code, pushes any edge that doesn't lead
        // to a direct ancestor in the current DFS path onto the stack.
        if (visit[x] >= visit[nx]) {
            edge_stack.emplace_back(nc, x, nx);
        }

        if (visit[nx] == 0) { // If vertex nx has not been visited yet
            int temp = dfs(nx, x);

            // If the subtree rooted at nx cannot reach an ancestor of x,
            // then x is an articulation point, and a BCC has been found.
            if (temp >= visit[x]) {
                set<tuple<int, int, int>> bcc;

                // Pop edges from the stack until the current tree edge (x, nx) is found.
                // These popped edges form the BCC.
                while (!edge_stack.empty()) {
                    auto [w, u, v] = edge_stack.back();
                    edge_stack.pop_back();

                    bcc.insert({w, min(u, v), max(u, v)});
                    // Tentatively assign the current cycle index to the edge's position.
                    position[graph[u][v].second] = cycle.size();

                    if (w == nc && u == x && v == nx) {
                        break;
                    }
                }

                if (bcc.size() > 2) {
                    // If the BCC has more than 2 edges, it's a valid cycle.
                    cycle.push_back(bcc);
                } else {
                    // Otherwise, it's a bridge. Reset the position for its edges to -1.
                    for (const auto& edge : bcc) {
                        // Edges in the set are normalized {w, min_v, max_v}
                        position[graph[get<1>(edge)][get<2>(edge)].second] = -1;
                    }
                }
            }
            min_val = min(min_val, temp);
        } else { // If nx is already visited, it's a back edge.
            min_val = min(min_val, visit[nx]);
        }
    }
    return min_val;
}

int main() {
    // Fast I/O for performance
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M >> Q;

    // Initialize data structures
    graph.resize(N + 1);
    position.assign(M, -1);

    for (int i = 0; i < M; ++i) {
        int u, v, c;
        cin >> u >> v >> c;
        graph[u][v] = {c, i};
        graph[v][u] = {c, i};
        SUM += c;
    }

    // Find all cycles using DFS starting from node 1.
    // Assumes the graph is connected.
    visit.assign(N + 1, 0);
    dfs(1, 1);

    // Initial calculation: for each cycle, subtract the weight of the heaviest edge
    // if it's positive. This minimizes the total cost.
    for (const auto& bcc : cycle) {
        if (!bcc.empty()) {
            // The max element in a std::set is the last one (*rbegin()).
            int max_weight = get<0>(*bcc.rbegin());
            if (max_weight > 0) {
                SUM -= max_weight;
            }
        }
    }

    cout << SUM << "\n";

    // Process Q queries for edge weight updates
    for (int q = 0; q < Q; ++q) {
        int u, v, d;
        cin >> u >> v >> d;

        auto [c, i] = graph[u][v]; // Get old cost and edge index

        graph[u][v] = {d, i};      // Update graph with new cost
        graph[v][u] = {d, i};

        int p = position[i];

        if (p < 0) {
            // Case 1: The edge is not in a cycle (it's a bridge in the cactus).
            // The change in its cost directly affects the total sum.
            SUM = SUM - c + d;
        } else {
            // Case 2: The edge is in a cycle.
            if (u > v) swap(u, v); // Normalize vertex order for set lookup

            // Get the max edge weight in the cycle BEFORE the change.
            int max1_weight = get<0>(*cycle[p].rbegin());

            // Update the edge in its cycle set.
            cycle[p].erase({c, u, v});
            cycle[p].insert({d, u, v});

            // Get the max edge weight in the cycle AFTER the change.
            int max2_weight = get<0>(*cycle[p].rbegin());

            // Update the total SUM.
            // 1. Account for the direct change in edge weight (-c + d).
            // 2. Add back the old subtracted value (max(0, max1_weight)).
            // 3. Subtract the new value that should be removed (max(0, max2_weight)).
            SUM = SUM - c + d;
            if (max1_weight > 0) SUM += max1_weight;
            if (max2_weight > 0) SUM -= max2_weight;
        }
        cout << SUM << "\n";
    }

    return 0;
}