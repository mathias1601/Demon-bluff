'use client'
import React, { useState } from 'react'
import "../styles/card.css"

interface Props {
	positionIndex: number,
	name: string,
	reveal: string,
	usage: number,
	usageResult: string | null,
	isRevealed: boolean,
	x: number,
	y: number,
	isSelected: boolean,
	isExecuted: boolean,
}

const Card = ({ positionIndex, name, reveal, usage, usageResult, isRevealed, x, y, isSelected, isExecuted }: Props) => {
	
	return (
		<div>
			<div
				className={`card-container ${isRevealed ? "flipped" : ""}`}
				style={{
					position: "absolute",
					left: `${x}px`,
					top: `${y}px`,
					cursor: "pointer",
				}}
			>	
			<div className='card'>
				<div 
					style={{
						border: isSelected ? "3px solid red" : "2px solid #333",
						background: isExecuted ? "red" : "#444"
					}} 
					className="card-front"
				>
          #{positionIndex}
        </div>
        <div 
					style={
						{
							border: isSelected ? "3px solid red" : "2px solid #333",
							background: isExecuted ? "red" : "#fafafa",
						}} 
					className="card-back"
				>
					<h3>#{positionIndex}</h3>
          <h3>{name}</h3>
          {reveal && <p>{reveal}</p>}
					{usageResult && <p>{usageResult}</p>}
          {usage > 0 && <p>!</p>}
        </div>
			</div>
			</div>
		</div>
	)
}

export default Card