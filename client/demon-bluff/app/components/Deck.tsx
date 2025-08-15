'use client'
import React, { useState } from 'react'
import Card from './Card';

type CardType = {
	positionIndex: number,
	name: string,
	reveal: string,
	usage: number,
	isRevealed: boolean,
}

const Deck = () => {
	const radius = 500; // distance from center

	const [currentDeck, setCurrentDeck] = useState<CardType[]>([]);
	const [deckCreated, setDeckCreated] = useState<boolean>(false);
	const [error, setError] = useState<any>(null);

	// Selection mode state
	const [selectMode, setSelectMode] = useState(false);
	const [actionCardIndex, setActionCardIndex] = useState<number | null>(null);
	const [requiredSelections, setRequiredSelections] = useState(0);
	const [selectedCards, setSelectedCards] = useState<number[]>([]);

	async function createDeck() {
		setError(null);
		setDeckCreated(true);
		try {
			const res = await fetch('http://localhost:8000/create-deck', { method: 'POST' });
			const data = await res.json();
			if (res.ok) {
				setCurrentDeck(data.deck);
			} else {
				setError(data.error || 'Failed to create deck');
			}
		} catch (e) {
			setError('Network error');
		}
	}

	const revealCard = (index: number) => {
		const card = currentDeck[index];

		// If already revealed and has usage → enter selection mode
		if (card.isRevealed && card.usage > 0) {
			startSelectMode(index, card.usage);
			return;
		}

		// Reveal the card
		setCurrentDeck(prevDeck =>
			prevDeck.map((c, i) =>
				i === index ? { ...c, isRevealed: true } : c
			)
		);
	};

	const startSelectMode = (cardIndex: number, usage: number) => {
		setSelectMode(true);
		setActionCardIndex(cardIndex);
		setRequiredSelections(usage);
		setSelectedCards([]);
	};

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
		console.log("Card use result:", data.result);
	}

	return (
		<div>
			<div style={{ padding: 20 }}>
				<h1>Game Deck</h1>

				{!deckCreated ? (
					<button onClick={createDeck}>Create Deck</button>
				) : (
					<div>
						<p>Deck created with {currentDeck.length} cards</p>
					</div>
				)}

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
							onClick={() =>
								selectMode
									? toggleTargetSelection(card.positionIndex)
									: revealCard(card.positionIndex)
							}
						>
							<Card
								positionIndex={card.positionIndex}
								name={card.name}
								reveal={card.reveal}
								usage={card.usage}
								isRevealed={card.isRevealed}
								x={x}
								y={y}
								isSelected={selectedCards.includes(card.positionIndex)}
							/>
						</div>
					);
				})}
			</div>
		</div>
	);
}

export default Deck;