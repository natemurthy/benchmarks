# results

In each test an instance of a server was launched on a t2.medium EC2 node
in the us-west-2 region, and the benchmark client was executed on my local
machine. All things being equal, networking latency should even out so that
the effects of executing I/O requests on the server are the true measure of
response time. When testing yourself, be sure to run on separate machines
so that concurrent requests from your benchmark client don't saturate the 
CPU needs of your test server.
