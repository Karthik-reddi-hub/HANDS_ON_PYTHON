playlist=list(map(int,input("Enter song durations in seconds : ").split()))

if any(duration<=0 for duration in playlist):
    print("\nInvalid playlist : Duration must be greater than 0")
else:
    total_duration=sum(playlist)
    number_of_songs=len(playlist)

    is_repetitive=len(playlist)!=len(set(playlist))

    if total_duration<300:
        category="Too Short playlist"
        recommendation="Add more songs"

    elif total_duration>3600:
        category="Too Long Playlist"
        recommendation="Consider trimming your playlist"

    elif is_repetitive:
        category="Repetitive Playlist"
        recommendation="Add variety"
        
    else:
        if max(playlist)-min(playlist)>600:
            category="Irregular Playlist"
            recommendation="Adjust song duration balance"
        else:
            category="Balanced Playlist"
            recommendation="Good listening session"

print("\nTotal Duration:", total_duration, "seconds")
print("Songs:", number_of_songs)
print("Category:", category)
print("Recommendation:", recommendation)

