'use client'
import React, { useEffect, useState } from 'react'
import Card from './Card';
import '../styles/deck.css'
import { faSkull } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';


type CardType = {
	positionIndex: number,
	name: string,
	reveal: string,
	usage: number,
	usageResult: string | null,
	isRevealed: boolean,
	isEvil: boolean,
	executeEffect: number
}

interface Props {
	level: number
	quit: () => void
}

const Deck = ({ level, quit }: Props) => {
	const radius = 500; // distance from center

	const maxHealth = 10;
	const [currentHealth, setCurrentHealth] = useState<number>(maxHealth);
	const [evilCount, setEvilCount] = useState<number>(0);
	const [evilsExecuted, setEvilsExecuted] = useState<number>(0);

	const [currentDeck, setCurrentDeck] = useState<CardType[]>([]);
	const [deckCreated, setDeckCreated] = useState<boolean>(false);
	const [error, setError] = useState<any>(null);

	// Selection mode state
	const [selectMode, setSelectMode] = useState<boolean>(false);
	const [actionCardIndex, setActionCardIndex] = useState<number | null>(null);
	const [requiredSelections, setRequiredSelections] = useState(0);
	const [selectedCards, setSelectedCards] = useState<number[]>([]);

	// Execution mode state
	const [executionMode, setExecutionMode] = useState<boolean>(false);
	const [executedCards, setExecutedCards] = useState<number[]>([]);


	useEffect(() => {
		createDeck()
	}, [])

	async function createDeck() {
		setError(null);
		setDeckCreated(true);
		try {
			const res = await fetch(`http://localhost:8000/create-deck/${level}`, { method: 'POST' });
			const data = await res.json();
			console.log(data.deck)
			if (res.ok) {
				setCurrentDeck(data.deck);
				setEvilCount(data.evilCount)
			} else {
				setError(data.error || 'Failed to create deck');
			}
		} catch (e) {
			setError('Network error');
		}
	}

	const revealCard = (index: number) => {

		// Reveal the card
		setCurrentDeck(prevDeck =>
			prevDeck.map((card, i) =>
				i === index ? { ...card, isRevealed: true } : card
			)
		);
	};

	const startSelectMode = (cardIndex: number, usage: number) => {
		if (usage !== 0) {
			setSelectMode(true);
			setActionCardIndex(cardIndex);
			setRequiredSelections(usage);
			setSelectedCards([]);
			setCurrentDeck(prevDeck =>
				prevDeck.map((card, i) =>
					i === cardIndex ? { ...card, usage: 0 } : card
				)
			);
		}
	};

	const toggleExecution = (index: number) => {

		// Execute evil
		if (!executedCards.includes(index) && currentDeck[index].executeEffect == -1) {
			setExecutedCards(prev => [...prev, index])
			setEvilsExecuted(evilsExecuted + 1)
		}

		// Execute innocent
		else if (!executedCards.includes(index) && currentDeck[index].executeEffect !== 0) {
			setExecutedCards(prev => [...prev, index])
			setCurrentHealth(currentHealth + currentDeck[index].executeEffect)

		}
	}

	const toggleTargetSelection = (index: number) => {

		if (!selectMode) return;

		setSelectedCards(prev => {
			if (prev.includes(index)) {
				return prev.filter(i => i !== index); // Deselect
			}
			if (prev.length >= requiredSelections) {
				return prev; // Can't select more
			}
			return [...prev, index];
		});
	};

	// Check when selection is complete
	if (selectMode && selectedCards.length === requiredSelections) {
		if (actionCardIndex !== null) {
			fetchUseCard(selectedCards, actionCardIndex);
		}
		// Reset mode
		setSelectMode(false);
		setActionCardIndex(null);
		setRequiredSelections(0);
		setSelectedCards([]);
	}


	async function fetchUseCard(targets: number[], cardIndex: number) {
		const res = await fetch("http://localhost:8000/use-card", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ cardIndex: cardIndex, targets }),
		});

		if (!res.ok) {
			console.error("Failed to use card");
			return;
		}

		const data = await res.json();
		setCurrentDeck(prevDeck =>
			prevDeck.map((card, i) =>
				i === cardIndex ? { ...card, usageResult: data.usageResult } : card
			)
		);

	}



	const handleCardClick = (cardIndex: number) => {
		const card = currentDeck[cardIndex]

		if (executionMode) {
			toggleExecution(cardIndex)
			revealCard(cardIndex)
		}
		else if (selectMode) {
			toggleTargetSelection(cardIndex)
		}
		else if (!card.isRevealed) {
			revealCard(cardIndex);
		}
		else {
			startSelectMode(cardIndex, card.usage)
		}
	};

	// For css-styling
	const getHeartLevel = () => {
		if (currentHealth <= 2) return "level-1";
		if (currentHealth <= 5) return "level-2";
		if (currentHealth < 8) return "level-3";
		return "level-4";
	};

	return (
		<div>
			<div style={{ padding: 20 }}>
				<div>
					<button onClick={quit} className='backButton'></button>
					<h1>Level {level}</h1>
				</div>
				<div
					className={`heart ${getHeartLevel()}`}
				>
					<div className='heart-text'>Health: {currentHealth}/{maxHealth}</div>
				</div>
				<p>Evils executed: {evilsExecuted}/{evilCount}</p>

				{selectMode && (
					<div style={{ marginTop: "10px", color: "blue" }}>
						Selecting {requiredSelections} target(s) for card #{actionCardIndex}
						<button
							style={{ marginLeft: "10px" }}
							onClick={() => {
								setSelectMode(false);
								setActionCardIndex(null);
								setRequiredSelections(0);
								setSelectedCards([]);
							}}
						>
							Cancel
						</button>
					</div>
				)}

				<div>
					<button className='executeButton' onClick={() => { setExecutionMode(!executionMode); setSelectMode(false) }} >Execute <FontAwesomeIcon icon={faSkull} /></button>
					{executionMode && (
						<div style={{ marginTop: "10px", color: "blue" }}>
							Selecting target to execute
							<button
								style={{ marginLeft: "10px" }}
								onClick={() => {
									setExecutionMode(false);
								}}
							>
								Cancel
							</button>
						</div>
					)}
				</div>
			</div>

			<div
				style={{
					position: "relative",
					width: `${radius * 2 + 100}px`,
					height: `${radius * 2 + 100}px`,
					margin: "50px auto",
				}}
			>
				{currentDeck.map((card) => {
					const angle = (card.positionIndex / currentDeck.length) * 2 * Math.PI - Math.PI / 2;
					const x = radius * Math.cos(angle) + radius;
					const y = radius * Math.sin(angle) + radius;

					return (
						<div
							key={card.positionIndex}
							onClick={() => handleCardClick(card.positionIndex)}
						>
							<Card
								positionIndex={card.positionIndex}
								name={card.name}
								reveal={card.reveal}
								usage={card.usage}
								isRevealed={card.isRevealed}
								x={x}
								y={y}
								usageResult={card.usageResult}
								isSelected={selectedCards.includes(card.positionIndex)}
								isExecuted={executedCards.includes(card.positionIndex)} />

						</div>
					);
				})}
			</div>
		</div>
	);
}

export default Deck;