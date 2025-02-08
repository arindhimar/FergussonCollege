import java.util.*;

interface RiverBank {
    void moveAManToBoat();
    void moveTwoMenToBoat();
    void moveAManAndACannibalToBoat();
    void moveACannibalToBoat();
    void moveTwoCannibalsToBoat();
}

class State {
    int leftMissionaries;
    int leftCannibals;
    int rightMissionaries;
    int rightCannibals;
    boolean isBoatOnLeft;
    String actions;

    State(int lm, int lc, int rm, int rc, boolean boat, String actions) {
        this.leftMissionaries = lm;
        this.leftCannibals = lc;
        this.rightMissionaries = rm;
        this.rightCannibals = rc;
        this.isBoatOnLeft = boat;
        this.actions = actions;
    }

    boolean isValid() {
        return (leftMissionaries >= leftCannibals || leftMissionaries == 0) &&
               (rightMissionaries >= rightCannibals || rightMissionaries == 0) &&
               leftMissionaries >= 0 && leftCannibals >= 0 &&
               rightMissionaries >= 0 && rightCannibals >= 0;
    }

    boolean isGoal() {
        return leftMissionaries == 0 && leftCannibals == 0 &&
               rightMissionaries == 3 && rightCannibals == 3;
    }

    @Override
    public String toString() {
        return "Left Bank: " + leftMissionaries + "M, " + leftCannibals + "C | " +
               "Right Bank: " + rightMissionaries + "M, " + rightCannibals + "C | " +
               "Boat on " + (isBoatOnLeft ? "Left" : "Right") + " Bank";
    }
}

class MissionariesAndCannibalsGame {
    private int leftMissionaries = 3;
    private int leftCannibals = 3;
    private int rightMissionaries = 0;
    private int rightCannibals = 0;
    private boolean isBoatOnLeft = true;

    private void moveBoat() {
        isBoatOnLeft = !isBoatOnLeft;
        System.out.println("The boat has moved to the " + (isBoatOnLeft ? "left" : "right") + " bank.");
    }

    private void printState() {
        System.out.println("\nCurrent State:");
        System.out.println("Left Bank: Missionaries=" + leftMissionaries + ", Cannibals=" + leftCannibals);
        System.out.println("Right Bank: Missionaries=" + rightMissionaries + ", Cannibals=" + rightCannibals);
        System.out.println("Boat is on the " + (isBoatOnLeft ? "left" : "right") + " bank.");
    }

    private void move(int missionaries, int cannibals) {
        if (isBoatOnLeft) {
            if (leftMissionaries >= missionaries && leftCannibals >= cannibals) {
                leftMissionaries -= missionaries;
                leftCannibals -= cannibals;
                rightMissionaries += missionaries;
                rightCannibals += cannibals;
                moveBoat();
            } else {
                System.out.println("Invalid move. Not enough missionaries or cannibals on the left bank.");
            }
        } else {
            if (rightMissionaries >= missionaries && rightCannibals >= cannibals) {
                rightMissionaries -= missionaries;
                rightCannibals -= cannibals;
                leftMissionaries += missionaries;
                leftCannibals += cannibals;
                moveBoat();
            } else {
                System.out.println("Invalid move. Not enough missionaries or cannibals on the right bank.");
            }
        }
    }

    private boolean isSolved() {
        return leftMissionaries == 0 && leftCannibals == 0 &&
               rightMissionaries == 3 && rightCannibals == 3;
    }

    public void startGame() {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            printState();
            if (isSolved()) {
                System.out.println("\nCongratulations! You successfully solved the problem!");
                break;
            }

            System.out.println("\nMenu:");
            System.out.println("1. Move 1 missionary to the boat.");
            System.out.println("2. Move 2 missionaries to the boat.");
            System.out.println("3. Move 1 cannibal to the boat.");
            System.out.println("4. Move 2 cannibals to the boat.");
            System.out.println("5. Move 1 missionary and 1 cannibal to the boat.");
            System.out.println("6. Solve using BFS (step-by-step).");
            System.out.println("7. Exit.");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            switch (choice) {
                case 1 -> move(1, 0);
                case 2 -> move(2, 0);
                case 3 -> move(0, 1);
                case 4 -> move(0, 2);
                case 5 -> move(1, 1);
                case 6 -> solveUsingBFS();
                case 7 -> {
                    System.out.println("Exiting...");
                    return;
                }
                default -> System.out.println("Invalid choice. Try again.");
            }
        }
    }

    private void solveUsingBFS() {
        System.out.println("\nSolving using BFS (step-by-step)...");
        Queue<State> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        State initialState = new State(3, 3, 0, 0, true, "Start");
        queue.offer(initialState);
        visited.add(serialize(initialState));

        while (!queue.isEmpty()) {
            State current = queue.poll();

            // Display the current step
            System.out.println(current);

            if (current.isGoal()) {
                System.out.println("\nSolution found!");
                return;
            }

            List<State> nextStates = generateNextStates(current);
            for (State next : nextStates) {
                if (!visited.contains(serialize(next)) && next.isValid()) {
                    visited.add(serialize(next));
                    queue.offer(next);
                }
            }
        }

        System.out.println("No solution found.");
    }

    private List<State> generateNextStates(State current) {
        List<State> states = new ArrayList<>();
        if (current.isBoatOnLeft) {
            addValidState(states, current, -1, 0, "Move 1 missionary");
            addValidState(states, current, -2, 0, "Move 2 missionaries");
            addValidState(states, current, 0, -1, "Move 1 cannibal");
            addValidState(states, current, 0, -2, "Move 2 cannibals");
            addValidState(states, current, -1, -1, "Move 1 missionary and 1 cannibal");
        } else {
            addValidState(states, current, 1, 0, "Return 1 missionary");
            addValidState(states, current, 2, 0, "Return 2 missionaries");
            addValidState(states, current, 0, 1, "Return 1 cannibal");
            addValidState(states, current, 0, 2, "Return 2 cannibals");
            addValidState(states, current, 1, 1, "Return 1 missionary and 1 cannibal");
        }
        return states;
    }

    private void addValidState(List<State> states, State current, int dM, int dC, String action) {
        State next = new State(
            current.leftMissionaries + dM,
            current.leftCannibals + dC,
            current.rightMissionaries - dM,
            current.rightCannibals - dC,
            !current.isBoatOnLeft,
            current.actions + " -> " + action
        );

        if (next.isValid()) states.add(next);
    }

    private String serialize(State state) {
        return state.leftMissionaries + "," + state.leftCannibals + "," +
               state.rightMissionaries + "," + state.rightCannibals + "," +
               state.isBoatOnLeft;
    }
}

public class MissionariesAndCannibals {
    public static void main(String[] args) {
        MissionariesAndCannibalsGame game = new MissionariesAndCannibalsGame();
        game.startGame();
    }
}
