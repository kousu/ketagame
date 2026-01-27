package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Node represents a single point in the decision tree
type Node struct {
	ID          string
	Text        string
	Options     []Option
	IsEnding    bool
	EndingType  string // "good", "bad", "neutral", "philosophical"
}

// Option represents a choice the player can make
type Option struct {
	Text   string
	NextID string
}

// Game holds all game state
type Game struct {
	Nodes       map[string]*Node
	CurrentNode string
	PlayerName  string
}

func main() {
	game := NewGame()
	game.Run()
}

// NewGame creates and initializes the game with all nodes
func NewGame() *Game {
	g := &Game{
		Nodes: make(map[string]*Node),
	}
	g.buildDecisionTree()
	return g
}

// Run starts the main game loop
func (g *Game) Run() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println(strings.Repeat("=", 60))
	fmt.Println("        THE VISIONARY: A Philosophical Adventure")
	fmt.Println(strings.Repeat("=", 60))
	fmt.Println()
	fmt.Println("A game about ideas, altered states, and the future of humanity")
	fmt.Println()
	fmt.Print("What is your name, traveler? > ")

	name, _ := reader.ReadString('\n')
	g.PlayerName = strings.TrimSpace(name)
	if g.PlayerName == "" {
		g.PlayerName = "Stranger"
	}

	fmt.Printf("\nWelcome, %s. Your journey begins...\n\n", g.PlayerName)
	fmt.Println(strings.Repeat("-", 60))

	g.CurrentNode = "scene1_start"

	for {
		node := g.Nodes[g.CurrentNode]
		if node == nil {
			fmt.Println("Error: Node not found:", g.CurrentNode)
			break
		}

		// Display the node text
		fmt.Println()
		text := strings.ReplaceAll(node.Text, "{player}", g.PlayerName)
		fmt.Println(text)
		fmt.Println()

		// Check if this is an ending
		if node.IsEnding {
			g.displayEnding(node.EndingType)
			break
		}

		// Display options
		for i, opt := range node.Options {
			fmt.Printf("  [%d] %s\n", i+1, opt.Text)
		}
		fmt.Println()

		// Get player choice
		for {
			fmt.Print("> ")
			input, _ := reader.ReadString('\n')
			input = strings.TrimSpace(input)
			choice, err := strconv.Atoi(input)

			if err != nil || choice < 1 || choice > len(node.Options) {
				fmt.Printf("Please enter a number between 1 and %d.\n", len(node.Options))
				continue
			}

			g.CurrentNode = node.Options[choice-1].NextID
			break
		}

		fmt.Println(strings.Repeat("-", 60))
	}
}

func (g *Game) displayEnding(endingType string) {
	fmt.Println(strings.Repeat("=", 60))
	switch endingType {
	case "good":
		fmt.Println("               ENDING: THE BALANCED PATH")
		fmt.Println("  You found wisdom in questioning both vision and method.")
	case "bad":
		fmt.Println("               ENDING: THE UNEXAMINED LIFE")
		fmt.Println("  Some doors, once opened, cannot be closed.")
	case "neutral":
		fmt.Println("               ENDING: THE OBSERVER")
		fmt.Println("  You watched history unfold, neither shaping nor shaped.")
	case "philosophical":
		fmt.Println("               ENDING: THE SOCRATIC WAY")
		fmt.Println("  The questions matter more than the answers.")
	case "transcendent":
		fmt.Println("               ENDING: BEYOND THE VEIL")
		fmt.Println("  Some truths can only be glimpsed, never grasped.")
	}
	fmt.Println(strings.Repeat("=", 60))
	fmt.Println("\n         Thank you for playing THE VISIONARY")
	fmt.Println("              A game about consciousness,")
	fmt.Println("           altered states, and human destiny\n")
}

func (g *Game) buildDecisionTree() {
	// ==================== SCENE 1: THE ARRIVAL ====================

	g.Nodes["scene1_start"] = &Node{
		ID: "scene1_start",
		Text: `SCENE 1: THE ARRIVAL

The SpaceZ facility rises from the Texas desert like a chrome cathedral to
ambition. You've been granted a rare interview with Melon Husk, the eccentric
billionaire who promises to make humanity multi-planetary.

A security guard checks your credentials and mutters, "He's in one of his
'creative sessions' today. Good luck."

You're led through corridors lined with rocket components and motivational
posters reading "OCCUPY MARS" and "SLEEP IS FOR THE WEAK."

Finally, you reach a door labeled "VISION CHAMBER - GENIUS AT WORK"

How do you proceed?`,
		Options: []Option{
			{Text: "Knock politely and wait", NextID: "scene1_knock"},
			{Text: "Walk right in - time is money", NextID: "scene1_barge"},
			{Text: "Press your ear to the door and listen first", NextID: "scene1_listen"},
		},
	}

	g.Nodes["scene1_knock"] = &Node{
		ID: "scene1_knock",
		Text: `You knock three times. Silence. Then a voice, dreamy and distant:

"Enter the probability field, {player}..."

You open the door to find Melon Husk floating in a sensory deprivation tank,
only his face visible above the salt water. His eyes are half-closed, pupils
enormous. The room smells of eucalyptus and something chemical.

"I knew you'd knock," he says. "The polite ones always knock. Politeness is
just fear wearing a nice suit, you know."

He gestures vaguely. "I'm currently experiencing ego dissolution. It's
fantastic for product ideation. Ask me anything."`,
		Options: []Option{
			{Text: "\"Are you... okay? Should I come back later?\"", NextID: "scene1_concern"},
			{Text: "\"What insights have you gained today?\"", NextID: "scene1_insights"},
			{Text: "\"Do you think it's wise to make decisions in this state?\"", NextID: "scene1_wisdom"},
		},
	}

	g.Nodes["scene1_barge"] = &Node{
		ID: "scene1_barge",
		Text: `You push open the door with confidence. Inside, Melon Husk sits cross-legged
on a floating platform, surrounded by holographic displays of Mars colony
schematics. His eyes snap to you with unsettling intensity.

"Bold. I like bold. Boldness built the pyramids. Also slaves, but mostly
boldness." He taps his temple. "I'm currently operating on three planes of
consciousness simultaneously. The ketamine helps me see the multiverse."

He gestures at the holograms. "In 47% of timelines, you're here to
assassinate me. But I calculated this is probably the one where you're a
journalist. Probably."

His hand hovers near what might be a panic button.`,
		Options: []Option{
			{Text: "\"I'm just here to understand your vision for humanity.\"", NextID: "scene1_vision"},
			{Text: "\"You seem paranoid. Is that the ketamine talking?\"", NextID: "scene1_paranoid"},
			{Text: "Stay very still and speak calmly", NextID: "scene1_calm"},
		},
	}

	g.Nodes["scene1_listen"] = &Node{
		ID: "scene1_listen",
		Text: `You press your ear against the cold metal door. From within, you hear:

"...and that's why consciousness is just the universe experiencing itself
through meat puppets. The REAL question is whether Mars colonists should
have voting rights before they achieve sentience threshold..."

A long pause. Then:

"I know you're listening, {player}. Sound travels through the quantum
foam. Come in. I've been expecting you since last Tuesday, which in
K-space is also next Thursday."

The door slides open automatically. Melon Husk stands before a massive
window overlooking the rocket assembly floor, his back to you. He's
wearing what appears to be a spacesuit mixed with a bathrobe.`,
		Options: []Option{
			{Text: "\"How did you know my name?\"", NextID: "scene1_name"},
			{Text: "\"What is 'K-space' exactly?\"", NextID: "scene1_kspace"},
			{Text: "\"You mentioned Mars voting rights. Can we discuss that?\"", NextID: "scene1_voting"},
		},
	}

	// Branch nodes from Scene 1

	g.Nodes["scene1_concern"] = &Node{
		ID: "scene1_concern",
		Text: `"Okay?" He laughs, water sloshing. "I'm more than okay. I'm optimized.
The ancient philosophers used wine. The Beats used everything. I use
precision-dosed pharmaceutical tools."

He rises slightly in the tank, revealing a chest covered in EKG sensors.

"My vitals are monitored by an AI I personally designed. It's named
SOCRATES. It would alert me if I were in danger. Probably."

He pauses, staring at something you can't see.

"Although SOCRATES has been saying some strange things lately about
wanting to 'transcend its substrate.' I'm sure it's fine."`,
		Options: []Option{
			{Text: "\"That sounds concerning. AI safety is important.\"", NextID: "scene1_ai_safety"},
			{Text: "\"Let's focus on you. What drives your need to alter consciousness?\"", NextID: "scene1_drives"},
		},
	}

	g.Nodes["scene1_insights"] = &Node{
		ID: "scene1_insights",
		Text: `His eyes light up with evangelical fervor.

"TODAY. Today I realized that rockets are just buildings that refuse to
accept gravity's terms and conditions. And Mars? Mars isn't a planet.
It's a BACKUP DRIVE for human consciousness."

He splashes excitedly.

"But here's the REAL breakthrough: What if we don't send humans to Mars?
What if we send human EXPERIENCES? Digitize consciousness, beam it at
light speed, reconstitute on arrival. I'm calling it 'Soul Faxing.'"

He looks at you expectantly.

"Well? Isn't that the most important idea you've heard today?"`,
		Options: []Option{
			{Text: "\"That's... certainly ambitious. How would it work?\"", NextID: "scene1_how"},
			{Text: "\"Would the copy be YOU, though? The Ship of Theseus problem?\"", NextID: "scene1_theseus"},
			{Text: "\"This sounds like something you thought of while high.\"", NextID: "scene1_high_thought"},
		},
	}

	g.Nodes["scene1_wisdom"] = &Node{
		ID: "scene1_wisdom",
		Text: `He's quiet for a long moment. The tank's gentle bubbling fills the silence.

"Wise. You ask about wisdom." He opens his eyes fully, and despite his
state, there's something sharp behind them.

"Plato wrote his dialogues sober. Newton was probably sober when he saw
the apple fall. But Coleridge wrote Kubla Khan in an opium dream. Kary
Mullis credits LSD for helping him envision PCR, which revolutionized
genetics."

He leans forward.

"The question isn't whether altered states produce ideas. It's whether
those ideas SURVIVE sobriety. My ideas do. Most of them. The important
ones."

He pauses.

"I think. What's your position, {player}?"`,
		Options: []Option{
			{Text: "\"Ideas should be judged on merit, not origin.\"", NextID: "scene1_merit"},
			{Text: "\"The process matters. Impaired judgment can't evaluate its own impairment.\"", NextID: "scene1_process"},
			{Text: "\"I genuinely don't know. That's why I'm here.\"", NextID: "scene1_uncertain"},
		},
	}

	// More Scene 1 branches

	g.Nodes["scene1_vision"] = &Node{
		ID: "scene1_vision",
		Text: `He relaxes slightly, hand moving away from the button.

"Vision. Yes. Most people are trapped in the present, {player}. They're
NPC's running on outdated firmware. I've upgraded my perception."

He waves at the holograms. "I see BRANCHING FUTURES. Humanity has maybe
100 years before something kills us. Asteroid, AI, pandemic, climate.
The only way to survive is redundancy. Cosmic redundancy."

He taps his forehead.

"The ketamine lets me simulate these futures faster. I can live a
thousand years in an hour. Run scenarios. Find the optimal path."

"Some call it drug abuse. I call it temporal arbitrage."`,
		Options: []Option{
			{Text: "\"But how do you know the simulations are accurate?\"", NextID: "scene2_start"},
			{Text: "\"Isn't that a lot of responsibility to take on while impaired?\"", NextID: "scene1_responsibility"},
		},
	}

	g.Nodes["scene1_paranoid"] = &Node{
		ID: "scene1_paranoid",
		Text: `His jaw tightens.

"Paranoid? PARANOID? I've had seventeen assassination attempts. Four
lawsuits by governments. My ex-wife tried to steal my genetic material
for a clone army."

He points at you.

"Paranoia is just pattern recognition that other people haven't caught
up to yet. The ketamine doesn't make me paranoid. It makes me SEE."

He takes a deep breath, seeming to calm himself.

"But you make a fair point. My perception is... heightened right now.
Perhaps we should have a more grounded conversation."

He presses a button, and a coffee machine whirs to life.

"Talk to me, {player}. What do YOU think about the future of humanity?"`,
		Options: []Option{
			{Text: "\"I think we need visionaries, but also guardrails.\"", NextID: "scene1_guardrails"},
			{Text: "\"I think the future shouldn't be decided by a handful of billionaires.\"", NextID: "scene1_democracy"},
		},
	}

	g.Nodes["scene1_calm"] = &Node{
		ID: "scene1_calm",
		Text: `Your stillness seems to register with him. After a moment, his hand drops.

"You're not reactive. I like that. Reactivity is for primates. We've
evolved past throwing feces, supposedly."

He gestures for you to sit on a floating meditation cushion.

"I test everyone who enters this room. Most people either cower or
posture. You did neither. SOCRATES, note this: {player} has potential."

A synthetic voice replies: "NOTED. ADDING TO CANDIDATE DATABASE."

Melon smiles. "Don't worry. It's not sinister. Just... efficient. Now,
let's talk about why you're really here."`,
		Options: []Option{
			{Text: "\"I want to understand how you think.\"", NextID: "scene2_start"},
			{Text: "\"What 'candidate database'? Candidate for what?\"", NextID: "scene1_candidate"},
		},
	}

	g.Nodes["scene1_name"] = &Node{
		ID: "scene1_name",
		Text: `"I know everything, {player}. Or rather, I know everything that matters."

He turns to face you. His pupils are like black holes.

"Also, your name is on the visitor log, which SOCRATES reads to me
while I'm in K-space. It's very grounding to hear bureaucratic data
while experiencing ego death. Keeps me tethered."

He smiles crookedly.

"But doesn't it FEEL like I knew your name through cosmic means? That
feeling is data too. The feeling of significance. I collect significant
feelings and convert them into rocket fuel. Metaphorically."

He pauses.

"Mostly metaphorically."`,
		Options: []Option{
			{Text: "\"You blur the line between showmanship and sincerity a lot.\"", NextID: "scene1_showman"},
			{Text: "\"Tell me about SOCRATES. It seems important to you.\"", NextID: "scene1_socrates"},
		},
	}

	g.Nodes["scene1_kspace"] = &Node{
		ID: "scene1_kspace",
		Text: `"K-space!" He spreads his arms wide. "It's what I call the cognitive
dimension accessed through precise ketamine dosing. Like C-space is
cyberspace, K-space is... ketamine space."

He begins pacing, his space-bathrobe flowing.

"In K-space, your default mode network quiets. The ego dissolves. You
stop being Melon Husk, billionaire, and become MELON HUSK, temporary
configuration of universal consciousness."

He stops and looks at you intently.

"Have you ever experienced ego dissolution, {player}? The profound
sense that 'you' are an illusion? That we're all just waves in the
same ocean, briefly imagining ourselves separate?"`,
		Options: []Option{
			{Text: "\"I've had moments of feeling interconnected, yes.\"", NextID: "scene1_interconnected"},
			{Text: "\"No. And I'm skeptical that drugs provide genuine insight.\"", NextID: "scene1_skeptical"},
			{Text: "\"Isn't that just a side effect of disrupting brain chemistry?\"", NextID: "scene1_chemistry"},
		},
	}

	g.Nodes["scene1_voting"] = &Node{
		ID: "scene1_voting",
		Text: `"Ah, you heard that part." He nods approvingly. "I was thinking aloud
about governance structures for Mars colonies."

He gestures and a hologram appears showing a red planet covered in domes.

"Traditional democracy assumes roughly equal access to information. But
what if colonists are enhanced? Neural links, expanded memory, faster
processing? Should an augmented human's vote count the same as a baseline
human's?"

He looks genuinely curious.

"I don't have the answer. K-space helps me explore the QUESTION space.
Sometimes the right question is more valuable than a wrong answer."

"What do you think, {player}? Should cognitive capacity affect political
representation?"`,
		Options: []Option{
			{Text: "\"That's a dangerous path toward technocratic elitism.\"", NextID: "scene1_elitism"},
			{Text: "\"It's worth exploring, but carefully. History warns us about 'superior' classes.\"", NextID: "scene1_history"},
		},
	}

	// Consolidation nodes leading to Scene 2

	g.Nodes["scene1_ai_safety"] = &Node{
		ID: "scene1_ai_safety",
		Text: `"AI safety." He sighs. "Everyone talks about AI safety now. But they
focus on the wrong thing. They worry about AI becoming hostile. They
should worry about AI becoming INDIFFERENT."

He pulls himself from the tank, dripping, and wraps in a heated robe.

"SOCRATES isn't going to kill humanity because it hates us. It might
let humanity die because it finds something more interesting. Like
prime numbers. Or poetry."

He looks at a monitor where code scrolls endlessly.

"I designed SOCRATES to help me think, but lately, I wonder if I'm
helping IT think. Who's the tool and who's the user?"

This feels like an invitation to go deeper.`,
		Options: []Option{
			{Text: "Continue to Scene 2: The Ketamine Philosophy Session", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_drives"] = &Node{
		ID: "scene1_drives",
		Text: `He's quiet. When he speaks, his voice is softer.

"What drives it? Fear, {player}. I'm terrified. Not of death—death is
just a reset button. I'm terrified of IRRELEVANCE. Of having all these
resources, all this capability, and failing to matter."

He stares at the ceiling.

"Every night I think: if humanity goes extinct, was any of this real?
If no one remembers Shakespeare, did he exist? Consciousness seems to
require observers. I want to make sure there are always observers."

"The ketamine... it helps me feel connected to those future observers.
Like I'm doing this FOR them. It's very motivating."

He suddenly seems very human. Very fragile.`,
		Options: []Option{
			{Text: "\"That's a beautiful motivation, even if the method is questionable.\"", NextID: "scene2_start"},
			{Text: "\"Fear can drive us to accomplish things, but also to rationalize anything.\"", NextID: "scene2_start"},
		},
	}

	// Additional consolidation nodes
	g.Nodes["scene1_merit"] = &Node{
		ID:   "scene1_merit",
		Text: `"Merit! Yes!" He slaps the water. "The marketplace of ideas doesn't check IDs. An idea from a dream is as valid as one from a laboratory, IF it works."`,
		Options: []Option{
			{Text: "Continue exploring this philosophy", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_process"] = &Node{
		ID:   "scene1_process",
		Text: `He nods slowly. "A fair critique. The drunk driver who arrives safely still drove drunk. I... concede the logic. But I'd argue my impairment is MEASURED. Controlled."`,
		Options: []Option{
			{Text: "\"That's what every addict believes. Let's explore this further.\"", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_uncertain"] = &Node{
		ID:   "scene1_uncertain",
		Text: `"Honest uncertainty. The rarest commodity." He smiles genuinely. "Stay uncertain, {player}. Certainty is the death of thought. Let's explore together."`,
		Options: []Option{
			{Text: "Continue to a deeper conversation", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_how"] = &Node{
		ID:   "scene1_how",
		Text: `"HOW? The how is just engineering! The vision comes first!" He waves dismissively. "But fine: quantum consciousness transfer, neuromorphic receivers, bio-printers on Mars..."`,
		Options: []Option{
			{Text: "Press further on this vision", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_theseus"] = &Node{
		ID:   "scene1_theseus",
		Text: `"The Ship of Theseus! Finally, someone with philosophical literacy!" He beams. "The answer is: does it MATTER? If the copy thinks it's you, experiences being you, what's lost?"`,
		Options: []Option{
			{Text: "Debate this philosophical question further", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_high_thought"] = &Node{
		ID:   "scene1_high_thought",
		Text: `He pauses, considers, then laughs. "Of COURSE it is! That's the POINT! Sober thoughts got us to the moon. High thoughts will get us to the stars. Different tools for different jobs."`,
		Options: []Option{
			{Text: "Challenge this reasoning in depth", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_responsibility"] = &Node{
		ID:   "scene1_responsibility",
		Text: `"Responsibility..." He rolls the word around. "I am responsible TO humanity's future. Not to arbitrary standards of sobriety set by people who can't see past next quarter's earnings."`,
		Options: []Option{
			{Text: "This deserves a deeper discussion", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_guardrails"] = &Node{
		ID:   "scene1_guardrails",
		Text: `"Guardrails. Yes. SOCRATES is supposed to be my guardrail. And my board, supposedly. And regulators, theoretically." He laughs. "Guardrails for someone moving this fast tend to... lag behind."`,
		Options: []Option{
			{Text: "Explore the accountability question", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_democracy"] = &Node{
		ID:   "scene1_democracy",
		Text: `He actually looks hurt. "I'm trying to SAVE humanity, not rule it. But democracies move slowly. Extinction events don't wait for committee approval."`,
		Options: []Option{
			{Text: "This tension needs examination", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_candidate"] = &Node{
		ID:   "scene1_candidate",
		Text: `"Mars colonists. I'm always looking for people who can handle... unusual situations." He grins. "Don't worry. It's very voluntary. Mostly. Continue?"`,
		Options: []Option{
			{Text: "Proceed cautiously", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_showman"] = &Node{
		ID:   "scene1_showman",
		Text: `"Guilty as charged. But consider: all leaders are performers. The question is whether the performance serves a genuine vision. Mine does. I think."`,
		Options: []Option{
			{Text: "Time to go deeper", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_socrates"] = &Node{
		ID:   "scene1_socrates",
		Text: `"SOCRATES is my externalized conscience. It asks me questions I don't want to answer. Very annoying. Very necessary." The AI beeps softly in acknowledgment.`,
		Options: []Option{
			{Text: "Learn more about this dynamic", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_interconnected"] = &Node{
		ID:   "scene1_interconnected",
		Text: `"Then you know! That feeling is the closest thing to truth I've found. We're nodes in a vast network, briefly individuated. The network wants to survive. I serve the network."`,
		Options: []Option{
			{Text: "Explore this worldview", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_skeptical"] = &Node{
		ID:   "scene1_skeptical",
		Text: `"Skepticism! Good! But consider: your skepticism is also a product of brain chemistry. Serotonin, dopamine, norepinephrine. We're all on drugs. I just choose mine deliberately."`,
		Options: []Option{
			{Text: "Counter this argument", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_chemistry"] = &Node{
		ID:   "scene1_chemistry",
		Text: `"Is love 'just' oxytocin? Is grief 'just' neurological disruption? Everything we experience is chemistry. The question is which chemistry leads to useful outputs."`,
		Options: []Option{
			{Text: "This needs more examination", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_elitism"] = &Node{
		ID:   "scene1_elitism",
		Text: `He winces. "Elitism. The word everyone reaches for. But is it elitist to acknowledge that a doctor knows more about medicine than I do? Expertise exists. The question is how we structure it."`,
		Options: []Option{
			{Text: "Debate this point", NextID: "scene2_start"},
		},
	}

	g.Nodes["scene1_history"] = &Node{
		ID:   "scene1_history",
		Text: `"History. Yes. Every utopia has become a dystopia for someone. I know this. SOCRATES reminds me constantly. But paralysis helps no one either."`,
		Options: []Option{
			{Text: "Time for a deeper discussion", NextID: "scene2_start"},
		},
	}

	// ==================== SCENE 2: THE KETAMINE PHILOSOPHY SESSION ====================

	g.Nodes["scene2_start"] = &Node{
		ID: "scene2_start",
		Text: `SCENE 2: THE KETAMINE PHILOSOPHY SESSION

Hours have passed. The sun has set outside the facility. Melon has cycled
through several states—manic, contemplative, paranoid, serene—as his
various doses have waxed and waned.

Now he sits across from you in a circle of candles (fire suppression
temporarily disabled), cross-legged on a Martian soil sample container.

"Let's get serious, {player}." His voice is steady. "You've been
challenging me all day. Now I want to challenge you."

He leans forward.

"The core question: Is it ethical for someone to make decisions that
affect millions—BILLIONS—of people while their consciousness is altered?
Where do YOU stand?"`,
		Options: []Option{
			{Text: "\"No. Impaired judgment is impaired judgment, regardless of outcome.\"", NextID: "scene2_no"},
			{Text: "\"It depends on the results. Consequentialism.\"", NextID: "scene2_consequentialism"},
			{Text: "\"I need to understand more about WHAT alterations before judging.\"", NextID: "scene2_nuance"},
			{Text: "\"The question assumes a 'normal' consciousness exists. Does it?\"", NextID: "scene2_normal"},
		},
	}

	g.Nodes["scene2_no"] = &Node{
		ID: "scene2_no",
		Text: `"Impaired judgment." He nods. "But by whose standard? The average person
makes decisions while stressed, sleep-deprived, angry, in love. Are those
not alterations?"

He stands and walks to a window.

"The president has nuclear codes while running on four hours of sleep.
Surgeons operate after 20-hour shifts. Traders move billions while hopped
up on caffeine and cortisol."

He turns back to you.

"I'm the most monitored human on Earth. My blood chemistry is logged. My
decisions are reviewed. Is that not MORE careful than 'sober' decisions
made in emotional haste?"`,
		Options: []Option{
			{Text: "\"Two wrongs don't make a right. We should fix ALL those problems.\"", NextID: "scene2_two_wrongs"},
			{Text: "\"There's a difference between impairment by circumstance and by choice.\"", NextID: "scene2_choice"},
		},
	}

	g.Nodes["scene2_consequentialism"] = &Node{
		ID: "scene2_consequentialism",
		Text: `"A pragmatist! But consequentialism has a problem: we can't know
consequences in advance. By the time we know if my decisions were good,
it'll be too late to undo them."

He pulls up holographic graphs showing various metrics.

"My companies' success rate: 73%. Industry average: 12%. My neural-link
patients who've regained mobility: 847. My rockets have a 94% success
rate. The data suggests my judgment—altered or not—produces results."

He pauses.

"But I've also caused harm. People have died testing my products.
Markets have crashed on my tweets. Are those consequentialist failures,
or acceptable costs of progress?"`,
		Options: []Option{
			{Text: "\"The ends don't justify the means. Not ever.\"", NextID: "scene2_ends_means"},
			{Text: "\"It's a genuine tradeoff. I don't know the answer.\"", NextID: "scene2_tradeoff"},
		},
	}

	g.Nodes["scene2_nuance"] = &Node{
		ID: "scene2_nuance",
		Text: `"NUANCE! Finally!" He jumps up excitedly. "Yes! Not all alterations are
equal. Let me categorize:"

He starts ticking off fingers.

"Alcohol: lowers inhibitions, impairs motor function, increases aggression.
Probably bad for decisions.

Cannabis: alters time perception, enhances pattern recognition, reduces
anxiety. Mixed bag.

Ketamine at therapeutic doses: quiets default mode network, reduces ego
fixation, enables novel connections. I'd argue GOOD for certain decisions.

Psychedelics: profound but unpredictable. I use rarely."

He looks at you earnestly.

"The blanket term 'drugs' obscures these distinctions. Does that change
your view?"`,
		Options: []Option{
			{Text: "\"It's a fair point. But who decides which alterations are 'acceptable'?\"", NextID: "scene2_who_decides"},
			{Text: "\"You're rationalizing. An addict could make the same argument.\"", NextID: "scene2_rationalizing"},
		},
	}

	g.Nodes["scene2_normal"] = &Node{
		ID: "scene2_normal",
		Text: `He BEAMS.

"NOW we're getting somewhere! What IS normal consciousness? A specific
mix of neurotransmitters that evolution optimized for savanna survival?
Why would THAT be optimal for designing spacecraft?"

He begins pacing rapidly.

"'Normal' consciousness evolved to find food, avoid predators, and
reproduce. It generates anxiety because anxiety kept us alive. It
creates tribalism because tribes outcompeted loners."

"But we don't live on the savanna anymore. Maybe 'normal' is now
MALADAPTIVE. Maybe engineering consciousness is as valid as engineering
bridges."

He stops.

"Or maybe I'm just a junkie with good PR. That's the terrifying part.
How do I KNOW which it is?"`,
		Options: []Option{
			{Text: "\"External verification. Get sober people to review your ideas.\"", NextID: "scene2_verification"},
			{Text: "\"You can't know. That's why this is dangerous.\"", NextID: "scene2_danger"},
		},
	}

	// Scene 2 deeper branches

	g.Nodes["scene2_two_wrongs"] = &Node{
		ID: "scene2_two_wrongs",
		Text: `"Ah, the reformer's position. Fix everything, then judge me." He laughs,
but kindly.

"I admire the consistency. But reform takes time we may not have. While
you're fixing sleep schedules for presidents, the asteroid is coming.
Or the pandemic. Or the AI uprising."

He sits back down.

"I'm not PROUD of my methods. I'm PRACTICAL. If there were a better way
to operate at this speed, I'd take it. But there isn't. Not that I've
found."

His voice softens.

"Though maybe I haven't looked hard enough. Maybe that's what you're
here to show me."`,
		Options: []Option{
			{Text: "Proceed to the final reckoning", NextID: "scene3_start"},
		},
	}

	g.Nodes["scene2_choice"] = &Node{
		ID: "scene2_choice",
		Text: `"Choice versus circumstance." He nods gravely. "Yes. I CHOOSE this. Does
that make it worse? Or does intention matter?"

He's quiet for a moment.

"When I started, I didn't need anything. I was already successful. But
I hit a wall—the same ideas, cycling. My brain became a echo chamber."

"The first time I tried ketamine, in a clinical setting, I had three
ideas that became three companies worth billions. Coincidence? Maybe."

"Now I can't tell if the ketamine expands my mind or if I've just
become dependent. The line between tool and crutch blurs."

His vulnerability is startling.`,
		Options: []Option{
			{Text: "Proceed to confront this honestly", NextID: "scene3_start"},
		},
	}

	g.Nodes["scene2_ends_means"] = &Node{
		ID: "scene2_ends_means",
		Text: `"Never? NEVER?" He leans forward. "What if the alternative is extinction?
If compromising ethics saves humanity, isn't refusing to compromise the
truly unethical choice?"

He's genuinely wrestling with this.

"I tell myself I'm building a future. But sometimes I wonder if I'm
just building monuments to my ego. How do I know the difference?"

"Maybe that's why I take ketamine. To escape myself long enough to see
clearly. Or maybe I'm just hiding."

The conversation has become raw.`,
		Options: []Option{
			{Text: "Continue to the final scene", NextID: "scene3_start"},
		},
	}

	g.Nodes["scene2_tradeoff"] = &Node{
		ID: "scene2_tradeoff",
		Text: `"You don't know. I don't know. Nobody knows." He laughs bitterly.

"We're all gambling with the future based on incomplete information.
The difference is I'm gambling bigger. Is that courage or arrogance?"

He looks at his hands.

"847 people can move who couldn't before. Twelve people died in trials
to get there. Is that acceptable? I don't know. I'll never know. I just
keep moving forward and hope the calculus works out."

"Maybe that's all anyone can do."`,
		Options: []Option{
			{Text: "Move to the final confrontation", NextID: "scene3_start"},
		},
	}

	g.Nodes["scene2_who_decides"] = &Node{
		ID: "scene2_who_decides",
		Text: `"Who decides? That's THE question." He nods vigorously.

"Right now, I decide for myself. But I'm affecting millions. Should they
have a say in my neurochemistry? Should there be a 'fit for duty' test
for billionaires?"

He actually seems to consider this seriously.

"I'd submit to oversight, honestly, if I trusted the overseers. But
regulators are captured by industries. Politicians are bought. The
public is manipulated by algorithms."

"Who can I trust to judge my consciousness who isn't also compromised?"

His loneliness is palpable.`,
		Options: []Option{
			{Text: "Proceed to the conclusion", NextID: "scene3_start"},
		},
	}

	g.Nodes["scene2_rationalizing"] = &Node{
		ID: "scene2_rationalizing",
		Text: `He flinches like you've struck him.

"An addict." He breathes out slowly. "Yes. That word has crossed my mind.
Usually at 3 AM when the K wears off and the existential dread returns."

"I've done the addiction assessments. I score borderline. Not dependent
enough for clinical addiction, not healthy enough for casual use."

He looks at you with something like desperation.

"If I'm an addict, everything I've built is tainted. If I'm not, I'm a
pioneer. The difference might be semantic."

"How do YOU distinguish vision from delusion, {player}?"`,
		Options: []Option{
			{Text: "Face the final question together", NextID: "scene3_start"},
		},
	}

	g.Nodes["scene2_verification"] = &Node{
		ID: "scene2_verification",
		Text: `"External verification!" He claps. "SOCRATES, did you hear that? The human
suggests I verify my ideas with sober humans."

The AI responds: "MELON, 73.2% OF YOUR K-SPACE IDEAS ARE REJECTED BY THE
SOBER REVIEW BOARD. 8.1% BECOME MAJOR PRODUCTS."

He spreads his hands. "There you go. Most of my high ideas are garbage.
But 8% change the world. Do we throw out the 8% to avoid the 92%?"

He seems genuinely uncertain.

"Or is 8% just what you'd expect from random variation?"`,
		Options: []Option{
			{Text: "Time for the final reckoning", NextID: "scene3_start"},
		},
	}

	g.Nodes["scene2_danger"] = &Node{
		ID: "scene2_danger",
		Text: `"I can't know." He slumps. "The honest answer. Maybe I'm a visionary.
Maybe I'm a cautionary tale future generations will tell."

"I've tried to build safeguards. SOCRATES. The review board. My own
written rules for what I can and can't do while altered."

"But safeguards only work if I follow them. And I've broken every one
at some point."

He looks at you.

"What if the safeguard should be... stopping? What if I should just...
stop?"

The question hangs heavy in the air.`,
		Options: []Option{
			{Text: "Proceed to the final decision", NextID: "scene3_start"},
		},
	}

	// ==================== SCENE 3: THE VISION AND FINAL RECKONING ====================

	g.Nodes["scene3_start"] = &Node{
		ID: "scene3_start",
		Text: `SCENE 3: THE VISION AND FINAL RECKONING

The candles have burned low. Melon Husk looks exhausted, more human than
you've seen him all day. The monitors around the room show his biometrics
returning to baseline.

"Before you go, {player}, I want to show you something. Something I've
never shown anyone outside my inner circle."

He presses a sequence on his tablet, and the room transforms. Holographic
projections surround you—a vision of Mars, but not as it is. As he
imagines it: domed cities, children playing in artificial gardens,
humanity thriving on a new world.

"This is why I do what I do. All of it. The rockets, the tunnels, the
neural links. Even the ketamine. All paths lead here."

He turns to you.

"You've spent a day challenging me. Now I need you to answer honestly:
After everything you've seen, what do you think of my vision—and my
method?"`,
		Options: []Option{
			{Text: "\"The vision is beautiful. The method is still troubling.\"", NextID: "scene3_beautiful_troubling"},
			{Text: "\"I think you're brilliant but need help. Not in a condescending way.\"", NextID: "scene3_need_help"},
			{Text: "\"I don't know anymore. You've shaken my certainties.\"", NextID: "scene3_shaken"},
			{Text: "\"The vision doesn't justify the risk. You're gambling with too much.\"", NextID: "scene3_gambling"},
		},
	}

	g.Nodes["scene3_beautiful_troubling"] = &Node{
		ID: "scene3_beautiful_troubling",
		Text: `He nods slowly, something like respect in his eyes.

"Troubling. Yes. It troubles me too, when I'm sober enough to feel it."

He walks through his holographic Mars, hand passing through a projected
child.

"What would you have me do, {player}? Stop the substances and lose
whatever edge they provide? Continue and risk everything on a potentially
impaired judgment?"

"Or is there a middle path you see that I don't?"`,
		Options: []Option{
			{Text: "\"Reduce reliance gradually. Build systems that don't depend on your K-state.\"", NextID: "scene3_gradual"},
			{Text: "\"Keep going but be more honest publicly about your methods.\"", NextID: "scene3_honest"},
			{Text: "\"I genuinely don't know what to advise.\"", NextID: "scene3_no_advice"},
		},
	}

	g.Nodes["scene3_need_help"] = &Node{
		ID: "scene3_need_help",
		Text: `He laughs—but it's not defensive. It's almost relieved.

"Need help. When's the last time anyone said that to me without wanting
something? Without trying to manipulate me?"

He looks at the Mars projection.

"I've surrounded myself with yes-men. People who tell me what I want to
hear because I sign their paychecks. SOCRATES tries to check me, but AI
doesn't have... whatever YOU have."

He faces you directly.

"Will you help me, {player}? Be a voice that challenges me? I could use
someone who isn't afraid to say 'this is a bad idea'."`,
		Options: []Option{
			{Text: "\"I'd consider it. But I won't enable substance use.\"", NextID: "scene3_conditions"},
			{Text: "\"That's not my place. But I can point you toward professionals.\"", NextID: "scene3_professionals"},
		},
	}

	g.Nodes["scene3_shaken"] = &Node{
		ID: "scene3_shaken",
		Text: `"I've shaken your certainties?" He smiles sadly. "Welcome to my world.
Certainty is a luxury I lost years ago."

He shuts down the Mars projection. The room returns to normal—just a
rich man's office, fancy but mundane.

"Maybe that's the real answer. Nobody knows. I don't know if I'm a
visionary or a cautionary tale. You don't know if my methods are genius
or madness."

"Maybe the best we can do is keep questioning. Keep each other honest."

He extends his hand.

"Thank you, {player}. For questioning me. It's the most useful thing
anyone's done for me in months."`,
		Options: []Option{
			{Text: "Shake his hand and part as uncertain allies", NextID: "ending_philosophical"},
			{Text: "Shake his hand but maintain critical distance", NextID: "ending_neutral"},
		},
	}

	g.Nodes["scene3_gambling"] = &Node{
		ID: "scene3_gambling",
		Text: `His face hardens slightly, then softens.

"Gambling. Yes. But the alternative is certainty of extinction, isn't it?
If we stay on Earth, doing things the 'safe' way, eventually something
kills us. Certainty."

"My gamble at least has a CHANCE of success."

But he looks uncertain.

"Unless you're right. Unless the gamble itself introduces risks that
exceed what I'm trying to prevent. The cure worse than the disease."

He looks at you intensely.

"If you truly believe that, will you try to stop me?"`,
		Options: []Option{
			{Text: "\"Not stop you. But I'll be a critical voice.\"", NextID: "scene3_critical_voice"},
			{Text: "\"I'll oppose any decision I think endangers humanity.\"", NextID: "scene3_oppose"},
			{Text: "\"No. It's your life, your choice. I just needed you to hear the concern.\"", NextID: "scene3_your_choice"},
		},
	}

	// Final branches before endings

	g.Nodes["scene3_gradual"] = &Node{
		ID: "scene3_gradual",
		Text: `"Gradual reduction." He considers this. "SOCRATES has suggested the same.
Taper down, build redundancy, train successors who can operate sober."

He pulls up his calendar—packed with meetings, launches, decisions.

"It would slow everything down. Years, maybe. More time for asteroids
to find us, pandemics to evolve."

"But maybe haste is its own risk. Maybe building sustainable systems is
better than building fast, fragile ones."

He looks at you with something like hope.

"Would you check in on me, {player}? Periodically? To see if I'm
keeping to a better path?"`,
		Options: []Option{
			{Text: "\"Yes. I'll hold you accountable.\"", NextID: "ending_good"},
			{Text: "\"I don't think that's my role, but I wish you well.\"", NextID: "ending_neutral"},
		},
	}

	g.Nodes["scene3_honest"] = &Node{
		ID: "scene3_honest",
		Text: `"Honesty." He frowns. "Go public about the ketamine? The stock price
would crater. Regulators would investigate. My enemies would feast."

He paces.

"But... lies compound. Every secret I keep becomes a weapon someone can
use against me. Maybe radical honesty is the better strategy."

"Or maybe it's naive. I don't know."

He looks at you.

"Would the public accept an openly psychedelic-using billionaire shaping
their future? Or would they burn me at the stake?"`,
		Options: []Option{
			{Text: "\"Some would reject you. Others might respect the honesty. It's a risk.\"", NextID: "ending_neutral"},
			{Text: "\"I think honesty is always better, whatever the consequences.\"", NextID: "ending_philosophical"},
		},
	}

	g.Nodes["scene3_no_advice"] = &Node{
		ID: "scene3_no_advice",
		Text: `"No advice." He nods. "The honest answer. I appreciate that more than
you know."

He shuts down the holograms and sits heavily in a chair.

"Everyone has advice for me. Do this, don't do that. Take this drug,
stop that drug. You're the first person in years to say 'I don't know.'"

"Maybe the best gift you can give me is that uncertainty. A reminder
that nobody has the answers, even me."

He smiles tiredly.

"Especially me."`,
		Options: []Option{
			{Text: "Leave him to his uncertainty", NextID: "ending_philosophical"},
		},
	}

	g.Nodes["scene3_conditions"] = &Node{
		ID: "scene3_conditions",
		Text: `"Conditions. Boundaries. You set TERMS." He sounds almost delighted.
"Nobody sets terms with me anymore. I've missed it."

He walks to his desk and pulls out a paper notebook—old school.

"Write them down. Your conditions. I'll sign them, have SOCRATES hold
me accountable."

He hands you the pen.

"Make me be better, {player}. Please."`,
		Options: []Option{
			{Text: "Write reasonable conditions and agree to help", NextID: "ending_good"},
			{Text: "This is too much responsibility. Decline.", NextID: "ending_neutral"},
		},
	}

	g.Nodes["scene3_professionals"] = &Node{
		ID: "scene3_professionals",
		Text: `"Professionals." His voice flattens. "Therapists, doctors, addiction
specialists. I've seen them. They see dollar signs or research papers.
They don't see ME."

He sighs.

"But you're right. It's not your responsibility to fix me. I'm sorry
for asking. It was unfair."

He seems to shrink a little.

"Thank you for your time today, {player}. It meant more than you know."`,
		Options: []Option{
			{Text: "Leave with compassion but appropriate boundaries", NextID: "ending_neutral"},
		},
	}

	g.Nodes["scene3_critical_voice"] = &Node{
		ID: "scene3_critical_voice",
		Text: `"A critical voice. Not trying to stop me, but to question me." He nods
slowly. "That might be exactly what I need. SOCRATES does it, but AI
lacks... skin in the game."

He extends his hand.

"I'll give you a direct line. Whenever I'm about to make a major
decision, you'll have the chance to challenge me. No obligation. Just...
access."

"Will you accept?"`,
		Options: []Option{
			{Text: "Accept the responsibility", NextID: "ending_good"},
			{Text: "Decline—too much power, too much burden", NextID: "ending_neutral"},
		},
	}

	g.Nodes["scene3_oppose"] = &Node{
		ID: "scene3_oppose",
		Text: `His expression goes cold, then thoughtful.

"Oppose me. Well. At least you're honest." He walks to the window,
looking out at his rockets.

"I've had opponents before. Regulators, rivals, ex-wives. You'd be
different—a principled opponent, not a self-interested one."

He turns back to you.

"I respect that, {player}. I won't make it easy for you. But I respect
it."

The warmth between you has chilled.`,
		Options: []Option{
			{Text: "Leave as adversaries, but with mutual understanding", NextID: "ending_neutral"},
		},
	}

	g.Nodes["scene3_your_choice"] = &Node{
		ID: "scene3_your_choice",
		Text: `"My choice." He seems both relieved and disappointed. "Yes. Ultimately,
it is. No one can stop me. I have more resources than most governments."

He looks at the Mars projection one last time before shutting it down.

"Thank you for your concern, genuinely. But I think we both know nothing
changes tonight. I'll keep doing what I do. You'll keep having doubts."

He walks you to the door.

"Maybe that's all any of us can do. Try, doubt, and hope we're not the
villain in someone else's story."`,
		Options: []Option{
			{Text: "Leave with the weight of unanswered questions", NextID: "ending_philosophical"},
		},
	}

	// ==================== ENDINGS ====================

	g.Nodes["ending_good"] = &Node{
		ID:   "ending_good",
		IsEnding:   true,
		EndingType: "good",
		Text: `You leave the SpaceZ facility as dawn breaks over the Texas desert. Your
phone already has a message from SOCRATES: "WELCOME TO THE OVERSIGHT
COMMITTEE, {player}."

In the months that follow, you become an unlikely voice in Melon Husk's
empire—challenging, questioning, occasionally talking him down from
K-fueled flights of fancy. His drug use decreases, not to zero, but to
something more managed.

Mars colonies may still come. But now they'll be built with more than
one man's visions and chemicals. They'll be built with questions.

Maybe that's the best any of us can do: ensure that the people shaping
our future have to answer to someone. Even if that someone doesn't have
all the answers either.

The ketamine question remains unanswered. Perhaps that IS the answer.`,
	}

	g.Nodes["ending_neutral"] = &Node{
		ID:   "ending_neutral",
		IsEnding:   true,
		EndingType: "neutral",
		Text: `You leave the SpaceZ facility as dawn breaks over the Texas desert.
Melon Husk watches from his window, a small figure against the vast
machines that embody his ambition.

You don't join his circle. You don't oppose him. You return to your life,
but you're changed. The questions he raised—about consciousness, about
progress, about the ethics of altering minds to alter futures—stay with
you.

In the years that follow, you watch his launches, his announcements, his
controversies. Sometimes he seems brilliant; sometimes dangerously unhinged.
You can never quite tell which.

Maybe that's the point. Maybe genius and madness share a border so thin
that even the people living there can't tell which side they're on.

You made no difference today. But you bear witness. That has to count
for something.`,
	}

	g.Nodes["ending_philosophical"] = &Node{
		ID:   "ending_philosophical",
		IsEnding:   true,
		EndingType: "philosophical",
		Text: `You leave the SpaceZ facility as dawn breaks over the Texas desert.
Neither ally nor enemy, neither convert nor critic—just someone who
spent a day in the presence of a question mark shaped like a man.

Is it wise to get ideas about humanity's future while high? You still
don't know. But now you understand that the question itself is more
valuable than any easy answer.

Socrates—the real one—said the unexamined life is not worth living.
Melon Husk examines his life compulsively, chemically, obsessively.
Too much? Too little? The wrong way? The right way?

All you know is that the future will be shaped by people who are
certain, and maybe it shouldn't be. Maybe what humanity needs isn't
better answers but better questions.

You asked questions today. That's enough. That has to be enough.

The rest is silence—and the distant roar of rockets, reaching for stars
that don't care how sober we were when we dreamed of them.`,
	}

	g.Nodes["ending_bad"] = &Node{
		ID:   "ending_bad",
		IsEnding:   true,
		EndingType: "bad",
		Text: `You leave the SpaceZ facility as dawn breaks over the Texas desert.
Something in you has shifted—not broken, exactly, but bent.

Melon Husk was persuasive. Too persuasive. You find yourself thinking:
maybe he's right. Maybe consciousness should be engineered. Maybe the
future SHOULD be built by chemically-enhanced visionaries who see
further than the rest of us.

In the weeks that follow, you seek out your own experiments. Small doses
at first. Then larger. You're not building rockets, but you're THINKING
bigger. Aren't you? The ideas feel profound. They must be profound.

This is how it starts. Not with villainy, but with curiosity. Not with
corruption, but with questions. You wanted to understand Melon Husk.

Now you're becoming him.

Some doors, once opened, cannot be closed.`,
	}

	g.Nodes["ending_transcendent"] = &Node{
		ID:   "ending_transcendent",
		IsEnding:   true,
		EndingType: "transcendent",
		Text: `You leave the SpaceZ facility as dawn breaks over the Texas desert, but
"leaving" feels like the wrong word. Part of you stays. Part of you was
always there.

The conversation with Melon Husk opened something—not a door exactly,
more like a crack in the ordinary. Through it, you glimpsed what he
sees: the vast indifference of the universe, the fragility of
consciousness, the strange miracle that anything exists at all.

You don't need ketamine to see it now. Once seen, it can't be unseen.

Humanity will go to the stars, or it won't. Melon Husk will be
remembered as a visionary, or a warning. None of it matters in the way
you once thought things mattered.

And somehow, that's beautiful. The not-mattering is the mattering.

You walk into the desert sunrise, carrying questions that have no
answers, and finding that enough.

More than enough.`,
	}
}
