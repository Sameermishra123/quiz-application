const quizData = {
  os: {
    easy: [
      {
        question: "Which of the following is not an OS?",
        options: ["Linux", "Windows", "Oracle", "MacOS"],
        answer: 2
      },
      {
        question: "What does OS stand for?",
        options: ["Operating System", "Output System", "Order System", "Option System"],
        answer: 0
      },
      {
        question: "Which OS is developed by Microsoft?",
        options: ["Linux", "Windows", "MacOS", "Unix"],
        answer: 1
      },
      {
        question: "What is the main function of an operating system?",
        options: ["Run applications", "Manage hardware resources", "Create files", "Browse internet"],
        answer: 1
      },
      {
        question: "Which scheduling algorithm is used in real-time systems?",
        options: ["FCFS", "Round Robin", "Priority Scheduling", "Shortest Job First"],
        answer: 2
      }
    ],
    medium: [
      {
        question: "What is a kernel in operating systems?",
        options: ["A shell", "Core component that manages system resources", "A file system", "A user interface"],
        answer: 1
      },
      {
        question: "What is virtual memory?",
        options: ["Physical RAM", "Memory management technique", "Hard disk", "Cache memory"],
        answer: 1
      },
      {
        question: "Which process state transition occurs when a process is waiting for I/O?",
        options: ["Ready to Running", "Running to Blocked", "Blocked to Ready", "Running to Ready"],
        answer: 1
      },
      {
        question: "What is deadlock?",
        options: ["Process termination", "Resource allocation issue", "System crash", "Memory leak"],
        answer: 1
      },
      {
        question: "What is the purpose of page replacement algorithms?",
        options: ["Manage CPU", "Manage memory pages", "Manage I/O", "Manage processes"],
        answer: 1
      }
    ],
    hard: [
      {
        question: "Which page replacement algorithm suffers from Belady's anomaly?",
        options: ["FIFO", "LRU", "Optimal", "LFU"],
        answer: 0
      },
      {
        question: "What is the difference between preemptive and non-preemptive scheduling?",
        options: ["No difference", "Preemptive allows CPU to be taken away", "Non-preemptive is faster", "Preemptive is simpler"],
        answer: 1
      },
      {
        question: "In which memory management technique is the entire process loaded into memory?",
        options: ["Paging", "Segmentation", "Contiguous allocation", "Virtual memory"],
        answer: 2
      },
      {
        question: "What is the purpose of semaphores in process synchronization?",
        options: ["Memory management", "Process communication", "Deadlock prevention", "I/O management"],
        answer: 1
      },
      {
        question: "Which algorithm is used to prevent deadlock?",
        options: ["Banker's Algorithm", "Round Robin", "FCFS", "SJF"],
        answer: 0
      }
    ]
  },
  dsa: {
    easy: [
      {
        question: "Which data structure uses FIFO?",
        options: ["Stack", "Queue", "Tree", "Graph"],
        answer: 1
      },
      {
        question: "Which data structure uses LIFO?",
        options: ["Queue", "Stack", "Array", "Linked List"],
        answer: 1
      },
      {
        question: "What is the time complexity of accessing an element in an array?",
        options: ["O(n)", "O(log n)", "O(1)", "O(n²)"],
        answer: 2
      },
      {
        question: "Which sorting algorithm has the best average time complexity?",
        options: ["Bubble Sort", "Selection Sort", "Quick Sort", "Insertion Sort"],
        answer: 2
      },
      {
        question: "What is a binary tree?",
        options: ["Tree with 2 nodes", "Tree where each node has at most 2 children", "Tree with 2 levels", "Tree with 2 leaves"],
        answer: 1
      }
    ],
    medium: [
      {
        question: "What is the time complexity of binary search?",
        options: ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
        answer: 1
      },
      {
        question: "Which traversal visits root, left, right?",
        options: ["Inorder", "Preorder", "Postorder", "Level order"],
        answer: 1
      },
      {
        question: "What is the worst-case time complexity of quicksort?",
        options: ["O(n log n)", "O(n²)", "O(n)", "O(log n)"],
        answer: 1
      },
      {
        question: "Which data structure is used for implementing recursion?",
        options: ["Queue", "Stack", "Array", "Tree"],
        answer: 1
      },
      {
        question: "What is a hash table?",
        options: ["Sorted array", "Key-value data structure", "Tree structure", "Linked list"],
        answer: 1
      }
    ],
    hard: [
      {
        question: "What is the time complexity of finding the maximum element in a heap?",
        options: ["O(n)", "O(log n)", "O(1)", "O(n log n)"],
        answer: 2
      },
      {
        question: "Which algorithm is used to find shortest path in a weighted graph?",
        options: ["BFS", "DFS", "Dijkstra's", "Kruskal's"],
        answer: 2
      },
      {
        question: "What is the space complexity of merge sort?",
        options: ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
        answer: 1
      },
      {
        question: "Which data structure is best for implementing a priority queue?",
        options: ["Array", "Linked List", "Heap", "Stack"],
        answer: 2
      },
      {
        question: "What is the time complexity of inserting in a balanced BST?",
        options: ["O(n)", "O(log n)", "O(1)", "O(n²)"],
        answer: 1
      }
    ]
  },
  networks: {
    easy: [
      {
        question: "What does HTTP stand for?",
        options: ["HyperText Transfer Protocol", "High Transfer Text Protocol", "Hyper Transfer Text Protocol", "High Text Transfer Protocol"],
        answer: 0
      },
      {
        question: "Which layer of OSI model handles routing?",
        options: ["Physical", "Data Link", "Network", "Transport"],
        answer: 2
      },
      {
        question: "What is the default port for HTTP?",
        options: ["80", "443", "21", "25"],
        answer: 0
      },
      {
        question: "Which protocol is used for email?",
        options: ["HTTP", "FTP", "SMTP", "TCP"],
        answer: 2
      },
      {
        question: "What does IP stand for?",
        options: ["Internet Protocol", "Internal Protocol", "Internet Program", "Internal Program"],
        answer: 0
      }
    ],
    medium: [
      {
        question: "What is the difference between TCP and UDP?",
        options: ["TCP is faster", "TCP is connection-oriented, UDP is connectionless", "UDP is more reliable", "No difference"],
        answer: 1
      },
      {
        question: "Which protocol is used for secure web communication?",
        options: ["HTTP", "HTTPS", "FTP", "SMTP"],
        answer: 1
      },
      {
        question: "What is a subnet mask used for?",
        options: ["Identify network portion of IP", "Encrypt data", "Route packets", "Establish connection"],
        answer: 0
      },
      {
        question: "Which device operates at the network layer?",
        options: ["Hub", "Switch", "Router", "Bridge"],
        answer: 2
      },
      {
        question: "What is DNS used for?",
        options: ["File transfer", "Domain name resolution", "Email", "Web browsing"],
        answer: 1
      }
    ],
    hard: [
      {
        question: "What is the purpose of ARP?",
        options: ["Route packets", "Resolve IP to MAC address", "Encrypt data", "Establish connection"],
        answer: 1
      },
      {
        question: "Which routing algorithm uses distance vectors?",
        options: ["OSPF", "RIP", "BGP", "EIGRP"],
        answer: 1
      },
      {
        question: "What is the maximum number of hosts in a /24 network?",
        options: ["254", "255", "256", "128"],
        answer: 0
      },
      {
        question: "Which protocol is used for dynamic IP assignment?",
        options: ["DNS", "DHCP", "ARP", "ICMP"],
        answer: 1
      },
      {
        question: "What is the purpose of NAT?",
        options: ["Encrypt traffic", "Translate private to public IP", "Route packets", "Resolve names"],
        answer: 1
      }
    ]
  },
  dbms: {
    easy: [
      {
        question: "What does DBMS stand for?",
        options: ["Database Management System", "Data Base Management System", "Database Management Software", "Data Base Management Software"],
        answer: 0
      },
      {
        question: "Which is a type of database model?",
        options: ["Relational", "Linear", "Circular", "Vertical"],
        answer: 0
      },
      {
        question: "What is a primary key?",
        options: ["First column", "Unique identifier", "Foreign key", "Index"],
        answer: 1
      },
      {
        question: "Which SQL command is used to retrieve data?",
        options: ["INSERT", "UPDATE", "SELECT", "DELETE"],
        answer: 2
      },
      {
        question: "What is a table in a database?",
        options: ["Collection of rows and columns", "Single row", "Single column", "Index"],
        answer: 0
      }
    ],
    medium: [
      {
        question: "What is normalization?",
        options: ["Data encryption", "Organizing data to reduce redundancy", "Data backup", "Data compression"],
        answer: 1
      },
      {
        question: "What is a foreign key?",
        options: ["Primary key", "Reference to primary key in another table", "Unique key", "Index key"],
        answer: 1
      },
      {
        question: "Which normal form eliminates transitive dependency?",
        options: ["1NF", "2NF", "3NF", "BCNF"],
        answer: 2
      },
      {
        question: "What is ACID in database transactions?",
        options: ["Atomicity, Consistency, Isolation, Durability", "Access, Control, Integrity, Data", "Analysis, Control, Input, Data", "Atomic, Consistent, Input, Data"],
        answer: 0
      },
      {
        question: "Which join returns all rows from both tables?",
        options: ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"],
        answer: 3
      }
    ],
    hard: [
      {
        question: "What is the difference between DELETE and TRUNCATE?",
        options: ["No difference", "TRUNCATE is faster and cannot be rolled back", "DELETE is faster", "TRUNCATE can be rolled back"],
        answer: 1
      },
      {
        question: "What is a transaction?",
        options: ["Single query", "Sequence of operations as one unit", "Table", "Index"],
        answer: 1
      },
      {
        question: "Which isolation level prevents dirty reads?",
        options: ["READ UNCOMMITTED", "READ COMMITTED", "REPEATABLE READ", "SERIALIZABLE"],
        answer: 1
      },
      {
        question: "What is a view in database?",
        options: ["Physical table", "Virtual table based on query", "Index", "Constraint"],
        answer: 1
      },
      {
        question: "Which index structure is used in most databases?",
        options: ["Array", "Linked List", "B-tree", "Hash Table"],
        answer: 2
      }
    ]
  }
};

