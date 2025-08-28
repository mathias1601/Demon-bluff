import React from 'react'
import '../styles/cardOverview.css'

type CardInfo = {
	cardName: string,
	cardDescription: string,
	cardHint: string,
}

interface Props {
	allPresentCards: CardInfo[]
}

const CardOverview = ({ allPresentCards }: Props) => {

	const displayCards = allPresentCards.map((card, index) => (
		<div key={index} className='cardOverviewDisplay'>
			<p
				style={{
					paddingBottom: "10px",
				}}
			>
				{card.cardName}
			</p>
			<p
				style={{
					paddingBottom: "10px",
				}}
			>
				{card.cardDescription}
			</p>
			<p>{card.cardHint}</p>
		</div>
	))

	return (
		<div>
			<p>Present cards:</p>
			<div
				className="grid grid-cols-8 gap-x-50 gap-y-0"
				style={{
					width: "1300px",
				}}
			>
				{displayCards}
			</div >
		</div>
	)
}

export default CardOverview