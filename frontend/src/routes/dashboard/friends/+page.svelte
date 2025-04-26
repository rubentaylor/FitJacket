<script lang="ts">
    import { auth } from "$lib/shared/auth.svelte";
    let { data } = $props();
    let friends = $derived(data.friends.results);
    let friendRequests = $derived(data.friendRequests.results);
</script>

<div class="flex flex-col gap-y-6 h-full">
    <h2>Friends</h2>

    <div class="flex w-full justify-between gap-6 h-full">
        <div class="p-4 bg-white shadow rounded w-2/3 overflow-y-auto">
            <div class="w-full flex flex-col max-h-full">
                {#if friends.length > 0}
                    {#each friends as friend, i}
                        <div class="flex w-full items-center">
                            <div class="flex justify-between w-full items-center">
                                <div>
                                    <h6>{friend.user_id1 != auth.user.id ? friend.user_id1_details.username : friend.user_id2_details.username}</h6>
                                    <p class="text-xs">{friend.user_id1 != auth.user.id ? friend.user_id1_details.email : friend.user_id2_details.email}</p>
                                </div>
                                <div class="flex gap-x-3">
                                    <a href={`/dashboard/messages/create`} 
                                        class="btn-primary h-8">
                                        Message
                                    </a>
                                    <button class="btn-secondary h-8">
                                        View Profile
                                    </button>
                                </div>
                            </div>
                        </div>
                        <hr class="my-4"/>                            
                    {/each}
                {:else}
                    <p>You don't have any friends</p>
                {/if}
            </div>
        </div>
        <div class="h-full flex flex-col gap-6 w-1/3">
            <div class="p-4 bg-white shadow rounded w-full overflow-y-auto h-full">
                <div class="flex flex-col gap-y-3">
                    <h4>Friend Requests</h4>
                    
                    {#if friendRequests && friendRequests.length > 0}
                        {#each friendRequests as request}
                            <div class="flex justify-between items-center py-2">
                                <div class="flex items-center gap-x-2">
                                    <div class="w-8 h-8 rounded-full bg-amber-100 flex items-center justify-center text-amber-600 font-semibold">
                                        {request.sender.username.charAt(0).toUpperCase()}
                                    </div>
                                    <div>
                                        <p class="font-medium">{request.sender.username}</p>
                                        <p class="text-xs text-gray-500">
                                            {new Date(request.created_at).toLocaleDateString()}
                                        </p>
                                    </div>
                                </div>
                                <div class="flex gap-x-2">
                                    <button class="btn-primary text-xs px-2 py-1">Accept</button>
                                    <button class="btn-secondary text-xs px-2 py-1">Decline</button>
                                </div>
                            </div>
                            <hr class="my-2" />
                        {/each}
                    {:else}
                        <p class="text-sm text-gray-500 py-2">No pending friend requests</p>
                    {/if}
                </div>
            </div>
            <!-- <div class="py-4 px-6 bg-white shadow rounded w-full overflow-y-scroll h-1/2">
                <div class="flex flex-col gap-y-3">
                    <h4></h4>
                </div>
            </div> -->
        </div>
    </div>
</div>