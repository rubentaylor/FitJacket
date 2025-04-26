<script lang="ts">
    import { modal, ModalType } from "$lib/shared/modals.svelte";

    let { data } = $props();
    let receivedMessages = $derived(data.receivedMessages.results);
    let sentMessages = $derived(data.sentMessages.results);

    function handleOpenMessage(message: any) {
        modal.setModal(ModalType.MESSAGE);
        modal.setPayload(message);    
    }
</script>

<div class="flex flex-col gap-y-6">
    <h2>Messages</h2>

    <div class="flex flex-col gap-y-3">
        <h4>Received</h4>
        {#if receivedMessages && receivedMessages.length > 0}
            <div class="flex flex-col gap-y-4">
                {#each receivedMessages as message}
                    <button onclick={() => handleOpenMessage(message)} class="p-4 {message.viewed ? "bg-neutral-100" : "bg-white"}  rounded shadow flex flex-col gap-y-2 text-start">
                        <div class="flex justify-between items-start">
                            <div class="flex items-center gap-x-2">
                                <div class="flex flex-col">
                                    <h6>{message.senderData.username}</h6>
                                    <p class="text-xs">{message.senderData.email}</p>
                                </div>
                            </div>
                            <p>{new Date(message.created_at).toLocaleString()}</p>
                        </div>
                        <p class="line-clamp-1">{message.text}</p>
                    </button>
                {/each}
            </div>
        {:else}
            <p >You don't have any messages yet.</p>
        {/if}
    </div>

    <div class="flex flex-col gap-y-3">
        <h4>Sent</h4>
        {#if sentMessages && sentMessages.length > 0}
            <div class="flex flex-col gap-y-4">
                {#each sentMessages as message}
                    <button onclick={() => handleOpenMessage(message)} class="p-4 {message.viewed ? "bg-neutral-100" : "bg-white"}  rounded shadow flex flex-col gap-y-2 text-start">
                        <div class="flex justify-between items-start">
                            <div class="flex items-center gap-x-2">
                                <div class="flex flex-col">
                                    <h6>{message.receiverData.username}</h6>
                                    <p class="text-xs">{message.receiverData.email}</p>
                                </div>
                            </div>
                            <p>{new Date(message.created_at).toLocaleString(undefined, {
                                year: 'numeric',
                                month: 'short',
                                day: 'numeric',
                                hour: '2-digit',
                                minute: '2-digit'
                            })}</p>
                        </div>
                        <p class="line-clamp-1">{message.text}</p>
                    </button>
                {/each}
            </div>
        {:else}
            <p >You don't have any messages yet.</p>
        {/if}
    </div>
</div>