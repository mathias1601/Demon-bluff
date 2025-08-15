'use client'
import { useState } from 'react';
import Deck from '../components/Deck';

type Card = {
	positionIndex: number,
	name: string,
	reveal: string,
	usage: number,
	isRevealed: boolean,
}

export default function Game() {

	return (
		<Deck />
	);
}