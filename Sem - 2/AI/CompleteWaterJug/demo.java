import java.util.*;

interface JUG {
    void transferToGround();
    int transferToAnother(int otherRemCap);
}

class Jug1 implements JUG {
    int maxCap;
    int currCap;

    Jug1() {
        this.maxCap = 5;
        this.currCap = 0;
    }

    @Override
    public void transferToGround() {
        currCap = 0;
    }

    @Override
    public int transferToAnother(int otherRemCap) {
        if (currCap > 0 && otherRemCap < 4) {
            int transferAmount = Math.min(currCap, 4 - otherRemCap);
            currCap -= transferAmount;
            return transferAmount;
        }
        return 0;
    }

    public int getCurrCap() {
        return currCap;
    }

    public int getMaxCap() {
        return maxCap;
    }
}

class Jug2 implements JUG {
    int maxCap = 4;
    int currCap = 0;

    Jug2() {
        this.maxCap = 4;
        this.currCap = 0;
    }

    @Override
    public void transferToGround() {
        currCap = 0;
    }

    @Override
    public int transferToAnother(int otherRemCap) {
        if (currCap > 0 && otherRemCap < 5) {
            int transferAmount = Math.min(currCap, 5 - otherRemCap);
            currCap -= transferAmount;
            return transferAmount;
        }
        return 0;
    }

    public int getCurrCap() {
        return currCap;
    }

    public int getMaxCap() {
        return maxCap;
    }
}

class State {
    int jug1Cap;
    int jug2Cap;
    String actions;
    int heuristic;  // Heuristic to guide Best First Search

    State(int jug1Cap, int jug2Cap, String actions, int heuristic) {
        this.jug1Cap = jug1Cap;
        this.jug2Cap = jug2Cap;
        this.actions = actions;
        this.heuristic = heuristic;
    }
}

public class demo {
    private static Jug1 jug1 = new Jug1();
    private static Jug2 jug2 = new Jug2();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Water Jug Game!");
        printStatus();

        while (true) {
            System.out.println("\nSelect an operation:");
            System.out.println("1. Fill Jug1");
            System.out.println("2. Fill Jug2");
            System.out.println("3. Transfer from Jug1 to Jug2");
            System.out.println("4. Transfer from Jug2 to Jug1");
            System.out.println("5. Empty Jug1");
            System.out.println("6. Empty Jug2");
            System.out.println("7. Check Capacities");
            System.out.println("8. Solve using BFS");
            System.out.println("9. Solve using Best First Search");
            System.out.println("10. Exit");

            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    fillJug1();
                    break;
                case 2:
                    fillJug2();
                    break;
                case 3:
                    transferJug1ToJug2();
                    break;
                case 4:
                    transferJug2ToJug1();
                    break;
                case 5:
                    emptyJug1();
                    break;
                case 6:
                    emptyJug2();
                    break;
                case 7:
                    printStatus();
                    break;
                case 8:
                    solveUsingBFS();
                    break;
                case 9:
                    solveUsingBestFirstSearch();
                    break;
                case 10:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice! Try again.");
                    break;
            }

            if (jug1.getCurrCap() == 2) {
                System.out.println("Congratulations! You have successfully reached 2 units in Jug 1.");
                break;
            }
        }
    }

    private static void fillJug1() {
        if (jug1.getCurrCap() < jug1.getMaxCap()) {
            jug1.currCap = jug1.getMaxCap();
            System.out.println("Jug 1 is now full.");
        } else {
            System.out.println("Jug 1 is already full.");
        }
    }

    private static void fillJug2() {
        if (jug2.getCurrCap() < jug2.getMaxCap()) {
            jug2.currCap = jug2.getMaxCap();
            System.out.println("Jug 2 is now full.");
        } else {
            System.out.println("Jug 2 is already full.");
        }
    }

    private static void transferJug1ToJug2() {
        int transferred = jug1.transferToAnother(jug2.getCurrCap());
        jug2.currCap += transferred;
        System.out.println("Transferred " + transferred + " units from Jug 1 to Jug 2.");
    }

    private static void transferJug2ToJug1() {
        int transferred = jug2.transferToAnother(jug1.getCurrCap());
        jug1.currCap += transferred;
        System.out.println("Transferred " + transferred + " units from Jug 2 to Jug 1.");
    }

    private static void emptyJug1() {
        jug1.transferToGround();
        System.out.println("Jug 1 is now empty.");
    }

    private static void emptyJug2() {
        jug2.transferToGround();
        System.out.println("Jug 2 is now empty.");
    }

    private static void printStatus() {
        System.out.println("\nCurrent Status:");
        System.out.println("Jug 1: " + jug1.getCurrCap() + "/" + jug1.getMaxCap());
        System.out.println("Jug 2: " + jug2.getCurrCap() + "/" + jug2.getMaxCap());
    }

    // BFS (Breadth-First Search)
    private static void solveUsingBFS() {
        Queue<State> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.offer(new State(0, 0, "", 0));
        visited.add("0,0");

        while (!queue.isEmpty()) {
            State current = queue.poll();

            // Display the current state and actions taken to reach it
            System.out.println("Processing state: Jug1=" + current.jug1Cap + ", Jug2=" + current.jug2Cap);
            System.out.println("Actions so far: " + current.actions);

            // Check if the solution is reached
            if (current.jug1Cap == 2) {
                System.out.println("Solution found: " + current.actions);
                printStatus();
                return;
            }

            // Generate all possible next states
            List<State> nextStates = generateNextStates(current);

            for (State next : nextStates) {
                String stateKey = next.jug1Cap + "," + next.jug2Cap;
                if (!visited.contains(stateKey)) {
                    visited.add(stateKey);
                    queue.offer(next);
                }
            }
        }

        System.out.println("No solution found.");
    }

    // Best First Search (Greedy)
    private static void solveUsingBestFirstSearch() {
        PriorityQueue<State> pq = new PriorityQueue<>(Comparator.comparingInt(s -> s.heuristic));
        Set<String> visited = new HashSet<>();

        pq.offer(new State(0, 0, "", calculateHeuristic(0, 0)));
        visited.add("0,0");

        while (!pq.isEmpty()) {
            State current = pq.poll();

            // Display the current state and actions taken to reach it
            System.out.println("Processing state: Jug1=" + current.jug1Cap + ", Jug2=" + current.jug2Cap);
            System.out.println("Actions so far: " + current.actions);

            // Check if the solution is reached
            if (current.jug1Cap == 2) {
                System.out.println("Solution found: " + current.actions);
                printStatus();
                return;
            }

            // Generate all possible next states
            List<State> nextStates = generateNextStates(current);

            for (State next : nextStates) {
                String stateKey = next.jug1Cap + "," + next.jug2Cap;
                if (!visited.contains(stateKey)) {
                    visited.add(stateKey);
                    pq.offer(new State(next.jug1Cap, next.jug2Cap, next.actions, calculateHeuristic(next.jug1Cap, next.jug2Cap)));
                }
            }
        }

        System.out.println("No solution found.");
    }

    private static int calculateHeuristic(int jug1Cap, int jug2Cap) {
        // Heuristic: we want to minimize the difference between jug1 and the target value (2 units)
        return Math.abs(jug1Cap - 2);
    }

    private static List<State> generateNextStates(State currentState) {
        List<State> nextStates = new ArrayList<>();

        // Fill Jug1
        if (currentState.jug1Cap < jug1.getMaxCap()) {
            nextStates.add(new State(jug1.getMaxCap(), currentState.jug2Cap, currentState.actions + "Fill Jug1 ", 0));
        }

        // Fill Jug2
        if (currentState.jug2Cap < jug2.getMaxCap()) {
            nextStates.add(new State(currentState.jug1Cap, jug2.getMaxCap(), currentState.actions + "Fill Jug2 ", 0));
        }

        // Empty Jug1
        if (currentState.jug1Cap > 0) {
            nextStates.add(new State(0, currentState.jug2Cap, currentState.actions + "Empty Jug1 ", 0));
        }

        // Empty Jug2
        if (currentState.jug2Cap > 0) { 
            nextStates.add(new State(currentState.jug1Cap, 0, currentState.actions + "Empty Jug2 ", 0));
        }

        // Transfer from Jug1 to Jug2
        if (currentState.jug1Cap > 0 && currentState.jug2Cap < jug2.getMaxCap()) {
            int transferAmount = Math.min(currentState.jug1Cap, jug2.getMaxCap() - currentState.jug2Cap);
            nextStates.add(new State(currentState.jug1Cap - transferAmount, currentState.jug2Cap + transferAmount, currentState.actions + "Transfer Jug1 to Jug2 ", 0));
        }

        // Transfer from Jug2 to Jug1
        if (currentState.jug2Cap > 0 && currentState.jug1Cap < jug1.getMaxCap()) {
            int transferAmount = Math.min(currentState.jug2Cap, jug1.getMaxCap() - currentState.jug1Cap);
            nextStates.add(new State(currentState.jug1Cap + transferAmount, currentState.jug2Cap - transferAmount, currentState.actions + "Transfer Jug2 to Jug1 ", 0));
        }

        return nextStates;
    }
}
