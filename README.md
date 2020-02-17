# Save your git checkout history

1. Clone this repo;
2. In interesting repos do the following:

        cd repo
        ln -s <full_path_to_cloned>/post_checkout_log/post_checkout_hook.py post-checkout
        
3. History of your branches checkout will appear here:

        cat ~/.git_history

    The format is CSV with following columns:
    
        utc_iso_time,repo_path,prev_head,next_head
