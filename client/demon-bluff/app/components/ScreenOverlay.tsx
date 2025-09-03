import React from 'react'
import '../styles/overlay.css'

interface Props {
	win: Boolean
	isOpen: boolean
	onClose: () => void
	children: any
}

const ScreenOverlay = ({ win, isOpen, onClose, children }: Props) => {

	return (
		<>
			{isOpen ?
				<div className='overlay'>
					<div className='overlay_background' onClick={onClose} />
					<div className='overlay_container'>
						<div className='overlay_controls'>
							<button className='overlay_close' type='button' onClick={onClose} />
						</div>
						<div>
							{win ?
								<div>
									<h1>Congratulations!</h1>
									<p>You have slain all Evil characters!</p>
								</div>
								:
								<div>
									<h1>Game over</h1>
								</div>
							}
						</div>
						{children}
					</div>
				</div>
				: null
			}
		</>
	)
}

export default ScreenOverlay