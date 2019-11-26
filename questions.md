# Questions

## Question 1

Fill in the two functions `compute_histogram_bins` and `plot_histogram` in `histogram.py`. As an example, we would like to be able to plot something similar to histogram_example.png` as a minimum result.

## Question 2

Go to the file `question2.py`:
1. fill in `send_data_to_backend` so that it returns the list of the peer's connection durations.
2. fill in `process_backend_data` which must do all necessary processing to return the connection durations histogram bins counts. **Don't call `plot_histogram` in this method, we just want to compute the histogram bins counts**.

## Question 3

With peers sending such datastructure and our _backend_ server making such operations, we retrieve exactly **all** the connection durations on the network at the moment of the snapshot and we are able to plot the _exact distribution_ of the connection durations.
1. `question2.py` main has several simulations with increasing numbers of peers and peer pool size. Run the simulations with your implementation. What do you see? Can you explain the limitations of the implementations of question 2 taking into account that a _real_ peer network can have _millions_ of peers? (answer below in this file)
>> In the current version I am collecting all the durations with its pairs and after execution of the function "compute_histogram_bins" we are obliged to post-process our result, dividing the number of elements in each bin by 2.
>> This approach spends a lot of time to collect and count a lot of redundant data. The execution time is growing in general tenfold, while we are increasing "number_of_peers" or "max_peer_pool_size" by 10.

## Question 4

Go to the file `question4.py`:
1. propose new implementations of `send_data_to_backend` and `process_backend_data` that can deal with millions of peers _and_ still provide a good representation of the _distribution_ of the connection duration. You are free to add any written comments, add pictures etc...to enhance your answer.
>> In the second version, I've created a temporary dictionary of peers and its pool, which are also dictionaries, to be able to delete the "twin" of already added connection time.
>> Hence, function "compute_histogram_bins" computes half the data in comparison with previous case. Moreover, we don't need to post-process our result.
>> Such implementation allows to down execution time by a factor of 1.5 (for example: number of peers = 1000000, max pool size - 10: Q2 method ~ 53 seconds; Q4 method ~ 34).
>> 
>>From the other side, current method requires much more memory for a dictionary of dictionaries, that we can exclude, deleting twins from our backend database 
>> (in this case we need to change the data type of this variable and the way we are retrieving data, that I didn't have access to under the terms of this exercise), but in this case we are going to delete the history of the snapshot.

