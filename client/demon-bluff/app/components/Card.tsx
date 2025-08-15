'use client'
import React, { useState } from 'react'

interface Props {
	positionIndex: number,
	name: string,
	reveal: string,
	usage: number,
	isRevealed: boolean,
	x: number,
	y: number,
	isSelected: boolean,
}

const Card = ({ positionIndex, name, reveal, usage, isRevealed, x, y, isSelected }: Props) => {

	return (
		<div>
			<div
				style={{
					position: "absolute",
					left: `${x}px`,
					top: `${y}px`,
					width: "200px",
					height: "300px",
					backgroundColor: "#fff",
					borderRadius: "8px",
					display: "flex",
					alignItems: "center",
					justifyContent: "center",
					transform: "translate(-50%, -50%)",
					boxShadow: "0 2px 6px rgba(0,0,0,0.2)",
					border: isSelected ? "3px solid green" : "1px solid black",
					cursor: "pointer",
				}}
			>
				{isRevealed
					?
					<div>
						<div>
							<div>#{positionIndex}</div>
							{name}
						</div>
						<div>
							{reveal}
						</div>
					</div>
					:
					null
				}
			</div>
		</div>
	)
}

export default Card