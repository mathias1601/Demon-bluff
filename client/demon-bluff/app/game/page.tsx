'use client'
import { use, useState } from 'react';
import Deck from '../components/Deck';
import '../styles/gamePage.css'

export default function Game() {

	const maxLevel = 2
	const [currentLevel, setCurrentLevel] = useState<number>(0);
	const [deckChosen, setDeckChosen] = useState<boolean>(false);


	const allLevels =
		Array.from({ length: maxLevel }).map((_, index) => (
			<div className='grid grid-cols-8' key={index} onClick={() => { setCurrentLevel(index), setDeckChosen(true) }}>
				<div className='levelContainer'>Level {index}</div>
			</div>
		))


	return (
		<div>
			{deckChosen
				?
				<Deck level={currentLevel} quit={() => setDeckChosen(false)} />

				:
				<div>
					<p>Choose a level:</p>
					{allLevels}
				</div>
			}

		</div>
	);
}