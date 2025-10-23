// JavaScript Document

//Virtualization//

//Click a graph and descriptive text appears//

var togglers = document.getElementsByClassName("ToggleArea");

for (var i = 0; i < togglers.length; i++) {
	togglers[i].addEventListener("click", function() {
		var p = document.getElementById(this.dataset.target);
		var html = this.dataset.text;
		p.innerHTML = (p.innerHTML === "" ? html : "");
});
}


//Filter option interactives//

var ChartTypeSel = document.getElementById("ChartTypeSelect");
var PieDetailsSel = document.getElementById("PieDetailsSelect");
var DataAnalysisSel = document.getElementById("DataAnalysisSelect");

var charts = [
	"TimeSpentSNS",
	"MentalHealth",
	"SNSExercise",
	"Cyberbullying",
	"SNSAddiction",
	"SNSEscape"
];

//Image swapper for Pie Details and Chart Type//

function UpdateChartImages() {
	for (var i = 0; i < charts.length; i++) {
		var id = charts[i];
		var img = document.getElementById(id);
		
		if (ChartTypeSel.value === "Pie Graph") {
			if (PieDetailsSel.value === "Clear") {
				img.src = id + ".png";
			}
			else if (PieDetailsSel.value === "Percentages") {
				img.src = id + "Percent.png";
			}
			else {
				img.src = id + "Number.png";
			}
		}
		else if (ChartTypeSel.value === "Clustered Column") {
			img.src = id + "Column.png";
		}
		else {
			img.src = id + "Radar.png";
		}
	}
}

ChartTypeSel.addEventListener("change", UpdateChartImages);
PieDetailsSel.addEventListener("change", UpdateChartImages);

//Data Analysis section//

var AnalysisText = {
	TimeSpentSNS: "1. Students report spending a surprisingly large slice of their waking hours on social media. While roughly 13% say “under one hour,” nearly two-thirds fall into the 1–3 hour range, and over 20% actually clock 4 hours or more per day. That sustained engagement shows that platforms aren’t just a quick check-in, they’ve become central to students’ routines. When so much of their free time is devoted to scrolling, it inevitably crowds out study, sleep, face-to-face connection, and physical activity, setting the stage for both mental and physical health effects we see in the subsequent charts.",
	MentalHealth: "2. More than half of students acknowledge that social media use has at least “somewhat” affected their mental health, about 39% say “somewhat” and 14% say “a lot.” Although around 41% report “not at all,” the combined majority feeling any impact underscores that digital life carries an emotional cost for most. These self-assessments reflect everything from heightened anxiety over likes and comments to disrupted sleep and mood swings. Understanding this self-reported mental health footprint is critical for framing why we need targeted wellness tools and mindful usage strategies.",
	SNSExercise: "3. A significant portion of students admit that social media sometimes or even always interferes with their exercise routines, roughly 40% say “sometimes” and nearly 7% “always.” Only about half claim their workouts remain unaffected. That displacement of physical activity illustrates how screen time can reinforce a sedentary lifestyle, increasing risks of fatigue, poor posture, and longer‐term health issues. These findings highlight the importance of carving out dedicated, device-free time to keep bodies, and minds, strong.",
	Cyberbullying: "4. While 75% of respondents say they haven’t suffered lasting effects from cyberbullying, nearly 18% report feeling anxious as a direct result, with smaller shares experiencing depression or physical health problems. Even if it’s a minority, those who do feel anxious or depressed can face serious disruptions to concentration, self-esteem, and overall well-being. This chart lays bare the darker side of online interaction and underscores why robust anti-bullying policies and mental health supports are non-negotiable on campuses.",
	SNSAddiction: "5. A clear majority, around 60%, label their own use as “a lot” addictive, with another 35% calling it “somewhat” addictive. This widespread acknowledgment of compulsive checking and endless scrolling points to design choices in apps that foster habitual use. When students recognize that they’re “hooked,” it sets the groundwork for solutions like scheduled breaks, app-limit tools, or digital detox programs. Accepting addiction as real is the first step toward reclaiming control of one’s time and attention.",
	SNSEscape: "6. The vast majority of students turn to social media to escape daily stress, almost half do so “a lot,” and another half “somewhat.” Very few (around 5%) never use it as a coping mechanism. This heavy reliance on screens to avoid problems can stunt emotional resilience and prevent healthy, face-to-face support networks from developing. By spotlighting this escapism, we can advocate for teaching alternative coping strategies, mindfulness, community engagement, or physical activity, that build genuine, lasting well-being."
};

function UpdateAnalysisText() {
	var show = (DataAnalysisSel.value === "On");
	for (var i = 0; i < charts.length; i++) {
		var pid = charts[i] + "Analysis";
		var p = document.getElementById(pid);
		p.textContent = show ? AnalysisText[charts[i]] : "";
	}
}

DataAnalysisSel.addEventListener("change", UpdateAnalysisText);

UpdateChartImages();
UpdateAnalysisText();













