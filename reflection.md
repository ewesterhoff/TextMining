# Project Overview
This project draws useless insights from many semi-coherent religions. Using a webscaper, text files from a collected list of religions are created and stored in a folder.  These text files are then read, and analyzed using Markov chains to create randomly generated speech from a combination of all the religious documents. This speech has to be parsed by the human mind, but can contain some surprisingly good nuggets.

# Implementation
This implementation is done in two parts: fetching and generating.  The fetching is done in fetch_files.py.  We travel to the website containing our content, and we know that the first 16 links on that page lead to large enough religions to gather religious documents.  We follow those sixteen links to their respective pages, and store the links of all text files on those pages in a list.  The second section of this code creates a folder in the working directory, sweeps through the list of texts, and stores all of the data in relevantly named files.

The second part deals with text analysis: the program sweeps through all of the created text files, and maps words to their prefixes and suffixes.  These values are appropriately stored in a dictionary, which is then used to randomly generate text from the frequencies stored in the dictionary.

One major design decision I had to make in the creation of this code is how to search for, handle, and store the text files.  Two major searching approaches could be used: the first follows the first link to its page, gathers all the text files, then travels back and repeats.  The approach that I choose was more intermediate; first I selected the religions I wanted, then traveled to those pages independently.  This was a slower approach, but makes the code easier to understand.  My code works like a human to-do list: creating a list of links that I should follow, then completing them one at a time.  This also means that I have a list of religions stored somewhere, which could be used in future iterations.

# Results
My personal goal for this assignment was to create randomly generated text that made the user feel uncomfortable.  My first approach was to use a badly written pseudo-novel 'my immortal' as the basis for text generation, but this writing was so laden with misspellings and grammatical errors that the results were nonsensical.  My next thought was that religion is often an uncomfortable topic, so why not use that to my advantage?  Looking online, hundreds of religious documents were available for download.  I build a scraper (which was not part of my original plan) to download them all.  Below are some of the insights that my code generated

### Magic is nothing compared to mere infinity
That is further, in more leaps than a mere infinite number. The Absolute Infinite is unknowable in the truest sense, a helper of humanity, when the candidate has lived such a life for a life. Magic--the influence of enemies. Much sickness was heralded

### The PTL, feds, and Seraphim must all work together
The group, long affiliated with PTL Club, was honored by the state governors or by the regional (subfederal) executives, by the chief executive of Babylon, while Gabriel worked quite alone with Michael and the celestial Choir of Seraphim

### High standards for our children, artisans and masons
Every child graduating from the precollege school system at eighteen is a skilled artisan. Then begins the study of the seven training worlds of the universe, much more far-reaching than the royal families, supposedly descended from the Gods, so is the way to taste even on earth the truth of this promise, having lived by it for the past, and let you comment on them: There is an additional factor in building, the soul body, the golden garment" of the mystic Mason and which he must carry out in tranquillity the plan of action accepted without validation.

### The fountain of all wisdom is puberty, apparently a facet of satanism
The will give them good grass-land for their food, till a priest came to give worship at the feet of Osiris, so that the period of puberty may last eternity. From this period the supreme council at universe headquarters, but this representation is suspended by rebellion. Satania now has an observer at the headquarters of the superuniverse training regime

### Sexual symbolism in dog poop?
This branch of magic is a central figure of the deceased; Slip a whoopee cushion under the widow. Leave some phony dog poop on top of their temples. Moroni didn't die for them. FOR if they would follow that bent in accor- dance with my advice. Indeed the surprise is that there is sexual symbolism here, have brought me to the test of time, where 'seeing the future' is an illogical

# Reflection
This was definitely not an appropriately scoped project.  My original idea was simple Markov text generation from a text file or two, no more than five (not requiring a web scraper) In the 24 hours before the deadline, I very quickly changed my mind about the direction of the project.  This shift occurred because I didn't really plan out my project ahead of time, or didn't like the vague idea I was working towards.  Overall though, the productivity of my code writing sessions was very high due to my increased ability to find answers online.  Unit testing was something I hope to work more on in the next project: because I was so focused on results I would often try and test blocks of code at a time.  I did have a unit testing success that is easily traceable: get_content.py where I tested my ability to download information from a text file in browser separate from scraping through hundreds of them.
