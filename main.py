from bst import BST
from graph import Graph
from hash_set import HashSet
from hash_table import HashTable
from min_heap import MinHeap
from linked_list import LinkedList
from linked_queue import Queue, board_passengers
from linked_stack import Stack, is_balanced


def main():
    """Runs the Metro City Navigator demonstration script automatically without user input."""
    print("=======================================")
    print("      METRO CITY NAV DEMO               ")
    print("=======================================\n")

    print("--- 1. METRO CITY GRAPH STRUCTURE ---")
    city_map = Graph(directed=False)
    station_names = ["Airport", "Beach", "Campus", "Downtown", "Eastside", "Factory", "Garden"]
    for station in station_names:
        city_map.add_vertex(station)

    route_pairs = [
        ("Airport", "Downtown"),
        ("Airport", "Eastside"),
        ("Beach", "Campus"),
        ("Beach", "Garden"),
        ("Campus", "Downtown"),
        ("Downtown", "Eastside"),
        ("Downtown", "Factory"),
        ("Eastside", "Factory"),
        ("Factory", "Garden"),
    ]
    for start, end in route_pairs:
        city_map.add_edge(start, end)

    print(str(city_map))
    print(f"Total Vertices: {city_map.vertex_count()}")
    print(f"Total Edges: {city_map.edge_count()}")
    print()

    print("--- 2. STATION DIRECTORY ---")
    tree = BST()
    setup_keys = ["Downtown", "Beach", "Factory", "Airport", "Campus", "Eastside", "Garden"]
    for key in setup_keys:
        tree.insert(key, f"Zone Info for {key}")

    print("Inorder (Alphabetical):", tree.inorder())
    print("Level Order:", tree.level_order())
    print("Preorder:", tree.preorder())
    print("Height:", tree.height())
    print("Leaf Count:", tree.count_leaves())
    print()

    print("--- 3. FARE-ZONE LOOKUP ---")
    fare_table = HashTable()
    zone_mapping = {
        "Airport": 1,
        "Beach": 3,
        "Campus": 2,
        "Downtown": 1,
        "Eastside": 2,
        "Factory": 2,
        "Garden": 3,
    }
    for stop, zone in zone_mapping.items():
        fare_table.put(stop, zone)

    for stop in station_names:
        print(f"Station: {stop:<10} | Fare Zone: {fare_table.get(stop)}")
    print()

    print("--- 4. TRIP LOG ---")
    log = LinkedList()
    stops_visited = ["Airport", "Downtown", "Campus", "Beach"]
    for stop in stops_visited:
        log.append(stop)

    print("Forward Trip Log:", str(log))
    log.reverse()
    print("Reversed Trip Log:", str(log))
    print()

    print("--- 5. MAINTENANCE TASKS ---")
    print("(Note: Numbers are task priorities, NOT graph connection weights)")
    work_orders = MinHeap()
    work_orders.push(3, "Inspect Beach-Campus sign")
    work_orders.push(1, "Repair Eastside crossing")
    work_orders.push(2, "Replace Downtown display")

    pending_tasks = work_orders.drain()
    for priority, task in pending_tasks:
        print(f"Priority {priority}: {task}")
    print()

    print("--- 6. RIDER BACK BUTTON ---")
    history = Stack()
    for stop in ["Airport", "Downtown", "Campus", "Beach"]:
        history.push(stop)

    print("Popped (Most Recent):", history.pop())
    print("Popped (Next Most Recent):", history.pop())
    print("Peek Top:", history.peek())
    print("Remaining Stack List:", history.to_list())
    print()

    print("--- 7. TICKET SERVICE LINE ---")
    line = Queue()
    for person in ["Ana", "Ben", "Cy"]:
        line.enqueue(person)

    print("Served First:", line.dequeue())
    print("Next in Line (Peek):", line.peek())
    print("Remaining Queue Size:", len(line))
    print("Remaining Queue List:", line.to_list())
    print()

    print("--- 8. COMMON STOPS:: ---")
    airport_stops = HashSet()
    factory_stops = HashSet()
    beach_stops = HashSet()

    for nbr in city_map.neighbors("Airport"):
        airport_stops.add(nbr)
    for nbr in city_map.neighbors("Factory"):
        factory_stops.add(nbr)
    for nbr in city_map.neighbors("Beach"):
        beach_stops.add(nbr)

    airport_factory_overlap = airport_stops.intersection(factory_stops)
    airport_beach_combined = airport_stops.union(beach_stops)
    airport_beach_overlap = airport_stops.intersection(beach_stops)

    print("Airport and Factory Shared Neighbors (Intersection):", sorted(airport_factory_overlap.to_list()))
    print("Airport and Beach Combined Neighbors (Union):", sorted(airport_beach_combined.to_list()))
    print("Airport and Beach Shared Neighbors (Intersection):", airport_beach_overlap.to_list())
    print()

    print("--- 9. FIFO vs LIFO ON DOWNTOWN NEIGHBORS ---")
    downtown_stops = city_map.neighbors("Downtown")
    print("Downtown Neighbors:", downtown_stops)

    fifo = Queue()
    lifo = Stack()
    for stop in downtown_stops:
        fifo.enqueue(stop)
        lifo.push(stop)

    fifo_out = [fifo.dequeue() for _ in range(len(fifo))]
    lifo_out = [lifo.pop() for _ in range(len(lifo))]

    print("Queue Drained (FIFO):", fifo_out)
    print("Stack Drained (LIFO):", lifo_out)
    print()

    print("--- 10. APPLICATION HELPER DEMONSTRATIONS ---")
    check_a = "([{}])"
    check_b = "([)]"
    print(f"is_balanced('{check_a}'): {is_balanced(check_a)}")
    print(f"is_balanced('{check_b}'): {is_balanced(check_b)}")

    riders = ["Ava", "Ben", "Cy", "Dee"]
    boarded_a, waiting_a = board_passengers(riders, 2)
    boarded_b, waiting_b = board_passengers(riders, 5)

    print(f"board_passengers({riders}, 2) -> Boarded: {boarded_a}, Waiting: {waiting_a}")
    print(f"board_passengers({riders}, 5) -> Boarded: {boarded_b}, Waiting: {waiting_b}")
    print()


if __name__ == "__main__":
    main()