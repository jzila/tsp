from heapq import heapify, heappop, heappush
import math
from graph.structs import GraphError, Edge


def hull_from_points(points):
    # Pick the first point
    if len(points) < 3:
        raise GraphError("Cannot calculate hull for fewer than 3 points")

    points = sorted(points, lambda p1, p2: cmp(p1.x, p2.x))

    # Extract the left-most element and calculate all vectors from it
    p1 = points.pop(0)
    vectors = [p - p1 for p in points]

    # Extract any vector, calculate all angles to it, and store them all in a heap
    v1 = vectors[0]
    angles = [(v2.angle(v1), v2) for v2 in vectors]
    heapify(angles)

    # Initializes the edge set; the least-angle edge will always be in the hull
    edges = [Edge(p1, heappop(angles)[1])]

    while len(angles) > 0:
        (_, v) = heappop(angles)
        targetP = p1 + v
        while True:
            head = edges[-1]
            sourceP = head.endP()
            e = Edge(sourceP, targetP)

            if (head.angle(e) < 0):
                edges.append(e)
                break

            edges.pop()

    edges.append(Edge(edges[-1].endP(), p1))

    return edges


def tsp_from_points(points):
    edges = set(hull_from_points(points))

    # Clear points currently on edges
    used_points = {e.p for e in edges}
    unused_points = {p for p in points if not p in used_points}

    # Basic algorithm:
    # 1) For every edge, introduce a new point from the set of non-edged points.
    # 2) Pick the edge-point reroute that increases the size of the path by the least.
    while unused_points:
        deltas = []
        for e in edges:
            for p in unused_points:
                e1 = Edge(e.p, p)
                e2 = Edge(p, e.endP())
                delta = e1.mag() + e2.mag() - e.mag()
                heappush(deltas, (delta, {'old': e, 'new': (e1, e2)}))

        (delta, o) = heappop(deltas)
        edges.remove(o['old'])
        edges.update(set(o['new']))
        unused_points.remove(o['new'][1].p)

    return list(edges)
