export enum ModalType {
	NONE = 'NONE',
	MESSAGE = 'MESSAGE',
	CREATE_EVENT = 'CREATE_EVENT',
	CREATE_CHALLENGE = 'CREATE_CHALLENGE'
}

export let modal = $state({
	type: ModalType.NONE,
	payload: null,

	setModal(modal: ModalType) {
		this.type = modal;
	},

	setPayload(payload: any) {
		this.payload = payload;
	},

	close() {
		this.type = ModalType.NONE;
	}
});
