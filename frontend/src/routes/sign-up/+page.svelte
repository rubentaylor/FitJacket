<script lang="ts">
    let name = $state('');
    let email = $state('');
    let password = $state('');
    let confirmPassword = $state('');
    let errorMsg = $state('');
    let loading = $state(false);

    async function handleSubmit(e: SubmitEvent) {
        e.preventDefault();
        errorMsg = '';
        
        if (password !== confirmPassword) {
            errorMsg = 'Passwords do not match';
            return;
        }
        
        if (password.length < 8) {
            errorMsg = 'Password must be at least 8 characters';
            return;
        }
        
        loading = true;
        
        try {
            // sign up
            
            // Redirect to login or dashboard
            window.location.href = '/dashboard';
        } catch (error) {
            errorMsg = 'An error occurred during sign up';
        } finally {
            loading = false;
        }
    }
</script>

<section>
    <div class="w-full h-[100vh] flex items-center justify-center">
        <div class="w-[360px] py-6 px-8 bg-white shadow rounded">
            <div class="flex flex-col items-center gap-y-6">
                <h3>Sign Up</h3>
                {#if errorMsg}
                    <div class="text-red-500 mb-4">{errorMsg}</div>
                {/if}
                
                <form class="flex flex-col gap-y-3 w-full" onsubmit={handleSubmit}>
                    <div class="flex flex-col gap-y-1">
                        <label for="name" class="text-sm">Name</label>
                        <input class="input h-9"
                            type="text" 
                            id="name" 
                            bind:value={name} 
                            required 
                            disabled={loading}
                        />
                    </div>
                    
                    <div class="flex flex-col gap-y-1">
                        <label for="email" class="text-sm">Email</label>
                        <input class="input h-9"
                            type="text" 
                            id="email" 
                            bind:value={email} 
                            required 
                            disabled={loading}
                        />
                    </div>
                    
                    <div class="flex flex-col gap-y-1">
                        <label for="password" class="text-sm">Password</label>
                        <input class="input h-9"
                            type="text" 
                            id="password" 
                            bind:value={password} 
                            required 
                            disabled={loading}
                        />
                    </div>
                    
                    <div class="flex flex-col gap-y-1">
                        <label for="confirmPassword" class="text-sm">Confirm Password</label>
                        <input class="input h-9"
                            type="text" 
                            id="confirmPassword" 
                            bind:value={confirmPassword} 
                            required 
                            disabled={loading}
                        />
                    </div>
                    
                    <button class="btn-primary w-full h-8 mt-2" type="submit" disabled={loading}>
                        {loading ? 'Creating account...' : 'Sign Up'}
                    </button>
                </form>
                
                <div>
                    Already have an account? <a class="link" href="/login">Log in</a>
                </div>
            </div>
            </div>
    </div>
</section>