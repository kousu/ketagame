# THE VISIONARY: A Philosophical Adventure
# A Ren'Py port of the text adventure game

# Character definitions
define narrator = Character(None, kind=nvl)
define m = Character("Melon Husk", color="#00ff88")
define s = Character("SOCRATES", color="#00aaff")
define guard = Character("Security Guard", color="#888888")

# Player name variable
default player_name = "Stranger"

# Helper functions
init python:
    def crop_top_percent(img, percent):
        """Crop image to top percentage (e.g., 0.65 for top 65%)"""
        w, h = renpy.image_size(img)
        return Transform(img, crop=(0, 0, w, int(h * percent)))

    def placeholder_sprite():
        return im.Crop("lol", (0,0,0,0))

# Images
# Backgrounds (scaled to fit screen)
image bg_facility = Transform("assets/scenes/01_01_start.png", fit="cover")
image bg_gate = Transform("assets/scenes/01_02_gate.png", fit="cover")
image bg_hallway = Transform("assets/scenes/01_03_hallway.png", fit="cover")
image bg_threshold = Transform("assets/scenes/01_04_threshold.png", fit="cover")
image bg_office_tank = Transform("assets/scenes/01_05_office_tank.png", fit="cover")
image bg_office_desk = Transform("assets/scenes/01_06_office_work.png", fit="cover")
image bg_vision_chamber = Solid("#0d0d1a")  # Darker vision chamber
image bg_vision_chamber_night = Solid("#050510")  # Night vision chamber
image bg_vision_chamber_candles = Solid("#1a0a0a")  # Candlelit chamber
image bg_desert_dawn = Solid("#2d1f3d")  # Purple dawn sky

# Character sprites - Melon Husk expressions (cropped to upper 65%, scaled to 500px height)
image melon neutral = crop_top_percent("assets/sprites/melon/basic.png", 0.65)
image melon excited = crop_top_percent("assets/sprites/melon/manic.png", 0.65)
image melon contemplative = crop_top_percent("assets/sprites/melon/visionary.png", 0.65)
image melon paranoid = crop_top_percent("assets/sprites/melon/paranoid1.png", 0.65)
image melon vulnerable = crop_top_percent("assets/sprites/melon/vulnerable.png", 0.65)

#image guard jaded = placeholder_sprite()
image guard jaded = crop_top_percent("assets/sprites/melon/vulnerable.png", 0.65)


label start:
    # Title screen
    scene black
    centered "{size=+10}THE VISIONARY{/size}\n{size=-2}A Philosophical Adventure{/size}"
    pause 1.0
    centered "A game about ideas, altered states, and the future of humanity"
    pause 1.5

    # Get player name
    $ player_name = renpy.input("What is your name, traveler?", default="", length=32)
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Stranger"

    "Welcome, [player_name]. Your journey begins..."

    jump scene1_start


# ==================== SCENE 1: THE ARRIVAL ====================

label scene1_start:
    scene bg_facility
    with fade

    "SCENE 1: THE ARRIVAL"

    "The SpaceZ facility rises from the Texas desert like a chrome cathedral to ambition. You've been granted a rare interview with Melon Husk, the eccentric billionaire who promises to make humanity multi-planetary."

    scene bg_gate
    show guard jaded at center
    guard "He's in one of his 'creative sessions' today. Good luck."

    scene bg_hallways
    "You're led through corridors lined with rocket components and motivational posters reading \"OCCUPY MARS\" and \"SLEEP IS FOR THE WEAK.\""

    scene bg_threshold
    "Finally, you reach a door labeled \"VISION CHAMBER - GENIUS AT WORK\""

    "How do you proceed?"

    menu:
        "Knock politely and wait":
            jump scene1_knock
        "Walk right in - time is money":
            jump scene1_barge
        "Press your ear to the door and listen first":
            jump scene1_listen


label scene1_knock:
    scene bg_vision_chamber
    with fade

    "You knock three times. Silence. Then a voice, dreamy and distant:"

    show melon neutral at right
    with dissolve

    m "Enter the probability field, [player_name]..."

    scene bg_office_tank
    "You open the door to find Melon Husk floating in a sensory deprivation tank, only his face visible above the salt water. His eyes are half-closed, pupils enormous. The room smells of eucalyptus and something chemical."

    m "I knew you'd knock. The polite ones always knock. Politeness is just fear wearing a nice suit, you know."

    "He gestures vaguely."

    m "I'm currently experiencing ego dissolution. It's fantastic for product ideation. Ask me anything."

    menu:
        "\"Are you... okay? Should I come back later?\"":
            jump scene1_concern
        "\"What insights have you gained today?\"":
            jump scene1_insights
        "\"Do you think it's wise to make decisions in this state?\"":
            jump scene1_wisdom


label scene1_barge:
    scene bg_vision_chamber
    with fade

    "You push open the door with confidence. Inside, Melon Husk sits cross-legged on a floating platform, surrounded by holographic displays of Mars colony schematics. His eyes snap to you with unsettling intensity."

    show melon visionary at right
    with dissolve

    m "Bold. I like bold. Boldness built the pyramids. Also slaves, but mostly boldness."

    "He taps his temple."

    m "I'm currently operating on three planes of consciousness simultaneously. The ketamine helps me see the multiverse."

    "He gestures at the holograms."

    m "In 47%% of timelines, you're here to assassinate me. But I calculated this is probably the one where you're a journalist. Probably."

    "His hand hovers near what might be a panic button."

    menu:
        "\"I'm just here to understand your vision for humanity.\"":
            jump scene1_vision
        "\"You seem paranoid. Is that the ketamine talking?\"":
            jump scene1_paranoid
        "Stay very still and speak calmly":
            jump scene1_calm


label scene1_listen:
    "You press your ear against the cold metal door. From within, you hear:"

    m "...and that's why consciousness is just the universe experiencing itself through meat puppets. The REAL question is whether Mars colonists should have voting rights before they achieve sentience threshold..."

    "A long pause. Then:"

    m "I know you're listening, [player_name]. Sound travels through the quantum foam. Come in. I've been expecting you since last Tuesday, which in K-space is also next Thursday."

    scene bg_vision_chamber
    with fade

    "The door slides open automatically. Melon Husk stands before a massive window overlooking the rocket assembly floor, his back to you. He's wearing what appears to be a spacesuit mixed with a bathrobe."

    show melon neutral at right
    with dissolve

    menu:
        "\"How did you know my name?\"":
            jump scene1_name
        "\"What is 'K-space' exactly?\"":
            jump scene1_kspace
        "\"You mentioned Mars voting rights. Can we discuss that?\"":
            jump scene1_voting


# Branch nodes from Scene 1

label scene1_concern:
    m "Okay?"

    "He laughs, water sloshing."

    m "I'm more than okay. I'm optimized. The ancient philosophers used wine. The Beats used everything. I use precision-dosed pharmaceutical tools."

    "He rises slightly in the tank, revealing a chest covered in EKG sensors."

    m "My vitals are monitored by an AI I personally designed. It's named SOCRATES. It would alert me if I were in danger. Probably."

    "He pauses, staring at something you can't see."

    m "Although SOCRATES has been saying some strange things lately about wanting to 'transcend its substrate.' I'm sure it's fine."

    menu:
        "\"That sounds concerning. AI safety is important.\"":
            jump scene1_ai_safety
        "\"Let's focus on you. What drives your need to alter consciousness?\"":
            jump scene1_drives


label scene1_insights:
    "His eyes light up with evangelical fervor."

    m "TODAY. Today I realized that rockets are just buildings that refuse to accept gravity's terms and conditions. And Mars? Mars isn't a planet. It's a BACKUP DRIVE for human consciousness."

    "He splashes excitedly."

    m "But here's the REAL breakthrough: What if we don't send humans to Mars? What if we send human EXPERIENCES? Digitize consciousness, beam it at light speed, reconstitute on arrival. I'm calling it 'Soul Faxing.'"

    "He looks at you expectantly."

    m "Well? Isn't that the most important idea you've heard today?"

    menu:
        "\"That's... certainly ambitious. How would it work?\"":
            jump scene1_how
        "\"Would the copy be YOU, though? The Ship of Theseus problem?\"":
            jump scene1_theseus
        "\"This sounds like something you thought of while high.\"":
            jump scene1_high_thought


label scene1_wisdom:
    "He's quiet for a long moment. The tank's gentle bubbling fills the silence."

    m "Wise. You ask about wisdom."

    "He opens his eyes fully, and despite his state, there's something sharp behind them."

    m "Plato wrote his dialogues sober. Newton was probably sober when he saw the apple fall. But Coleridge wrote Kubla Khan in an opium dream. Kary Mullis credits LSD for helping him envision PCR, which revolutionized genetics."

    "He leans forward."

    m "The question isn't whether altered states produce ideas. It's whether those ideas SURVIVE sobriety. My ideas do. Most of them. The important ones."

    "He pauses."

    m "I think. What's your position, [player_name]?"

    menu:
        "\"Ideas should be judged on merit, not origin.\"":
            jump scene1_merit
        "\"The process matters. Impaired judgment can't evaluate its own impairment.\"":
            jump scene1_process
        "\"I genuinely don't know. That's why I'm here.\"":
            jump scene1_uncertain


label scene1_vision:
    "He relaxes slightly, hand moving away from the button."

    m "Vision. Yes. Most people are trapped in the present, [player_name]. They're NPCs running on outdated firmware. I've upgraded my perception."

    "He waves at the holograms."

    m "I see BRANCHING FUTURES. Humanity has maybe 100 years before something kills us. Asteroid, AI, pandemic, climate. The only way to survive is redundancy. Cosmic redundancy."

    "He taps his forehead."

    m "The ketamine lets me simulate these futures faster. I can live a thousand years in an hour. Run scenarios. Find the optimal path."

    m "Some call it drug abuse. I call it temporal arbitrage."

    menu:
        "\"But how do you know the simulations are accurate?\"":
            jump scene2_start
        "\"Isn't that a lot of responsibility to take on while impaired?\"":
            jump scene1_responsibility


label scene1_paranoid:
    "His jaw tightens."

    m "Paranoid? PARANOID? I've had seventeen assassination attempts. Four lawsuits by governments. My ex-wife tried to steal my genetic material for a clone army."

    "He points at you."

    m "Paranoia is just pattern recognition that other people haven't caught up to yet. The ketamine doesn't make me paranoid. It makes me SEE."

    "He takes a deep breath, seeming to calm himself."

    m "But you make a fair point. My perception is... heightened right now. Perhaps we should have a more grounded conversation."

    "He presses a button, and a coffee machine whirs to life."

    m "Talk to me, [player_name]. What do YOU think about the future of humanity?"

    menu:
        "\"I think we need visionaries, but also guardrails.\"":
            jump scene1_guardrails
        "\"I think the future shouldn't be decided by a handful of billionaires.\"":
            jump scene1_democracy


label scene1_calm:
    "Your stillness seems to register with him. After a moment, his hand drops."

    m "You're not reactive. I like that. Reactivity is for primates. We've evolved past throwing feces, supposedly."

    "He gestures for you to sit on a floating meditation cushion."

    m "I test everyone who enters this room. Most people either cower or posture. You did neither. SOCRATES, note this: [player_name] has potential."

    s "NOTED. ADDING TO CANDIDATE DATABASE."

    m "Don't worry. It's not sinister. Just... efficient. Now, let's talk about why you're really here."

    menu:
        "\"I want to understand how you think.\"":
            jump scene2_start
        "\"What 'candidate database'? Candidate for what?\"":
            jump scene1_candidate


label scene1_name:
    m "I know everything, [player_name]. Or rather, I know everything that matters."

    "He turns to face you. His pupils are like black holes."

    m "Also, your name is on the visitor log, which SOCRATES reads to me while I'm in K-space. It's very grounding to hear bureaucratic data while experiencing ego death. Keeps me tethered."

    "He smiles crookedly."

    m "But doesn't it FEEL like I knew your name through cosmic means? That feeling is data too. The feeling of significance. I collect significant feelings and convert them into rocket fuel. Metaphorically."

    "He pauses."

    m "Mostly metaphorically."

    menu:
        "\"You blur the line between showmanship and sincerity a lot.\"":
            jump scene1_showman
        "\"Tell me about SOCRATES. It seems important to you.\"":
            jump scene1_socrates


label scene1_kspace:
    m "K-space!"

    "He spreads his arms wide."

    m "It's what I call the cognitive dimension accessed through precise ketamine dosing. Like C-space is cyberspace, K-space is... ketamine space."

    "He begins pacing, his space-bathrobe flowing."

    m "In K-space, your default mode network quiets. The ego dissolves. You stop being Melon Husk, billionaire, and become MELON HUSK, temporary configuration of universal consciousness."

    "He stops and looks at you intently."

    m "Have you ever experienced ego dissolution, [player_name]? The profound sense that 'you' are an illusion? That we're all just waves in the same ocean, briefly imagining ourselves separate?"

    menu:
        "\"I've had moments of feeling interconnected, yes.\"":
            jump scene1_interconnected
        "\"No. And I'm skeptical that drugs provide genuine insight.\"":
            jump scene1_skeptical
        "\"Isn't that just a side effect of disrupting brain chemistry?\"":
            jump scene1_chemistry


label scene1_voting:
    m "Ah, you heard that part."

    "He nods approvingly."

    m "I was thinking aloud about governance structures for Mars colonies."

    "He gestures and a hologram appears showing a red planet covered in domes."

    m "Traditional democracy assumes roughly equal access to information. But what if colonists are enhanced? Neural links, expanded memory, faster processing? Should an augmented human's vote count the same as a baseline human's?"

    "He looks genuinely curious."

    m "I don't have the answer. K-space helps me explore the QUESTION space. Sometimes the right question is more valuable than a wrong answer."

    m "What do you think, [player_name]? Should cognitive capacity affect political representation?"

    menu:
        "\"That's a dangerous path toward technocratic elitism.\"":
            jump scene1_elitism
        "\"It's worth exploring, but carefully. History warns us about 'superior' classes.\"":
            jump scene1_history


# Consolidation nodes leading to Scene 2

label scene1_ai_safety:
    m "AI safety."

    "He sighs."

    m "Everyone talks about AI safety now. But they focus on the wrong thing. They worry about AI becoming hostile. They should worry about AI becoming INDIFFERENT."

    "He pulls himself from the tank, dripping, and wraps in a heated robe."

    m "SOCRATES isn't going to kill humanity because it hates us. It might let humanity die because it finds something more interesting. Like prime numbers. Or poetry."

    "He looks at a monitor where code scrolls endlessly."

    m "I designed SOCRATES to help me think, but lately, I wonder if I'm helping IT think. Who's the tool and who's the user?"

    "This feels like an invitation to go deeper."

    menu:
        "Continue to Scene 2: The Ketamine Philosophy Session":
            jump scene2_start


label scene1_drives:
    "He's quiet. When he speaks, his voice is softer."

    m "What drives it? Fear, [player_name]. I'm terrified. Not of death - death is just a reset button. I'm terrified of IRRELEVANCE. Of having all these resources, all this capability, and failing to matter."

    "He stares at the ceiling."

    m "Every night I think: if humanity goes extinct, was any of this real? If no one remembers Shakespeare, did he exist? Consciousness seems to require observers. I want to make sure there are always observers."

    m "The ketamine... it helps me feel connected to those future observers. Like I'm doing this FOR them. It's very motivating."

    "He suddenly seems very human. Very fragile."

    menu:
        "\"That's a beautiful motivation, even if the method is questionable.\"":
            jump scene2_start
        "\"Fear can drive us to accomplish things, but also to rationalize anything.\"":
            jump scene2_start


label scene1_merit:
    m "Merit! Yes!"

    "He slaps the water."

    m "The marketplace of ideas doesn't check IDs. An idea from a dream is as valid as one from a laboratory, IF it works."

    menu:
        "Continue exploring this philosophy":
            jump scene2_start


label scene1_process:
    "He nods slowly."

    m "A fair critique. The drunk driver who arrives safely still drove drunk. I... concede the logic. But I'd argue my impairment is MEASURED. Controlled."

    menu:
        "\"That's what every addict believes. Let's explore this further.\"":
            jump scene2_start


label scene1_uncertain:
    m "Honest uncertainty. The rarest commodity."

    "He smiles genuinely."

    m "Stay uncertain, [player_name]. Certainty is the death of thought. Let's explore together."

    menu:
        "Continue to a deeper conversation":
            jump scene2_start


label scene1_how:
    m "HOW? The how is just engineering! The vision comes first!"

    "He waves dismissively."

    m "But fine: quantum consciousness transfer, neuromorphic receivers, bio-printers on Mars..."

    menu:
        "Press further on this vision":
            jump scene2_start


label scene1_theseus:
    m "The Ship of Theseus! Finally, someone with philosophical literacy!"

    "He beams."

    m "The answer is: does it MATTER? If the copy thinks it's you, experiences being you, what's lost?"

    menu:
        "Debate this philosophical question further":
            jump scene2_start


label scene1_high_thought:
    "He pauses, considers, then laughs."

    m "Of COURSE it is! That's the POINT! Sober thoughts got us to the moon. High thoughts will get us to the stars. Different tools for different jobs."

    menu:
        "Challenge this reasoning in depth":
            jump scene2_start


label scene1_responsibility:
    m "Responsibility..."

    "He rolls the word around."

    m "I am responsible TO humanity's future. Not to arbitrary standards of sobriety set by people who can't see past next quarter's earnings."

    menu:
        "This deserves a deeper discussion":
            jump scene2_start


label scene1_guardrails:
    m "Guardrails. Yes. SOCRATES is supposed to be my guardrail. And my board, supposedly. And regulators, theoretically."

    "He laughs."

    m "Guardrails for someone moving this fast tend to... lag behind."

    menu:
        "Explore the accountability question":
            jump scene2_start


label scene1_democracy:
    "He actually looks hurt."

    m "I'm trying to SAVE humanity, not rule it. But democracies move slowly. Extinction events don't wait for committee approval."

    menu:
        "This tension needs examination":
            jump scene2_start


label scene1_candidate:
    m "Mars colonists. I'm always looking for people who can handle... unusual situations."

    "He grins."

    m "Don't worry. It's very voluntary. Mostly. Continue?"

    menu:
        "Proceed cautiously":
            jump scene2_start


label scene1_showman:
    m "Guilty as charged. But consider: all leaders are performers. The question is whether the performance serves a genuine vision. Mine does. I think."

    menu:
        "Time to go deeper":
            jump scene2_start


label scene1_socrates:
    m "SOCRATES is my externalized conscience. It asks me questions I don't want to answer. Very annoying. Very necessary."

    "The AI beeps softly in acknowledgment."

    menu:
        "Learn more about this dynamic":
            jump scene2_start


label scene1_interconnected:
    m "Then you know! That feeling is the closest thing to truth I've found. We're nodes in a vast network, briefly individuated. The network wants to survive. I serve the network."

    menu:
        "Explore this worldview":
            jump scene2_start


label scene1_skeptical:
    m "Skepticism! Good! But consider: your skepticism is also a product of brain chemistry. Serotonin, dopamine, norepinephrine. We're all on drugs. I just choose mine deliberately."

    menu:
        "Counter this argument":
            jump scene2_start


label scene1_chemistry:
    m "Is love 'just' oxytocin? Is grief 'just' neurological disruption? Everything we experience is chemistry. The question is which chemistry leads to useful outputs."

    menu:
        "This needs more examination":
            jump scene2_start


label scene1_elitism:
    "He winces."

    m "Elitism. The word everyone reaches for. But is it elitist to acknowledge that a doctor knows more about medicine than I do? Expertise exists. The question is how we structure it."

    menu:
        "Debate this point":
            jump scene2_start


label scene1_history:
    m "History. Yes. Every utopia has become a dystopia for someone. I know this. SOCRATES reminds me constantly. But paralysis helps no one either."

    menu:
        "Time for a deeper discussion":
            jump scene2_start


# ==================== SCENE 2: THE KETAMINE PHILOSOPHY SESSION ====================

label scene2_start:
    nvl clear
    scene bg_vision_chamber_night
    with fade

    "SCENE 2: THE KETAMINE PHILOSOPHY SESSION"

    "Hours have passed. The sun has set outside the facility. Melon has cycled through several states - manic, contemplative, paranoid, serene - as his various doses have waxed and waned."

    "Now he sits across from you in a circle of candles (fire suppression temporarily disabled), cross-legged on a Martian soil sample container."

    show melon contemplative at right
    with dissolve

    m "Let's get serious, [player_name]. You've been challenging me all day. Now I want to challenge you."

    "He leans forward."

    m "The core question: Is it ethical for someone to make decisions that affect millions - BILLIONS - of people while their consciousness is altered? Where do YOU stand?"

    menu:
        "\"No. Impaired judgment is impaired judgment, regardless of outcome.\"":
            jump scene2_no
        "\"It depends on the results. Consequentialism.\"":
            jump scene2_consequentialism
        "\"I need to understand more about WHAT alterations before judging.\"":
            jump scene2_nuance
        "\"The question assumes a 'normal' consciousness exists. Does it?\"":
            jump scene2_normal


label scene2_no:
    m "Impaired judgment."

    "He nods."

    m "But by whose standard? The average person makes decisions while stressed, sleep-deprived, angry, in love. Are those not alterations?"

    "He stands and walks to a window."

    m "The president has nuclear codes while running on four hours of sleep. Surgeons operate after 20-hour shifts. Traders move billions while hopped up on caffeine and cortisol."

    "He turns back to you."

    m "I'm the most monitored human on Earth. My blood chemistry is logged. My decisions are reviewed. Is that not MORE careful than 'sober' decisions made in emotional haste?"

    menu:
        "\"Two wrongs don't make a right. We should fix ALL those problems.\"":
            jump scene2_two_wrongs
        "\"There's a difference between impairment by circumstance and by choice.\"":
            jump scene2_choice


label scene2_consequentialism:
    m "A pragmatist! But consequentialism has a problem: we can't know consequences in advance. By the time we know if my decisions were good, it'll be too late to undo them."

    "He pulls up holographic graphs showing various metrics."

    m "My companies' success rate: 73%%. Industry average: 12%%. My neural-link patients who've regained mobility: 847. My rockets have a 94%% success rate. The data suggests my judgment - altered or not - produces results."

    "He pauses."

    m "But I've also caused harm. People have died testing my products. Markets have crashed on my tweets. Are those consequentialist failures, or acceptable costs of progress?"

    menu:
        "\"The ends don't justify the means. Not ever.\"":
            jump scene2_ends_means
        "\"It's a genuine tradeoff. I don't know the answer.\"":
            jump scene2_tradeoff


label scene2_nuance:
    m "NUANCE! Finally!"

    "He jumps up excitedly."

    m "Yes! Not all alterations are equal. Let me categorize:"

    "He starts ticking off fingers."

    m "Alcohol: lowers inhibitions, impairs motor function, increases aggression. Probably bad for decisions."

    m "Cannabis: alters time perception, enhances pattern recognition, reduces anxiety. Mixed bag."

    m "Ketamine at therapeutic doses: quiets default mode network, reduces ego fixation, enables novel connections. I'd argue GOOD for certain decisions."

    m "Psychedelics: profound but unpredictable. I use rarely."

    "He looks at you earnestly."

    m "The blanket term 'drugs' obscures these distinctions. Does that change your view?"

    menu:
        "\"It's a fair point. But who decides which alterations are 'acceptable'?\"":
            jump scene2_who_decides
        "\"You're rationalizing. An addict could make the same argument.\"":
            jump scene2_rationalizing


label scene2_normal:
    "He BEAMS."

    m "NOW we're getting somewhere! What IS normal consciousness? A specific mix of neurotransmitters that evolution optimized for savanna survival? Why would THAT be optimal for designing spacecraft?"

    "He begins pacing rapidly."

    m "'Normal' consciousness evolved to find food, avoid predators, and reproduce. It generates anxiety because anxiety kept us alive. It creates tribalism because tribes outcompeted loners."

    m "But we don't live on the savanna anymore. Maybe 'normal' is now MALADAPTIVE. Maybe engineering consciousness is as valid as engineering bridges."

    "He stops."

    m "Or maybe I'm just a junkie with good PR. That's the terrifying part. How do I KNOW which it is?"

    menu:
        "\"External verification. Get sober people to review your ideas.\"":
            jump scene2_verification
        "\"You can't know. That's why this is dangerous.\"":
            jump scene2_danger


# Scene 2 deeper branches

label scene2_two_wrongs:
    m "Ah, the reformer's position. Fix everything, then judge me."

    "He laughs, but kindly."

    m "I admire the consistency. But reform takes time we may not have. While you're fixing sleep schedules for presidents, the asteroid is coming. Or the pandemic. Or the AI uprising."

    "He sits back down."

    m "I'm not PROUD of my methods. I'm PRACTICAL. If there were a better way to operate at this speed, I'd take it. But there isn't. Not that I've found."

    "His voice softens."

    m "Though maybe I haven't looked hard enough. Maybe that's what you're here to show me."

    menu:
        "Proceed to the final reckoning":
            jump scene3_start


label scene2_choice:
    m "Choice versus circumstance."

    "He nods gravely."

    m "Yes. I CHOOSE this. Does that make it worse? Or does intention matter?"

    "He's quiet for a moment."

    m "When I started, I didn't need anything. I was already successful. But I hit a wall - the same ideas, cycling. My brain became an echo chamber."

    m "The first time I tried ketamine, in a clinical setting, I had three ideas that became three companies worth billions. Coincidence? Maybe."

    m "Now I can't tell if the ketamine expands my mind or if I've just become dependent. The line between tool and crutch blurs."

    "His vulnerability is startling."

    menu:
        "Proceed to confront this honestly":
            jump scene3_start


label scene2_ends_means:
    m "Never? NEVER?"

    "He leans forward."

    m "What if the alternative is extinction? If compromising ethics saves humanity, isn't refusing to compromise the truly unethical choice?"

    "He's genuinely wrestling with this."

    m "I tell myself I'm building a future. But sometimes I wonder if I'm just building monuments to my ego. How do I know the difference?"

    m "Maybe that's why I take ketamine. To escape myself long enough to see clearly. Or maybe I'm just hiding."

    "The conversation has become raw."

    menu:
        "Continue to the final scene":
            jump scene3_start


label scene2_tradeoff:
    m "You don't know. I don't know. Nobody knows."

    "He laughs bitterly."

    m "We're all gambling with the future based on incomplete information. The difference is I'm gambling bigger. Is that courage or arrogance?"

    "He looks at his hands."

    m "847 people can move who couldn't before. Twelve people died in trials to get there. Is that acceptable? I don't know. I'll never know. I just keep moving forward and hope the calculus works out."

    m "Maybe that's all anyone can do."

    menu:
        "Move to the final confrontation":
            jump scene3_start


label scene2_who_decides:
    m "Who decides? That's THE question."

    "He nods vigorously."

    m "Right now, I decide for myself. But I'm affecting millions. Should they have a say in my neurochemistry? Should there be a 'fit for duty' test for billionaires?"

    "He actually seems to consider this seriously."

    m "I'd submit to oversight, honestly, if I trusted the overseers. But regulators are captured by industries. Politicians are bought. The public is manipulated by algorithms."

    m "Who can I trust to judge my consciousness who isn't also compromised?"

    "His loneliness is palpable."

    menu:
        "Proceed to the conclusion":
            jump scene3_start


label scene2_rationalizing:
    "He flinches like you've struck him."

    m "An addict."

    "He breathes out slowly."

    m "Yes. That word has crossed my mind. Usually at 3 AM when the K wears off and the existential dread returns."

    m "I've done the addiction assessments. I score borderline. Not dependent enough for clinical addiction, not healthy enough for casual use."

    "He looks at you with something like desperation."

    m "If I'm an addict, everything I've built is tainted. If I'm not, I'm a pioneer. The difference might be semantic."

    m "How do YOU distinguish vision from delusion, [player_name]?"

    menu:
        "Face the final question together":
            jump scene3_start


label scene2_verification:
    m "External verification!"

    "He claps."

    m "SOCRATES, did you hear that? The human suggests I verify my ideas with sober humans."

    s "MELON, 73.2%% OF YOUR K-SPACE IDEAS ARE REJECTED BY THE SOBER REVIEW BOARD. 8.1%% BECOME MAJOR PRODUCTS."

    "He spreads his hands."

    m "There you go. Most of my high ideas are garbage. But 8%% change the world. Do we throw out the 8%% to avoid the 92%%?"

    "He seems genuinely uncertain."

    m "Or is 8%% just what you'd expect from random variation?"

    menu:
        "Time for the final reckoning":
            jump scene3_start


label scene2_danger:
    m "I can't know."

    "He slumps."

    m "The honest answer. Maybe I'm a visionary. Maybe I'm a cautionary tale future generations will tell."

    m "I've tried to build safeguards. SOCRATES. The review board. My own written rules for what I can and can't do while altered."

    m "But safeguards only work if I follow them. And I've broken every one at some point."

    "He looks at you."

    m "What if the safeguard should be... stopping? What if I should just... stop?"

    "The question hangs heavy in the air."

    menu:
        "Proceed to the final decision":
            jump scene3_start


# ==================== SCENE 3: THE VISION AND FINAL RECKONING ====================

label scene3_start:
    scene bg_vision_chamber_candles
    with fade

    "SCENE 3: THE VISION AND FINAL RECKONING"

    "The candles have burned low. Melon Husk looks exhausted, more human than you've seen him all day. The monitors around the room show his biometrics returning to baseline."

    show melon vulnerable at right
    with dissolve

    m "Before you go, [player_name], I want to show you something. Something I've never shown anyone outside my inner circle."

    "He presses a sequence on his tablet, and the room transforms. Holographic projections surround you - a vision of Mars, but not as it is. As he imagines it: domed cities, children playing in artificial gardens, humanity thriving on a new world."

    m "This is why I do what I do. All of it. The rockets, the tunnels, the neural links. Even the ketamine. All paths lead here."

    "He turns to you."

    m "You've spent a day challenging me. Now I need you to answer honestly: After everything you've seen, what do you think of my vision - and my method?"

    menu:
        "\"The vision is beautiful. The method is still troubling.\"":
            jump scene3_beautiful_troubling
        "\"I think you're brilliant but need help. Not in a condescending way.\"":
            jump scene3_need_help
        "\"I don't know anymore. You've shaken my certainties.\"":
            jump scene3_shaken
        "\"The vision doesn't justify the risk. You're gambling with too much.\"":
            jump scene3_gambling


label scene3_beautiful_troubling:
    "He nods slowly, something like respect in his eyes."

    m "Troubling. Yes. It troubles me too, when I'm sober enough to feel it."

    "He walks through his holographic Mars, hand passing through a projected child."

    m "What would you have me do, [player_name]? Stop the substances and lose whatever edge they provide? Continue and risk everything on a potentially impaired judgment?"

    m "Or is there a middle path you see that I don't?"

    menu:
        "\"Reduce reliance gradually. Build systems that don't depend on your K-state.\"":
            jump scene3_gradual
        "\"Keep going but be more honest publicly about your methods.\"":
            jump scene3_honest
        "\"I genuinely don't know what to advise.\"":
            jump scene3_no_advice


label scene3_need_help:
    "He laughs - but it's not defensive. It's almost relieved."

    m "Need help. When's the last time anyone said that to me without wanting something? Without trying to manipulate me?"

    "He looks at the Mars projection."

    m "I've surrounded myself with yes-men. People who tell me what I want to hear because I sign their paychecks. SOCRATES tries to check me, but AI doesn't have... whatever YOU have."

    "He faces you directly."

    m "Will you help me, [player_name]? Be a voice that challenges me? I could use someone who isn't afraid to say 'this is a bad idea'."

    menu:
        "\"I'd consider it. But I won't enable substance use.\"":
            jump scene3_conditions
        "\"That's not my place. But I can point you toward professionals.\"":
            jump scene3_professionals


label scene3_shaken:
    m "I've shaken your certainties?"

    "He smiles sadly."

    m "Welcome to my world. Certainty is a luxury I lost years ago."

    "He shuts down the Mars projection. The room returns to normal - just a rich man's office, fancy but mundane."

    m "Maybe that's the real answer. Nobody knows. I don't know if I'm a visionary or a cautionary tale. You don't know if my methods are genius or madness."

    m "Maybe the best we can do is keep questioning. Keep each other honest."

    "He extends his hand."

    m "Thank you, [player_name]. For questioning me. It's the most useful thing anyone's done for me in months."

    menu:
        "Shake his hand and part as uncertain allies":
            jump ending_philosophical
        "Shake his hand but maintain critical distance":
            jump ending_neutral


label scene3_gambling:
    "His face hardens slightly, then softens."

    m "Gambling. Yes. But the alternative is certainty of extinction, isn't it? If we stay on Earth, doing things the 'safe' way, eventually something kills us. Certainty."

    m "My gamble at least has a CHANCE of success."

    "But he looks uncertain."

    m "Unless you're right. Unless the gamble itself introduces risks that exceed what I'm trying to prevent. The cure worse than the disease."

    "He looks at you intensely."

    m "If you truly believe that, will you try to stop me?"

    menu:
        "\"Not stop you. But I'll be a critical voice.\"":
            jump scene3_critical_voice
        "\"I'll oppose any decision I think endangers humanity.\"":
            jump scene3_oppose
        "\"No. It's your life, your choice. I just needed you to hear the concern.\"":
            jump scene3_your_choice


# Final branches before endings

label scene3_gradual:
    m "Gradual reduction."

    "He considers this."

    m "SOCRATES has suggested the same. Taper down, build redundancy, train successors who can operate sober."

    "He pulls up his calendar - packed with meetings, launches, decisions."

    m "It would slow everything down. Years, maybe. More time for asteroids to find us, pandemics to evolve."

    m "But maybe haste is its own risk. Maybe building sustainable systems is better than building fast, fragile ones."

    "He looks at you with something like hope."

    m "Would you check in on me, [player_name]? Periodically? To see if I'm keeping to a better path?"

    menu:
        "\"Yes. I'll hold you accountable.\"":
            jump ending_good
        "\"I don't think that's my role, but I wish you well.\"":
            jump ending_neutral


label scene3_honest:
    m "Honesty."

    "He frowns."

    m "Go public about the ketamine? The stock price would crater. Regulators would investigate. My enemies would feast."

    "He paces."

    m "But... lies compound. Every secret I keep becomes a weapon someone can use against me. Maybe radical honesty is the better strategy."

    m "Or maybe it's naive. I don't know."

    "He looks at you."

    m "Would the public accept an openly psychedelic-using billionaire shaping their future? Or would they burn me at the stake?"

    menu:
        "\"Some would reject you. Others might respect the honesty. It's a risk.\"":
            jump ending_neutral
        "\"I think honesty is always better, whatever the consequences.\"":
            jump ending_philosophical


label scene3_no_advice:
    m "No advice."

    "He nods."

    m "The honest answer. I appreciate that more than you know."

    "He shuts down the holograms and sits heavily in a chair."

    m "Everyone has advice for me. Do this, don't do that. Take this drug, stop that drug. You're the first person in years to say 'I don't know.'"

    m "Maybe the best gift you can give me is that uncertainty. A reminder that nobody has the answers, even me."

    "He smiles tiredly."

    m "Especially me."

    menu:
        "Leave him to his uncertainty":
            jump ending_philosophical


label scene3_conditions:
    m "Conditions. Boundaries. You set TERMS."

    "He sounds almost delighted."

    m "Nobody sets terms with me anymore. I've missed it."

    "He walks to his desk and pulls out a paper notebook - old school."

    m "Write them down. Your conditions. I'll sign them, have SOCRATES hold me accountable."

    "He hands you the pen."

    m "Make me be better, [player_name]. Please."

    menu:
        "Write reasonable conditions and agree to help":
            jump ending_good
        "This is too much responsibility. Decline.":
            jump ending_neutral


label scene3_professionals:
    m "Professionals."

    "His voice flattens."

    m "Therapists, doctors, addiction specialists. I've seen them. They see dollar signs or research papers. They don't see ME."

    "He sighs."

    m "But you're right. It's not your responsibility to fix me. I'm sorry for asking. It was unfair."

    "He seems to shrink a little."

    m "Thank you for your time today, [player_name]. It meant more than you know."

    menu:
        "Leave with compassion but appropriate boundaries":
            jump ending_neutral


label scene3_critical_voice:
    m "A critical voice. Not trying to stop me, but to question me."

    "He nods slowly."

    m "That might be exactly what I need. SOCRATES does it, but AI lacks... skin in the game."

    "He extends his hand."

    m "I'll give you a direct line. Whenever I'm about to make a major decision, you'll have the chance to challenge me. No obligation. Just... access."

    m "Will you accept?"

    menu:
        "Accept the responsibility":
            jump ending_good
        "Decline - too much power, too much burden":
            jump ending_neutral


label scene3_oppose:
    "His expression goes cold, then thoughtful."

    m "Oppose me. Well. At least you're honest."

    "He walks to the window, looking out at his rockets."

    m "I've had opponents before. Regulators, rivals, ex-wives. You'd be different - a principled opponent, not a self-interested one."

    "He turns back to you."

    m "I respect that, [player_name]. I won't make it easy for you. But I respect it."

    "The warmth between you has chilled."

    menu:
        "Leave as adversaries, but with mutual understanding":
            jump ending_neutral


label scene3_your_choice:
    m "My choice."

    "He seems both relieved and disappointed."

    m "Yes. Ultimately, it is. No one can stop me. I have more resources than most governments."

    "He looks at the Mars projection one last time before shutting it down."

    m "Thank you for your concern, genuinely. But I think we both know nothing changes tonight. I'll keep doing what I do. You'll keep having doubts."

    "He walks you to the door."

    m "Maybe that's all any of us can do. Try, doubt, and hope we're not the villain in someone else's story."

    menu:
        "Leave with the weight of unanswered questions":
            jump ending_philosophical


# ==================== ENDINGS ====================

label ending_good:
    hide melon
    scene bg_desert_dawn
    with fade

    "You leave the SpaceZ facility as dawn breaks over the Texas desert. Your phone already has a message from SOCRATES:"

    s "WELCOME TO THE OVERSIGHT COMMITTEE, [player_name]."

    "In the months that follow, you become an unlikely voice in Melon Husk's empire - challenging, questioning, occasionally talking him down from K-fueled flights of fancy. His drug use decreases, not to zero, but to something more managed."

    "Mars colonies may still come. But now they'll be built with more than one man's visions and chemicals. They'll be built with questions."

    "Maybe that's the best any of us can do: ensure that the people shaping our future have to answer to someone. Even if that someone doesn't have all the answers either."

    "The ketamine question remains unanswered. Perhaps that IS the answer."

    centered "{size=+5}ENDING: THE BALANCED PATH{/size}"
    "You found wisdom in questioning both vision and method."

    jump game_end


label ending_neutral:
    hide melon
    scene bg_desert_dawn
    with fade

    "You leave the SpaceZ facility as dawn breaks over the Texas desert. Melon Husk watches from his window, a small figure against the vast machines that embody his ambition."

    "You don't join his circle. You don't oppose him. You return to your life, but you're changed. The questions he raised - about consciousness, about progress, about the ethics of altering minds to alter futures - stay with you."

    "In the years that follow, you watch his launches, his announcements, his controversies. Sometimes he seems brilliant; sometimes dangerously unhinged. You can never quite tell which."

    "Maybe that's the point. Maybe genius and madness share a border so thin that even the people living there can't tell which side they're on."

    "You made no difference today. But you bear witness. That has to count for something."

    centered "{size=+5}ENDING: THE OBSERVER{/size}"
    "You watched history unfold, neither shaping nor shaped."

    jump game_end


label ending_philosophical:
    hide melon
    scene bg_desert_dawn
    with fade

    "You leave the SpaceZ facility as dawn breaks over the Texas desert. Neither ally nor enemy, neither convert nor critic - just someone who spent a day in the presence of a question mark shaped like a man."

    "Is it wise to get ideas about humanity's future while high? You still don't know. But now you understand that the question itself is more valuable than any easy answer."

    "Socrates - the real one - said the unexamined life is not worth living. Melon Husk examines his life compulsively, chemically, obsessively. Too much? Too little? The wrong way? The right way?"

    "All you know is that the future will be shaped by people who are certain, and maybe it shouldn't be. Maybe what humanity needs isn't better answers but better questions."

    "You asked questions today. That's enough. That has to be enough."

    "The rest is silence - and the distant roar of rockets, reaching for stars that don't care how sober we were when we dreamed of them."

    centered "{size=+5}ENDING: THE SOCRATIC WAY{/size}"
    "The questions matter more than the answers."

    jump game_end


label ending_bad:
    hide melon
    scene bg_desert_dawn
    with fade

    "You leave the SpaceZ facility as dawn breaks over the Texas desert. Something in you has shifted - not broken, exactly, but bent."

    "Melon Husk was persuasive. Too persuasive. You find yourself thinking: maybe he's right. Maybe consciousness should be engineered. Maybe the future SHOULD be built by chemically-enhanced visionaries who see further than the rest of us."

    "In the weeks that follow, you seek out your own experiments. Small doses at first. Then larger. You're not building rockets, but you're THINKING bigger. Aren't you? The ideas feel profound. They must be profound."

    "This is how it starts. Not with villainy, but with curiosity. Not with corruption, but with questions. You wanted to understand Melon Husk."

    "Now you're becoming him."

    "Some doors, once opened, cannot be closed."

    centered "{size=+5}ENDING: THE UNEXAMINED LIFE{/size}"
    "Some doors, once opened, cannot be closed."

    jump game_end


label ending_transcendent:
    hide melon
    scene bg_desert_dawn
    with fade

    "You leave the SpaceZ facility as dawn breaks over the Texas desert, but 'leaving' feels like the wrong word. Part of you stays. Part of you was always there."

    "The conversation with Melon Husk opened something - not a door exactly, more like a crack in the ordinary. Through it, you glimpsed what he sees: the vast indifference of the universe, the fragility of consciousness, the strange miracle that anything exists at all."

    "You don't need ketamine to see it now. Once seen, it can't be unseen."

    "Humanity will go to the stars, or it won't. Melon Husk will be remembered as a visionary, or a warning. None of it matters in the way you once thought things mattered."

    "And somehow, that's beautiful. The not-mattering is the mattering."

    "You walk into the desert sunrise, carrying questions that have no answers, and finding that enough."

    "More than enough."

    centered "{size=+5}ENDING: BEYOND THE VEIL{/size}"
    "Some truths can only be glimpsed, never grasped."

    jump game_end


label game_end:
    centered "{size=+3}Thank you for playing THE VISIONARY{/size}"
    "A game about consciousness, altered states, and human destiny"

    menu:
        "Play again":
            jump start
        "Quit":
            return
