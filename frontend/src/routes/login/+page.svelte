<script lang="ts">
    let email = $state('');
    let password = $state('');
    let errorMsg = $state('');
    let loading = $state(false);

    async function handleSubmit(e: SubmitEvent) {
        e.preventDefault();
        errorMsg = '';
        
        if (password.length < 8) {
            errorMsg = 'Password must be at least 8 characters';
            return;
        }
        
        loading = true;
        
        try {
            // login
            
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
                <h3>Login</h3>
                {#if errorMsg}
                    <div class="text-red-500 mb-4">{errorMsg}</div>
                {/if}
                
                <form class="flex flex-col gap-y-3 w-full" onsubmit={handleSubmit}>
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
                                        
                    <button class="btn-primary w-full h-8 mt-2" type="submit" disabled={loading}>
                        {loading ? 'Logging in...' : 'Login'}
                    </button>
                </form>
                
                <div>
                    Don't have an account? <a class="link" href="/login">Sign up</a>
                </div>
            </div>
            </div>
    </div>
</section>