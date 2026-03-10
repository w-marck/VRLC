









 flowchart
	style n1 fill:#000000,stroke-width:2px,stroke:#FFFFFF,color:#FFFFFF
	subgraph s1[" "]

		n5@{ shape: "circle", label: "1 🏁" }
		n4@{ shape: "circle", label: "2" }
		n3@{ shape: "circle", label: "3" }
		n2@{ shape: "circle", label: "4" }
		n1@{ shape: "circle", label: "5 🔧" }
	end
	n1
	n1 --- n2
	n2
	n2 --- n3
	n3
	n3 --- n4
	n4
	n4 --- n5
	style n2 fill:#FF5757,stroke-width:0px,color:#000000
	style n3 fill:#FFDE59,stroke-width:0px,color:#000000
	style n4 fill:#7ED957,stroke-width:0px,color:#000000
	style n5 fill:#FFFFFF,stroke:#000000,stroke-width:2px,color:#000000




